# China & HK: 17 Short Initiations (12 Oct 2026)

Short (2–3 page) initiation notes for the 17 China/Hong Kong stocks in the source pack
*"17 China/HK Stocks: Business Model, Performance and Outlook"* (6 Oct 2026). Each note covers company
background, business model, competitive landscape, TAM, a brief financial analysis (FY23A–FY28E) and
valuation (peer multiples, target price, bear/bull range).

- `China_HK_17_Short_Initiations_2026-10-12.pdf`: the report (46 pages, US Letter)
- `report.html`: the same content as a single HTML page
- `src/`: model inputs and text (`co_*.py`), build script (`build.py`) and PDF printer (`print_pdf.mjs`)

Rebuild:

```bash
cd src
python3 build.py        # writes ../report.html and prints each rating/TP
node print_pdf.mjs      # writes ../China_HK_17_Short_Initiations_2026-10-12.pdf (Playwright + Chromium)
```

Prices are 12-Oct-2026 closes. Ratings follow the target price mechanically
(Buy ≥ +20%, Sell ≤ −10%, otherwise Hold). This is AI-assisted research for information only, not investment advice.
