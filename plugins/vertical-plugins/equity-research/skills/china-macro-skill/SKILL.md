---
name: china-macro-skill
description: Pull official Chinese macroeconomic data straight from the National Bureau of Statistics (NBS) - CPI, PPI, official PMIs, industrial output, retail sales, fixed-asset and property investment, urban unemployment, M2 and real GDP, plus any other national NBS series (trade, output by product, energy, services, fiscal) found by keyword. Use whenever the user asks about China's economy or needs Chinese macro numbers - "what did China's CPI print", PMI trends, GDP growth, a macro backdrop or "China macro" section for an A-share, H-share or China ADR note, a morning note, sector overview or thesis - even if they never mention NBS. Prefer this over web search or memory for these figures, which change monthly.
---

# China Macro (NBS)

Official figures come from `scripts/nbs_macro.py`, which reads the National Bureau
of Statistics' database directly. Use it instead of recalling numbers: Chinese
macro data is revised and released monthly, so anything from memory is likely
out of date, and web articles often round or mislabel the period.

The script needs Python 3 and network access to `data.stats.gov.cn`; it has no
other dependencies. Run it from this skill's directory.

## Quick start

```bash
python3 scripts/nbs_macro.py latest                      # snapshot: latest + previous value of every curated series
python3 scripts/nbs_macro.py latest cpi_yoy ppi_yoy      # just some series
python3 scripts/nbs_macro.py get cpi_yoy pmi_manufacturing --start 2024-01
python3 scripts/nbs_macro.py get gdp_yoy --start 2019Q1 --format json
python3 scripts/nbs_macro.py list                        # curated series names
```

Output is CSV on stdout (`--format json` for `get` and `fetch`). Periods are
written `2026-08` (monthly), `2026Q2` (quarterly) or `2025` (annual). `get`
defaults to the last five years.

| Series | What it is |
|---|---|
| `cpi_yoy` | CPI, % change on a year earlier |
| `ppi_yoy` | Producer (ex-factory) prices, % change on a year earlier |
| `pmi_manufacturing` | Official NBS manufacturing PMI; 50 separates expansion from contraction |
| `pmi_non_manufacturing` | Official non-manufacturing business activity index; same 50 line |
| `industrial_output_yoy` | Value added of industry above designated size, % change on a year earlier |
| `retail_sales_yoy` | Retail sales of consumer goods, % change on a year earlier |
| `fixed_asset_investment_ytd_yoy` | Fixed-asset investment (ex rural households), year to date, % change |
| `property_investment_ytd_yoy` | Property development investment, year to date, % change |
| `unemployment_rate` | Surveyed urban unemployment rate, % |
| `m2_yoy` | M2 money supply, % change on a year earlier |
| `gdp_yoy` | Real GDP, % change on a year earlier (quarterly) |

## Other series

NBS publishes thousands of national series. When the question needs one that
isn't curated (exports, power generation, industrial profits, output of a product,
services production, fiscal revenue), find it and fetch it:

```bash
python3 scripts/nbs_macro.py search 发电量 --freq M          # keyword search, in Chinese
python3 scripts/nbs_macro.py browse                          # top monthly categories
python3 scripts/nbs_macro.py browse --node <node id>         # drill down; a leaf lists its indicators
python3 scripts/nbs_macro.py fetch --catalog <id> --indicator <id> --freq M --start 2024-01
```

Search matches keywords loosely and ranks poorly: "进出口" returns industrial
export deliveries before customs trade. Read the names in the results, try a more
specific term, and fall back to `browse` when search doesn't surface the obvious
series. For example, monthly customs trade is under 对外经济 → 货物进出口总额.

Picking the right indicator:
- **当期值 / 累计值**: this period's value vs the cumulative year-to-date total.
  **同比增长 / 累计增长**: growth on a year earlier for the period vs year to date.
- **Units**: 亿元 = 100 million yuan; 千美元 = thousand US dollars.
- **Split catalogs**: names ending in a year range, such as "(2021-2025)" or "(2026-)",
  hold one base period each. Fetch the catalog that covers the dates you need.
- `fetch` returns values exactly as published. An index labelled
  "(上年同月=100)" is not converted: 100.8 means up 0.8% on a year earlier.
  (The curated `cpi_yoy`, `ppi_yoy` and `gdp_yoy` are already converted.)
- `fetch` doesn't check freshness unless you pass `--max-age-days`, so look at
  the last period it returns before calling a figure current.

Keep requests modest. The site's pages turn away automated browsers, and the API
is undocumented. A handful of series per answer is fine; don't sweep hundreds of
indicators.

## Reporting the numbers

- **Name the period every figure refers to.** Write "CPI rose 0.8% on a year
  earlier in August 2026", not "CPI is 0.8%". Data lags: August activity data
  comes out in mid-September, and GDP about three weeks after the quarter ends.
- **Credit the source** wherever the numbers appear, in a table, chart or text:
  "Source: National Bureau of Statistics of China (来源：国家统计局)".
- **Year-to-date series are cumulative.** `fixed_asset_investment_ytd_yoy` for
  August is growth over January to August, not August alone.
- **January and February are often missing.** NBS publishes most activity data
  for the two months as one figure in March, so `industrial_output_yoy` and
  `retail_sales_yoy` have no rows for either month. Say so rather than filling
  the gap, and don't estimate missing months.
- **M2 lags.** It is central bank data that NBS republishes, often a month after
  the People's Bank of China. Check the period before comparing it with other
  series.
- **Reuse terms.** NBS keeps the copyright and allows reuse as free news or
  reference information with the credit above. If the user is building something
  sold or client-facing, mention once that they should confirm the terms with
  NBS; don't lecture.

## When the script fails

Failures go to stderr as `UNAVAILABLE <series>: ...` or `STALE <series>: ...`,
and the exit status is 1. Other series in the same command still print.

- **UNAVAILABLE, couldn't reach NBS.** The script has already retried three
  times, because connections from outside China are sometimes reset. If it
  keeps failing, the environment probably can't reach `data.stats.gov.cn`; tell
  the user. NBS's press releases at https://www.stats.gov.cn/sj/zxfb/ are a
  fallback if you can browse; say that's where the figure came from. Don't
  present remembered numbers as current.
- **UNAVAILABLE, "came back as ...".** NBS reorganised its database and a
  curated ID now points elsewhere. Use `search` / `fetch` to get the series for
  this answer, tell the user the curated entry needs fixing, and see
  `references/nbs-api.md` for how.
- **STALE.** NBS hasn't published a new figure for longer than expected (95
  days monthly, 125 quarterly). Rerun with a larger `--max-age-days` to see the
  latest available value, and report it with its date and the delay. For CPI
  after 2030, the likely cause is NBS's five-yearly rebasing into a new catalog,
  which has to be added to the script.

## Reference

`references/nbs-api.md` documents the NBS endpoints, request format and period
codes, and how to add or repair a curated series. Read it only when the script
itself needs changing.
