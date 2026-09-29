# Public sources for defence analysis

Check the latest release date of each source and state it in the output. All of these
revise past years, so quote the edition you used.

## Spending

| Source | What it gives | Watch out for |
|---|---|---|
| **SIPRI Military Expenditure Database** | Spending for most countries back to 1949: local currency, constant and current USD, share of GDP, per capita, share of government spending. Updated each spring. | SIPRI uses its own definition, so totals differ from national budgets. Figures for countries with opaque budgets are SIPRI estimates. **Licence:** free use requires both a non-commercial purpose and reproducing under 10% of the dataset; commercial use (including research sold or used for fees) needs a SIPRI licence. |
| **NATO, *Defence Expenditure of NATO Countries*** | Member spending in national currency and USD, share of GDP, real change, and split into equipment, personnel, infrastructure and other. Published annually. | NATO's definition (which includes pensions and some non-MoD forces) can differ considerably from national budgets. The latest years are estimates. Equipment share covers major equipment and related R&D. |
| **National budget documents** | Appropriations by line: US DoD Comptroller procurement (P-1) and RDT&E (R-1) exhibits, Japan MoD budget, UK MoD, Germany's defence budget and special fund, India's Union Budget defence grants. | The best detail, but in national formats and fiscal years. Requests are not appropriations, and appropriations are not outlays. |

## Orders, contracts and exports

| Source | What it gives | Watch out for |
|---|---|---|
| **US DoD daily contract announcements** (defense.gov) | Large US contract awards, with value, contractor and programme. | Face values often include options and ceilings; funding is obligated over time. |
| **USAspending.gov / SAM.gov** | US federal award and obligation data, searchable, with an API. | Obligations, not revenue. Reporting lags. |
| **DSCA major arms sales notifications** | Proposed US Foreign Military Sales notified to Congress. | Notifications are ceilings for possible sales; many are signed later, smaller, or never. |
| **EU TED, UK Find a Tender, national procurement agencies** (e.g. Japan ATLA contract data) | Tenders and award notices in Europe and Asia. | Coverage of defence awards is partial; sensitive contracts are often exempt. |
| **SIPRI Arms Transfers Database** | Deliveries of major conventional weapons between states. | Measured in trend-indicator values (TIV), a volume index, **not money**. Use it for shares and trends, not sales figures. Same licence terms as the SIPRI spending data. |
| **Company disclosures** | Backlog and RPO notes, order announcements, segment data, capacity plans. | Backlog definitions vary (see `kpis.md`). |

## Industry and inventories

| Source | What it gives | Watch out for |
|---|---|---|
| **SIPRI Arms Industry Database (Top 100)** | Arms revenue of the largest companies. | Lags by about a year; arms revenue is SIPRI's estimate where companies don't disclose. |
| **IISS *Military Balance*** (paid) | Equipment inventories and orders by country. | Needed for bottom-up replacement-demand sizing. Licensed; cite, don't reproduce. |
| **Broker and vendor research** (paid) | Forecasts, pipelines, channel checks. | Licensed to the subscriber. Paraphrase and cite; never redistribute. |

## Comparing figures

- **Fiscal years differ.** The US runs October to September; Japan, India and the UK run April to March. Say which year convention a figure uses.
- **Nominal vs real, local vs USD.** Currency moves can swamp real changes in USD comparisons. Use constant prices for trends.
- **Core vs related spending.** Alliance targets may count infrastructure, resilience or pensions that national "defence budgets" exclude. Compare like with like.
- **Estimates get revised.** The latest year in most datasets is an estimate. Prefer settled years for trend claims and flag estimates.
