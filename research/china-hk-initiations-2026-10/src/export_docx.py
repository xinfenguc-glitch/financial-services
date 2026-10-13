"""Export the report as a block model for the Word version (make_docx.mjs renders it).

Run:  python3 export_docx.py    -> build/docx/model.json, build/docx/charts.html
      node docx_charts.mjs      -> build/docx/img/*.png
      node make_docx.mjs        -> ../China_HK_17_Initiations_2026-10-12.docx

Text, numbers and tables come from the same functions build.py uses for the HTML/PDF version.
"""
import html
import json
import os
import re
from html.parser import HTMLParser

import build as B
from v2_forces import FORCES

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "build", "docx")

CHARTS = {}          # id -> svg markup


def chart(cid, svg):
    CHARTS[cid] = svg
    w = float(re.search(r'width="([\d.]+)"', svg).group(1))
    h = float(re.search(r'height="([\d.]+)"', svg).group(1))
    return {"type": "image", "id": cid, "w": w, "h": h}


# ----------------------------------------------------------------------------- inline HTML -> runs
class _Runs(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.runs, self.b, self.i = [], 0, 0

    def handle_starttag(self, tag, attrs):
        if tag in ("b", "strong"):
            self.b += 1
        elif tag in ("i", "em"):
            self.i += 1

    def handle_endtag(self, tag):
        if tag in ("b", "strong"):
            self.b -= 1
        elif tag in ("i", "em"):
            self.i -= 1

    def handle_data(self, data):
        if data:
            self.runs.append({"t": data, "b": self.b > 0, "i": self.i > 0})


def runs(s):
    """Inline HTML (b/i tags, entities) -> [{t, b, i}], whitespace collapsed as a browser would."""
    p = _Runs()
    p.feed(str(s))
    out = []
    for r in p.runs:
        t = re.sub(r"\s+", " ", r["t"].replace(" ", " "))
        if out and out[-1]["b"] == r["b"] and out[-1]["i"] == r["i"]:
            out[-1]["t"] += t
        else:
            out.append({**r, "t": t})
    if out:
        out[0]["t"] = out[0]["t"].lstrip()
        out[-1]["t"] = out[-1]["t"].rstrip()
    return [r for r in out if r["t"]]


def plain(s):
    return "".join(r["t"] for r in runs(s))


def para(s, style="body"):
    return {"type": "para", "runs": runs(s), "style": style}


def bullets(items, style="body"):
    return {"type": "bullets", "items": [runs(x) for x in items], "style": style}


def h2(t):
    return {"type": "h2", "text": t}


def label(t):
    return {"type": "label", "text": t}


def grid(left, right, split=0.5, rule=False):
    return {"type": "grid", "left": left, "right": right, "split": split, "rule": rule}


# ----------------------------------------------------------------------------- mini DOM for front/back matter
class _Dom(HTMLParser):
    VOID = {"br", "img", "meta", "hr"}

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.root = {"tag": "root", "attrs": {}, "kids": []}
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        n = {"tag": tag, "attrs": dict(attrs), "kids": []}
        self.stack[-1]["kids"].append(n)
        if tag not in self.VOID:
            self.stack.append(n)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i]["tag"] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        self.stack[-1]["kids"].append(data)

    def handle_entityref(self, name):
        self.stack[-1]["kids"].append(f"&{name};")

    def handle_charref(self, name):
        self.stack[-1]["kids"].append(f"&#{name};")


def dom(s):
    p = _Dom()
    p.feed(s)
    return p.root


def inner(n):
    """Serialise a node's children back to inline HTML (for runs())."""
    out = []
    for k in n["kids"]:
        if isinstance(k, str):
            out.append(k)
        else:
            out.append(f"<{k['tag']}>{inner(k)}</{k['tag']}>")
    return "".join(out)


def cls(n):
    return n["attrs"].get("class", "") if isinstance(n, dict) else ""


def dom_blocks(n):
    """Front/back-matter HTML -> blocks (headings, paragraphs, lists, two-column grids, charts)."""
    out = []
    for k in n["kids"]:
        if isinstance(k, str):
            if k.strip():
                out.append(para(k))
            continue
        c, t = cls(k), k["tag"]
        if "sec-h" in c:
            out.append({"type": "h1", "text": plain(inner(k))})
        elif t == "h4":
            out.append({"type": "h3", "text": plain(inner(k))})
        elif t == "p":
            out.append(para(inner(k), "disc" if "disc" in c else "body"))
        elif t == "ul":
            out.append(bullets([inner(li) for li in k["kids"] if isinstance(li, dict) and li["tag"] == "li"]))
        elif t == "img" and k["attrs"].get("data-chart"):
            cid = k["attrs"]["data-chart"]
            out.append(chart(cid, CHARTS[cid]))
        elif "two" in c:
            cols = [x for x in k["kids"] if isinstance(x, dict)]
            out.append(grid(dom_blocks(cols[0]), dom_blocks(cols[1]), 0.5))
        else:
            out.extend(dom_blocks(k))
    return out


# ----------------------------------------------------------------------------- tables
def num_table(head, rows, est_from, widths, first_w=None):
    """Numeric table: head = [title, col...]; rows = (label, values, row_class)."""
    return {"type": "table", "kind": "num", "head": [plain(h) for h in head],
            "rows": [{"cells": [plain(lab)] + [plain(v) for v in vals], "cls": rc} for lab, vals, rc in rows],
            "est_from": est_from, "widths": widths}


def txt_table(head, rows, widths, kind="txt"):
    return {"type": "table", "kind": kind, "head": list(head) if head else None,
            "rows": [{"cells": [plain(c) for c in r], "cls": ""} for r in rows], "widths": widths}


def kv_table(rows, widths=(46, 54)):
    return {"type": "table", "kind": "kv", "head": None,
            "rows": [{"cells": [plain(a), plain(b)], "cls": ""} for a, b in rows], "widths": list(widths)}


# ----------------------------------------------------------------------------- company
def company(idx, co, m):
    ph, fa = m["ph"], m["fa"]
    f = lambda s: B.fill(s, ph)
    short = B.SHORT[co["key"]]
    ccy_tp = co["ccy"] if co["ccy"] == "HK$" else "RMB"
    blocks = [{"type": "pagebreak"},
              {"type": "band", "kicker": f"{idx:02d} · {co['theme']} · {co['sector']}".upper(),
               "name": short, "cn": co["cn"], "ticker": f"{co['ticker']} · Initiation of coverage · {B.AS_OF}",
               "rating": m["rating"], "tp": f"{ccy_tp}{B.tp_str(m['tp'])}",
               "px": f"Price {B.price_fmt(co['price'], co['ccy'])} · {B.pct(m['up'], 0, sign=True)}"},
              {"type": "headline", "runs": runs(f(co["headline"]))}]

    left = [para(f(co["summary"]), "lede"), bullets([f(x) for x in co["thesis"]]),
            label("Catalysts"), bullets([f(x) for x in co["catalysts"]], "small"),
            label(co.get("risks_title", "Key risks")), bullets([f(x) for x in co["risks"]], "small")]
    right = [label("Key data"), kv_table(B.key_data_rows(co, m))]
    if co.get("mix"):
        right += [label(co["mix_title"]), chart(f"mix_{co['key']}", B.svg_mix(co["mix"]))]
    else:
        right += [label("Key operating indicators"), kv_table(co["kpis"], (52, 48))]
    blocks.append(grid(left, right, 0.63, rule=True))

    fx_note = ("" if co["ccy"] == "RMB" else ", converted at HK$1 = RMB0.853" if co["fin_unit"].startswith("RMB")
               else ", converted at US$1 = HK$7.8475")
    blocks += [h2("Key financials and valuation"),
               num_table(["Year to December"] + B.YEARS, B.fin_rows(co, m), 3, [31] + [11.5] * 6),
               para("A = actual (company reports; StockAnalysis/S&amp;P Global), E = our estimates. Multiples at the "
                    f"12-Oct-2026 price{fx_note}.", "cap")]

    # qualitative sections
    blocks += [h2("Company background")] + [para(f(x)) for x in co["background"]]
    blocks.append(grid([label("Milestones"), kv_table(co["milestones"], (17, 83))],
                       [label("Ownership and listing"), kv_table(co["ownership"], (38, 62))], 0.6))
    blocks += [h2("The business")] + [para(f(x)) for x in co["business"]]
    seg_cols = co.get("segments_cols", ("Segment", "Share of revenue", "Key assets / products", "Economics"))
    blocks += [label(co["segments_title"]), txt_table(seg_cols, co["segments"], [19, 12, 38, 31])]
    blocks += [h2("Competitive landscape")] + [para(f(x)) for x in co["competition"]]
    blocks += [label("Main competitors"),
               txt_table(("Competitor", "Base", "Focus", "Position vs " + short), co["competitors"], [19, 12, 34, 35]),
               label("Industry structure: five forces"),
               {"type": "table", "kind": "forces", "head": ["Force", "Intensity", "Assessment"],
                "rows": [{"cells": [a, lv, plain(t)], "cls": ""} for a, lv, t in FORCES[co["key"]]],
                "widths": [15, 11, 74]},
               label("Moat and vulnerabilities"), bullets(co["moat"])]
    blocks += [h2("Addressable market (TAM)")] + [para(f(x)) for x in co["tam"]]
    blocks += [txt_table(("Market", "Size", "Growth / dynamics", "Source"), co["tam_table"], [19, 22, 35, 24]),
               {"type": "tiles", "items": [[v, l] for v, l in co["tiles"]]}]

    # financial analysis
    unit = co["fin_unit"]
    np_title = "Net profit" if co["profile"] == "profit" else co["loss_label"].replace(" (loss)", "")
    fcf_series = fa["fcf_h"][:3] + fa["fcf_e"]
    k = co["key"]
    blocks += [h2("Financial analysis"),
               {"type": "row", "items": [chart(f"rev_{k}", B.svg_columns(m["rev"], "Revenue", unit, 228, 150)),
                                         chart(f"np_{k}", B.svg_columns(m["np"], np_title, unit, 228, 150)),
                                         chart(f"fcf_{k}", B.svg_columns(fcf_series, "Free cash flow", unit, 228,
                                                                         150))]},
               para(f(co["fin_is"]))]
    bh, br, _ = B.bs_data(co, fa)
    debt_note = (" and, pre-IPO, preferred shares carried as liabilities" if k in ("horizon", "minimax") else "")
    blocks.append(grid([num_table(bh, br, None, [40, 15, 15, 15, 15]),
                        para("Source: company filings via StockAnalysis/S&amp;P Global. Jun-26 = latest interim balance "
                             f"sheet. Debt includes leases{debt_note}.", "cap")],
                       [para(f(co["fin_bs"]))], 0.5))
    ch, cr, ce = B.cf_data(co, m, fa)
    blocks += [num_table(ch, cr, ce, [27] + [73 / 7] * 7),
               para("TTM = twelve months to June 2026; Jun-26 net cash in the TTM column. E = our estimates: OCF = net "
                    "profit + D&amp;A − increase in working capital; net cash rolls forward FCF less dividends plus "
                    "equity raised.", "cap"),
               para(f(co["fin_cf"]))]
    rh, rr, re_ = B.ratio_data(co, m, fa)
    rt_note = ("ROE/ROA on average balances. Days on year-end balances: receivables on revenue, inventory and payables "
               "on cost of sales. Net debt/equity below zero = net cash. "
               + ("Payout = DPS/EPS. " if co["profile"] == "profit" else "")
               + "n.m./– = not meaningful or not modelled.")
    blocks.append(grid([num_table(rh, rr, re_, [31] + [11.5] * 6), para(rt_note, "cap")],
                       [para(f(co["fin_ratios"]))], 0.62))

    # valuation
    ph_head, ph_rows, ph_cap = B.peer_rows(co, m)
    scen = co["scen"]
    scen_note = (f'Bear ({scen["bear"]["desc"]}): {B.price_fmt(m["bear"], co["ccy"])}. '
                 f'Bull ({scen["bull"]["desc"]}): {B.price_fmt(m["bull"], co["ccy"])}.')
    peers = txt_table(ph_head, ph_rows, [33, 17, 16, 18, 16], "peers")
    blocks += [h2("Valuation"),
               grid([peers, para(html.escape(ph_cap), "cap")],
                    [chart(f"scen_{k}", B.svg_scenarios(co, m)), para(html.escape(scen_note), "cap")], 0.55),
               para(f(co["valuation"])),
               para("Sources: " + html.escape(co["sources"]), "src")]
    return blocks


# ----------------------------------------------------------------------------- front matter
def cover(cos):
    n = dom(B.cover(cos))
    sec = [k for k in n["kids"] if isinstance(k, dict)][0]
    find = lambda c: next(k for k in sec["kids"] if isinstance(k, dict) and c in cls(k))
    h1 = next(k for k in sec["kids"] if isinstance(k, dict) and k["tag"] == "h1")
    stats = []
    for t in find("cv-stats")["kids"]:
        if isinstance(t, dict):
            divs = [d for d in t["kids"] if isinstance(d, dict)]
            stats.append([plain(inner(divs[0])), plain(inner(divs[1]))])
    box = [para(inner(p), "cover") for p in find("cv-box")["kids"] if isinstance(p, dict) and p["tag"] == "p"]
    title = plain(inner(h1).replace("<br>", " "))
    return [{"type": "cover", "kicker": plain(inner(find("cv-top"))), "title": title,
             "sub": plain(inner(find("cv-sub"))), "meta": plain(inner(find("cv-meta"))), "stats": stats,
             "box": box, "foot": runs(inner(find("cv-foot")))}]


def summary(cos):
    rows = []
    for i, (c, m) in enumerate(cos, 1):
        if c["profile"] == "profit":
            v26, v27, lab = B.mult(m["pe"][3]), B.mult(m["pe"][4]), "P/E"
        else:
            v26, v27, lab = B.mult(m["evs"][3]), B.mult(m["evs"][4]), "EV/S"
        rows.append({"cells": [str(i), {"name": B.SHORT[c["key"]], "sub": c["ticker"]}, {"pill": m["rating"]},
                               B.price_fmt(c["price"], c["ccy"]), B.price_fmt(m["tp"], c["ccy"]),
                               B.pct(m["up"], 0, sign=True), f"{m['mcap_usd']:,.1f}", f"{lab} {v26}", v27,
                               plain(B.fill(c["headline"], m["ph"]))], "cls": ""})
    return [{"type": "h1", "text": "Summary of ratings and valuation"},
            {"type": "table", "kind": "sum",
             "head": ["#", "Company", "Rating", "Price", "Target", "Return", "Mkt cap US$bn", "FY26E", "FY27E",
                      "One-line view"],
             "rows": rows, "widths": [3.5, 15, 7, 9, 9, 6.5, 7, 9, 6, 28]},
            para("Prices are 12-Oct-2026 closes (A-shares in RMB; H-shares in HK$). P/E for H-share-rated names uses "
                 "the H-share price. EV/S = enterprise value / sales for loss-making companies. Ratings: Buy ≥ +20% "
                 "implied return; Sell ≤ −10%; Hold otherwise.", "cap")]


def themes(cos):
    chart_rows = sorted([(B.SHORT[c["key"]], m["up"], m["rating"]) for c, m in cos], key=lambda r: r[1],
                        reverse=True)
    CHARTS["upside"] = B.svg_upside(chart_rows)
    s = re.sub(r"<svg.*?</svg>", '<img data-chart="upside">', B.themes_page(cos), flags=re.S)
    return [{"type": "pagebreak"}] + dom_blocks(dom(s))


def back():
    return [{"type": "pagebreak"}] + dom_blocks(dom(B.back_matter()))


def main():
    cos = B.load()
    blocks = cover(cos) + [{"type": "pagebreak"}] + summary(cos) + themes(cos)
    for i, (c, m) in enumerate(cos, 1):
        blocks += company(i, c, m)
    blocks += back()
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "model.json"), "w", encoding="utf-8") as fh:
        json.dump({"blocks": blocks, "as_of": B.AS_OF}, fh, ensure_ascii=False, indent=1)
    page = ["<!doctype html><html><head><meta charset='utf-8'><style>", B.CSS,
            "body{margin:0;background:#fff} .c{display:inline-block;padding:2px;background:#fff}</style></head><body>"]
    for cid, svg in CHARTS.items():
        page.append(f'<div class="c" id="{cid}">{svg}</div><br/>')
    page.append("</body></html>")
    with open(os.path.join(OUT, "charts.html"), "w", encoding="utf-8") as fh:
        fh.write("".join(page))
    print(f"{len(blocks)} blocks, {len(CHARTS)} charts -> {OUT}")


if __name__ == "__main__":
    main()
