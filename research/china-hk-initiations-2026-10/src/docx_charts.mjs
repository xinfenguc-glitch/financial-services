// Render every chart in build/docx/charts.html to a 3x PNG (build/docx/img/<id>.png) for the Word version.
import { createRequire } from "module";
import fs from "fs";
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
const dir = path.join(here, "build", "docx");
const imgDir = path.join(dir, "img");
fs.mkdirSync(imgDir, { recursive: true });

const browser = await playwright.chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 3, viewport: { width: 900, height: 900 } });
await page.goto(pathToFileURL(path.join(dir, "charts.html")).href, { waitUntil: "networkidle" });
await page.evaluate(() => document.fonts.ready);
const ids = await page.$$eval("div.c", (els) => els.map((e) => e.id));
for (const id of ids) {
  await page.locator(`#${id} > svg`).screenshot({ path: path.join(imgDir, `${id}.png`), omitBackground: false });
}
await browser.close();
console.log(`rendered ${ids.length} charts -> ${imgDir}`);
