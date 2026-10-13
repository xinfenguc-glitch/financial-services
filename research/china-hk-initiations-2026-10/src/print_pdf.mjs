// Render ../report.html to PDF with running header/footer (Playwright + bundled Chromium).
// Usage: node print_pdf.mjs [output.pdf]
import { createRequire } from "module";
import path from "path";
import { fileURLToPath, pathToFileURL } from "url";

const require = createRequire(import.meta.url);
let playwright;
try {
  playwright = require("playwright");
} catch {
  playwright = require("/opt/node22/lib/node_modules/playwright");
}

const here = path.dirname(fileURLToPath(import.meta.url));
const input = path.join(here, "..", "report.html");
const output = process.argv[2] || path.join(here, "..", "China_HK_17_Short_Initiations_2026-10-12.pdf");

const browser = await playwright.chromium.launch();
const page = await browser.newPage();
await page.goto(pathToFileURL(input).href, { waitUntil: "networkidle" });
await page.evaluate(() => document.fonts.ready);
await page.pdf({
  path: output,
  format: "Letter",
  printBackground: true,
  preferCSSPageSize: true,
  displayHeaderFooter: true,
  headerTemplate: `<div style="width:100%;font-family:Inter,sans-serif;font-size:6.5pt;color:#898781;padding:0 0.55in;
      display:flex;justify-content:space-between;"><span>China &amp; HK: 17 Initiations</span>
      <span>12 October 2026</span></div>`,
  footerTemplate: `<div style="width:100%;font-family:Inter,sans-serif;font-size:6.5pt;color:#898781;padding:0 0.55in;
      display:flex;justify-content:space-between;"><span>AI-assisted research for information only; not investment
      advice. See disclosures.</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
  margin: { top: "0.62in", bottom: "0.62in", left: "0.55in", right: "0.55in" },
});
await browser.close();
console.log("wrote", output);
