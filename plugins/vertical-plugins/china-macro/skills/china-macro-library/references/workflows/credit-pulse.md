# Workflow: China Credit Pulse

**Question answered**: Where is China's credit cycle, who is still borrowing, and is new credit gaining or losing traction?
**Frameworks**: wright-deleveraging ch02 (interest on credit vs GDP), ch04 (bank assets vs TSF, the five financial effects), ch05 (credit reallocation), ch06 (TSF revisions); patterns.md "Credit Measurement Triangulation".

## Step 1: Gather data
Use the most recent 24–36 months. Ask the user for data or pull it from a connected source, and note the release date of each series.

| Series | Source | Why |
|---|---|---|
| TSF stock growth and flow by component (RMB loans, trust loans, entrusted loans, undiscounted acceptances, corporate bonds, government bonds, equity) | PBOC | Headline credit. Strip out government bonds to see private credit. |
| Balance sheet of other depository corporations: total assets; claims on government, NBFIs and other banks | PBOC | Bank-asset credit gauge and shadow-channel proxy |
| RMB loans by sector: household short- and medium/long-term, corporate short- and medium/long-term, bills | PBOC | Who is borrowing |
| M1, M2 | PBOC | Liquidity and activity signal |
| Nominal GDP growth | NBS | Credit vs GDP |
| LPR, 7-day reverse-repo rate, DR007, 10y CGB yield | PBOC / CFETS | Price of credit |
| Local-government bond issuance (general, special, refinancing) | MoF | Fiscal share of credit |

If a series is unavailable, say so and continue with what exists.

## Step 2: Triangulate growth
1. TSF y/y, both headline and **ex-government bonds**. Remember that government bonds were added to TSF in December 2019, so headline TSF overstates private credit.
2. Bank-asset y/y.
3. If the two diverge by more than 2pp, explain it (shadow swings, government-bond share, base effects).
4. Credit growth minus nominal GDP growth. Wright's benchmark is **only marginally positive**: a large positive gap adds leverage, a negative gap means deleveraging.

## Step 3: Traction test
- Estimate annual interest on credit as average lending rate × credit stock, and compare it with the annual nominal GDP increment. If interest is larger, new credit is mostly servicing old debt (true every year from 2012 per Wright).
- Credit impulse: the change in new credit as a share of GDP over 12 months.

## Step 4: Composition (who can still borrow)
| Borrower | Signal to read | Wright baseline |
|---|---|---|
| Households | Medium/long-term loans (mortgage proxy) | RMB 6–8 trillion a year in 2018–21; property share of loans 33% (2018) |
| Corporates | Medium/long-term vs short-term and bills | Bills and short-term loans substituting for long-term = weak demand or window dressing |
| SOEs vs private | Net bond issuance by ownership | Private net issuance negative after 2018 |
| Government | Bond share of TSF flow | Rising share = fiscalization of credit |
| Shadow | Trust, entrusted loans, acceptances | Contracted outright 2017–18 |
| Regions | Provincial TSF/loan growth | NE and West ~4% vs coastal SE ~13% after 2018 |

## Step 5: Interpret
Classify the regime:
- **Re-leveraging** (credit growth ≫ nominal GDP, shadow channels growing): Wright's "abandon deleveraging" path.
- **Fiscalized credit** (government bonds carry the TSF growth, private credit weak): the "save localities" path.
- **Balance-sheet stall** (credit growth ≈ GDP, household and private demand weak, rates falling): the base case Wright projects.
- **Deleveraging squeeze** (credit < GDP, defaults rising): a "double down" path.

## Output template
```
CHINA CREDIT PULSE — [month/year of latest data]
Regime: [one of the four] | Confidence: [H/M/L]
Headline: TSF [x]% (ex-govt [y]%) | Bank assets [z]% | Nominal GDP [g]% | Gap [±]
Traction: interest on credit ≈ RMB [a] trillion vs ΔGDP RMB [b] trillion → [gaining/losing]
Who's borrowing: [households / corporates / government / shadow, with one line each]
Versus Wright baselines: [2–3 comparisons with vintages]
Watch next: [3 items, e.g. LGFV issuance, household medium/long-term loans, M1]
Sources and vintages: [list]
```
