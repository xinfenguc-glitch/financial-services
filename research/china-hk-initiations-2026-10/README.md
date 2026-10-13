# China & HK: 17 Initiations (12 Oct 2026)

Initiation notes (five pages each) for the 17 China/Hong Kong stocks in the source pack
*"17 China/HK Stocks: Business Model, Performance and Outlook"* (6 Oct 2026). Each note has:

1. A summary page: rating, target price, thesis, catalysts, risks, key data and key financials (FY23A–FY28E).
2. At least two pages on **company background** (history, milestones, ownership), **the business** (how it makes
   money, segment economics), **competitive landscape** (competitors, five forces, moat) and **addressable market
   (TAM)**.
3. A **financial analysis** of all three statements: income statement (revenue, profit and FCF charts), balance sheet
   (FY23A–Jun-26A), cash flow (FY23A–FY28E, with a simple OCF/FCF/net-cash roll-forward) and key ratios (margins,
   ROE/ROA, working-capital days, liquidity, leverage, capex intensity, payout).
4. **Valuation**: peer multiples, target price method, bear/bull range.

- `China_HK_17_Short_Initiations_2026-10-12.pdf`: the report (89 pages, US Letter)
- `report.html`: the same content as a single HTML page
- `src/`: inputs and text, build script and PDF printer
  - `co_*.py`: market data, estimates, page-1 text and valuation per company
  - `v2_*.py`: long-form background, business, competition and TAM text plus financial commentary;
    `v2_forces.py` (five forces) and `v2_extra.py` (strategy and sizing paragraphs)
  - `fin_data.py`: balance-sheet and cash-flow history (FY23–FY25, Jun-26/TTM); `fin_model.py`: ratios and
    FY26–28E cash-flow/balance-sheet roll-forward
  - `build.py`: assembles `../report.html`; `print_pdf.mjs`: renders the PDF

Rebuild:

```bash
cd src
python3 build.py        # writes ../report.html and prints each rating/TP
node print_pdf.mjs      # writes ../China_HK_17_Short_Initiations_2026-10-12.pdf (Playwright + Chromium)
```

Prices are 12-Oct-2026 closes. Ratings follow the target price mechanically
(Buy ≥ +20%, Sell ≤ −10%, otherwise Hold). This is AI-assisted research for information only, not investment advice.
