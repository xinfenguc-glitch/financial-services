// Build the Word version of the report from build/docx/model.json (export_docx.py) and build/docx/img/*.png
// (docx_charts.mjs).  Usage: node make_docx.mjs [output.docx]
import { createRequire } from "module";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const require = createRequire(import.meta.url);
const {
  AlignmentType, BorderStyle, Document, Footer, Header, ImageRun, LevelFormat, Packer, PageNumber, Paragraph,
  ShadingType, Table, TableCell, TableLayoutType, TableRow, TabStopType, TextRun, VerticalAlign, WidthType,
  HeadingLevel, LineRuleType,
} = require("docx");

const here = path.dirname(fileURLToPath(import.meta.url));
const dir = path.join(here, "build", "docx");
const model = JSON.parse(fs.readFileSync(path.join(dir, "model.json"), "utf-8"));
const output = process.argv[2] || path.join(here, "..", "China_HK_17_Initiations_2026-10-12.docx");

// ---------------------------------------------------------------- page geometry and palette
const PAGE_W = 12240, PAGE_H = 15840, MX = 792, MY = 893;   // US Letter; 0.55in / 0.62in margins
const TEXT_W = PAGE_W - 2 * MX;                             // 10656 DXA = 7.4in
const C = {
  ink: "0B0B0B", ink2: "52514E", muted: "898781", grid: "E1E0D9", axis: "C3C2B7", accent: "104281",
  wash: "EEF4FC", tile: "FBFBFA",
};
const FONT = "Arial";
const CJK = { ascii: FONT, hAnsi: FONT, cs: FONT, eastAsia: "Microsoft YaHei" };
const PILL = {
  buy: ["E3F3E3", "006300"], hold: ["ECEBE6", "3D3C39"], sell: ["FBE4E4", "B02A2A"],
  high: ["FBE4E4", "B02A2A"], medium: ["FDF0D8", "8A5A00"], low: ["E3F3E3", "006300"],
};
const NONE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const NO_BORDERS = { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE };
const line = (color = C.grid, size = 4) => ({ style: BorderStyle.SINGLE, size, color });

// ---------------------------------------------------------------- text helpers
const STYLE_IDS = {
  body: "Normal", lede: "Lede", cap: "Cap", src: "Src", disc: "Disc", small: "Small", cover: "CoverBody",
};
let pendingBreak = false;
function takeBreak() {
  const b = pendingBreak;
  pendingBreak = false;
  return b;
}

function textRuns(runs, extra = {}) {
  return runs.map((r) => new TextRun({ text: r.t, bold: r.b || extra.bold, italics: r.i, ...extra }));
}

function P(opts) {
  return new Paragraph({ ...opts, pageBreakBefore: takeBreak() || opts.pageBreakBefore });
}

function pill(label, key, size = 14) {
  const [fill, color] = PILL[key] || PILL.hold;
  return new TextRun({
    text: ` ${label} `, bold: true, size, color, shading: { type: ShadingType.CLEAR, color: "auto", fill },
  });
}

// ---------------------------------------------------------------- tables
const dxa = (weights, width) => {
  const tot = weights.reduce((a, b) => a + b, 0);
  const out = weights.map((w) => Math.floor((w / tot) * width));
  out[out.length - 1] += width - out.reduce((a, b) => a + b, 0);
  return out;
};

function cellPara(children, { align = AlignmentType.LEFT, keepNext = false, indent, spacing } = {}) {
  return new Paragraph({
    children, alignment: align, keepNext, indent,
    spacing: spacing || { before: 0, after: 0, line: 240, lineRule: LineRuleType.AUTO },
  });
}

function cell(paras, width, { fill, borders, vAlign, margins } = {}) {
  return new TableCell({
    children: paras, width: { size: width, type: WidthType.DXA },
    shading: fill ? { type: ShadingType.CLEAR, color: "auto", fill } : undefined,
    borders: borders || { top: NONE, left: NONE, right: NONE, bottom: line() },
    verticalAlign: vAlign || VerticalAlign.TOP, margins,
  });
}

function table(b, width) {
  const cols = dxa(b.widths, width);
  const kind = b.kind;
  const size = kind === "sum" ? 14 : 15;
  const isNum = kind === "num";
  const est = b.est_from;
  const estCol = (i) => isNum && est !== null && est !== undefined && i >= 1 && i - 1 >= est;
  const alignOf = (i) => {
    if (isNum) return i === 0 ? AlignmentType.LEFT : AlignmentType.RIGHT;
    if (kind === "peers") return i < 2 ? AlignmentType.LEFT : AlignmentType.RIGHT;
    if (kind === "sum") return [3, 4, 5, 6].includes(i) ? AlignmentType.RIGHT : AlignmentType.LEFT;
    return AlignmentType.LEFT;
  };
  const rows = [];
  const nRows = b.rows.length;
  if (b.head) {
    rows.push(new TableRow({
      tableHeader: true, cantSplit: true,
      children: b.head.map((h, i) => cell([cellPara([new TextRun({ text: h, bold: true, size, color: C.ink2 })],
        { align: alignOf(i), keepNext: true })], cols[i], {
        fill: estCol(i) ? C.wash : undefined, borders: { top: NONE, left: NONE, right: NONE, bottom: line(C.axis) },
        vAlign: VerticalAlign.BOTTOM,
      })),
    }));
  }
  b.rows.forEach((r, ri) => {
    const last = ri === nRows - 1;
    const keepNext = !last && nRows <= 20;
    const hl = r.cls === "hl" || (kind === "peers" && last);
    const sub = r.cls === "sub";
    const rowFill = kind === "peers" && last ? C.wash : undefined;
    const children = r.cells.map((c, i) => {
      let paras;
      const color = sub ? C.ink2 : (kind === "kv" && i === 0) ? C.ink2 : C.ink;
      const bold = hl || ((kind === "txt" || kind === "forces") && i === 0) || (kind === "kv" && i === 1 && false);
      if (c && typeof c === "object" && c.pill) {
        paras = [cellPara([pill(c.pill, c.pill.toLowerCase(), size)], { keepNext })];
      } else if (c && typeof c === "object" && c.name) {
        paras = [cellPara([new TextRun({ text: c.name, bold: true, size })], { keepNext }),
          cellPara([new TextRun({ text: c.sub, size: 11, color: C.muted })], { keepNext })];
      } else if (kind === "forces" && i === 1) {
        const key = String(c).split(" ").pop().toLowerCase();
        paras = [cellPara([pill(c, key, 12)], { keepNext })];
      } else {
        const runColor = kind === "sum" && i === 9 ? C.ink2 : color;
        paras = [cellPara([new TextRun({ text: String(c), bold, size: sub ? size - 1 : size, color: runColor })],
          { align: alignOf(i), keepNext, indent: sub && i === 0 ? { left: 140 } : undefined })];
      }
      return cell(paras, cols[i], { fill: estCol(i) ? C.wash : rowFill });
    });
    rows.push(new TableRow({ children, cantSplit: true }));
  });
  return new Table({
    rows, width: { size: width, type: WidthType.DXA }, columnWidths: cols, layout: TableLayoutType.FIXED,
    borders: NO_BORDERS, margins: { top: 22, bottom: 22, left: 50, right: 50 },
  });
}

// ---------------------------------------------------------------- images
function imageRun(id, wPx, hPx, maxPx) {
  const scale = maxPx && wPx > maxPx ? maxPx / wPx : 1;
  return new ImageRun({
    type: "png", data: fs.readFileSync(path.join(dir, "img", `${id}.png`)),
    transformation: { width: Math.round(wPx * scale), height: Math.round(hPx * scale) },
    altText: { title: id, description: `Chart ${id}`, name: id },
  });
}
const dxaToPx = (d) => (d / 1440) * 96;

// ---------------------------------------------------------------- blocks
function render(b, width) {
  switch (b.type) {
    case "pagebreak":
      pendingBreak = true;
      return [];
    case "h1":
      return [P({ heading: HeadingLevel.HEADING_1, children: [new TextRun(b.text)] })];
    case "h2":
      return [P({ heading: HeadingLevel.HEADING_2, children: [new TextRun(b.text)] })];
    case "h3":
      return [P({ heading: HeadingLevel.HEADING_3, children: [new TextRun(b.text)] })];
    case "label":
      return [P({ style: "Label", children: [new TextRun(b.text)] })];
    case "headline":
      return [P({ style: "Headline", children: textRuns(b.runs) })];
    case "para":
      return [P({ style: STYLE_IDS[b.style] || "Normal", children: textRuns(b.runs) })];
    case "bullets":
      return b.items.map((it, i) => P({
        style: b.style === "small" ? "Small" : "Normal", numbering: { reference: "bullets", level: 0 },
        spacing: b.style === "small" ? undefined : { after: i === b.items.length - 1 ? 120 : 70 },
        children: textRuns(it),
      }));
    case "table":
      return [table(b, width), new Paragraph({ style: "Spacer", children: [] })];
    case "image":
      return [P({ style: "Figure", children: [imageRun(b.id, b.w, b.h, dxaToPx(width) - 4)] })];
    case "row": {
      const runs = [];
      b.items.forEach((it, i) => {
        if (i) runs.push(new TextRun({ text: "  " }));
        runs.push(imageRun(it.id, it.w, it.h, (dxaToPx(width) - 12) / b.items.length));
      });
      return [P({ style: "Figure", keepNext: false, children: runs })];
    }
    case "tiles": {
      const n = b.items.length;
      const cols = dxa(Array(n).fill(1), width);
      const box = { top: line(), bottom: line(), left: line(), right: line() };
      return [new Table({
        width: { size: width, type: WidthType.DXA }, columnWidths: cols, layout: TableLayoutType.FIXED,
        borders: NO_BORDERS, margins: { top: 80, bottom: 80, left: 120, right: 120 },
        rows: [new TableRow({
          cantSplit: true,
          children: b.items.map(([v, l], i) => cell([
            cellPara([new TextRun({ text: v, bold: true, size: 24 })], { keepNext: true }),
            cellPara([new TextRun({ text: l, size: 13, color: C.ink2 })], { spacing: { before: 30, after: 0 } }),
          ], cols[i], { fill: C.tile, borders: box })),
        })],
      }), new Paragraph({ style: "Spacer", children: [] })];
    }
    case "grid": {
      const gap = 200;
      const [lw, rw] = dxa([b.split, 1 - b.split], width);
      const lInner = lw - gap / 2, rInner = rw - gap / 2;
      const kids = (blocks, w) => {
        const out = blocks.flatMap((x) => render(x, w));
        if (!out.length || out[out.length - 1] instanceof Table) out.push(new Paragraph({ children: [] }));
        return out;
      };
      const left = kids(b.left, lInner), right = kids(b.right, rInner - (b.rule ? 140 : 0));
      return [new Table({
        width: { size: width, type: WidthType.DXA }, columnWidths: [lw, rw], layout: TableLayoutType.FIXED,
        borders: NO_BORDERS,
        rows: [new TableRow({
          cantSplit: true,
          children: [
            cell(left, lw, { borders: { top: NONE, bottom: NONE, left: NONE, right: NONE },
              margins: { left: 0, right: gap / 2, top: 0, bottom: 0 } }),
            cell(right, rw, { borders: { top: NONE, bottom: NONE, right: NONE, left: b.rule ? line() : NONE },
              margins: { left: gap / 2 + (b.rule ? 140 : 0), right: 0, top: 0, bottom: 0 } }),
          ],
        })],
      }), new Paragraph({ style: "Spacer", children: [] })];
    }
    case "band": {
      const out = [P({ style: "Kicker", children: [new TextRun(b.kicker)] })];
      const [lw, rw] = dxa([0.7, 0.3], width);
      const bottom = { top: NONE, left: NONE, right: NONE, bottom: line(C.accent, 18) };
      const ratingKey = b.rating.toLowerCase();
      out.push(new Table({
        width: { size: width, type: WidthType.DXA }, columnWidths: [lw, rw], layout: TableLayoutType.FIXED,
        borders: NO_BORDERS, margins: { top: 0, bottom: 90, left: 0, right: 0 },
        rows: [new TableRow({
          cantSplit: true,
          children: [
            cell([
              new Paragraph({
                heading: HeadingLevel.HEADING_1, keepNext: true,
                children: [new TextRun(b.name), new TextRun({ text: `  ${b.cn}`, font: CJK, size: 22, bold: false, color: C.ink2 })],
              }),
              cellPara([new TextRun({ text: b.ticker, size: 15, color: C.ink2 })]),
            ], lw, { borders: bottom, vAlign: VerticalAlign.BOTTOM }),
            cell([
              cellPara([pill(b.rating.toUpperCase(), ratingKey, 17)], { align: AlignmentType.RIGHT, keepNext: true }),
              cellPara([new TextRun({ text: "TP ", size: 15, color: C.ink2 }), new TextRun({ text: b.tp, bold: true, size: 28 })],
                { align: AlignmentType.RIGHT, keepNext: true, spacing: { before: 40, after: 0 } }),
              cellPara([new TextRun({ text: b.px, size: 15, color: C.ink2 })], { align: AlignmentType.RIGHT }),
            ], rw, { borders: bottom, vAlign: VerticalAlign.BOTTOM }),
          ],
        })],
      }));
      return out;
    }
    case "cover": {
      const out = [
        new Paragraph({ style: "Kicker", spacing: { before: 1500, after: 200 }, children: [new TextRun(b.kicker.toUpperCase())] }),
        new Paragraph({ style: "CoverTitle", children: [new TextRun(b.title)] }),
        new Paragraph({ style: "CoverSub", children: [new TextRun(b.sub)] }),
        new Paragraph({ style: "Cap", spacing: { before: 200, after: 400 }, children: [new TextRun({ text: b.meta, size: 19 })] }),
      ];
      const tw = 1600;
      const box = { top: line(), bottom: line(), left: line(), right: line() };
      out.push(new Table({
        width: { size: tw * 3 + 400, type: WidthType.DXA }, columnWidths: [tw, 200, tw, 200, tw].slice(0, 5),
        layout: TableLayoutType.FIXED, borders: NO_BORDERS, margins: { top: 100, bottom: 100, left: 160, right: 160 },
        rows: [new TableRow({
          children: [0, 1, 2, 3, 4].map((i) => i % 2
            ? cell([new Paragraph({ children: [] })], 200, { borders: { top: NONE, bottom: NONE, left: NONE, right: NONE } })
            : cell([
              cellPara([new TextRun({ text: b.stats[i / 2][0], bold: true, size: 44 })]),
              cellPara([new TextRun({ text: b.stats[i / 2][1], size: 15, color: C.ink2 })]),
            ], tw, { fill: C.tile, borders: box })),
        })],
      }));
      out.push(new Paragraph({ style: "Spacer", spacing: { after: 360 }, children: [] }));
      b.box.forEach((p, i) => out.push(new Paragraph({
        style: "CoverBody", border: i === 0 ? { top: line(C.accent, 12) } : undefined,
        spacing: i === 0 ? { before: 0, after: 160 } : undefined, children: textRuns(p.runs),
      })));
      out.push(new Paragraph({ style: "Disc", spacing: { before: 1000 }, children: textRuns(b.foot) }));
      return out;
    }
    default:
      throw new Error(`unknown block ${b.type}`);
  }
}

// ---------------------------------------------------------------- document
const children = model.blocks.flatMap((b) => render(b, TEXT_W));

const para = (id, name, run, paragraph, extra = {}) => ({
  id, name, basedOn: "Normal", next: "Normal", quickFormat: true, run, paragraph, ...extra,
});

const doc = new Document({
  creator: "AI-assisted research",
  title: "China & HK: 17 Initiations",
  description: "Initiation notes on 17 China/Hong Kong stocks, 12 October 2026",
  styles: {
    default: { document: { run: { font: FONT, size: 18, color: C.ink } } },
    paragraphStyles: [
      { id: "Normal", name: "Normal", run: { font: FONT, size: 18, color: C.ink }, paragraph: { spacing: { before: 0, after: 140, line: 300, lineRule: LineRuleType.AUTO } } },
      para("Heading1", "Heading 1", { size: 32, bold: true, color: C.ink }, { spacing: { before: 0, after: 60 }, keepNext: true, outlineLevel: 0 }),
      para("Heading2", "Heading 2", { size: 20, bold: true, color: C.accent },
        { spacing: { before: 240, after: 80 }, keepNext: true, keepLines: true, outlineLevel: 1, border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: C.grid, space: 2 } } }),
      para("Heading3", "Heading 3", { size: 18, bold: true, color: C.ink }, { spacing: { before: 140, after: 50 }, keepNext: true, outlineLevel: 2 }),
      para("Label", "Table Title", { size: 16, bold: true, color: C.ink2 }, { spacing: { before: 130, after: 50 }, keepNext: true }),
      para("Headline", "Headline", { size: 23, bold: true, color: C.ink }, { spacing: { before: 140, after: 110 }, keepNext: true }),
      para("Kicker", "Kicker", { size: 14, bold: true, color: C.accent }, { spacing: { before: 0, after: 40 }, keepNext: true }),
      para("Lede", "Lede", { size: 19 }, { spacing: { after: 120 } }),
      para("Small", "Small", { size: 17 }, { spacing: { after: 50 } }),
      para("Cap", "Caption Note", { size: 14, color: C.muted }, { spacing: { before: 30, after: 90, line: 228, lineRule: LineRuleType.AUTO } }),
      para("Src", "Sources", { size: 13, color: C.muted },
        { spacing: { before: 120, after: 0, line: 228, lineRule: LineRuleType.AUTO }, border: { top: { style: BorderStyle.SINGLE, size: 4, color: C.grid, space: 3 } } }),
      para("Disc", "Disclosure", { size: 15, color: C.ink2 }, { spacing: { after: 90 } }),
      para("CoverTitle", "Cover Title", { size: 64, bold: true, color: C.ink }, { spacing: { before: 0, after: 200, line: 240, lineRule: LineRuleType.AUTO } }),
      para("CoverSub", "Cover Subtitle", { size: 23, color: C.ink2 }, { spacing: { after: 120 } }),
      para("CoverBody", "Cover Body", { size: 19 }, { spacing: { after: 160, line: 276, lineRule: LineRuleType.AUTO } }),
      para("Figure", "Figure", {}, { spacing: { before: 40, after: 60, line: 240, lineRule: LineRuleType.AUTO }, keepNext: false }),
      para("Spacer", "Spacer", { size: 4 }, { spacing: { before: 0, after: 40, line: 120, lineRule: LineRuleType.AUTO } }),
    ],
  },
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 220, hanging: 180 } } } }],
    }],
  },
  sections: [{
    properties: {
      page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MY, bottom: MY, left: MX, right: MX, header: 400, footer: 400 } },
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          tabStops: [{ type: TabStopType.RIGHT, position: TEXT_W }],
          children: [new TextRun({ text: "China & HK: 17 Initiations", size: 13, color: C.muted }),
            new TextRun({ text: `\t${model.as_of}`, size: 13, color: C.muted })],
        })],
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          tabStops: [{ type: TabStopType.RIGHT, position: TEXT_W }],
          children: [
            new TextRun({ text: "AI-assisted research for information only; not investment advice. See disclosures.", size: 13, color: C.muted }),
            new TextRun({ children: ["\t", PageNumber.CURRENT, " / ", PageNumber.TOTAL_PAGES], size: 13, color: C.muted }),
          ],
        })],
      }),
    },
    children,
  }],
});

// docx-js gives every drawing docPr id="1"; Word expects unique ids, so renumber them.
const JSZip = createRequire(require.resolve("docx"))("jszip");     // docx's own dependency
const zip = await JSZip.loadAsync(await Packer.toBuffer(doc));
let xml = await zip.file("word/document.xml").async("string");
let n = 0;
xml = xml.replace(/<wp:docPr id="\d+"/g, () => `<wp:docPr id="${++n}"`);
zip.file("word/document.xml", xml);
fs.writeFileSync(output, await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" }));
console.log("wrote", output);
