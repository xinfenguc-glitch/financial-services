---
name: model-update
description: Update financial models with new data — quarterly earnings, management guidance, consensus moves, filings, KPI releases, capital-structure changes, or revised assumptions. Maps every data point to a treatment before writing, keeps the original intact, adjusts estimates, recalculates valuation, and flags material changes. Use after earnings, guidance updates, or when assumptions need refreshing. Triggers on "update model", "plug earnings", "refresh estimates", "update numbers for [company]", "new guidance", "roll it forward", or "revise estimates".
---

# Model Update

Sourcing, evidence labels, freshness, market-data arithmetic and the readiness posture follow the `research-conventions` skill. Load it before the first write.

Updating is not building. You know what changed in the world, but not what the workbook will do when you write into it. So the order below works like this:

- It maps every data point to a treatment before a single cell moves.
- It keeps the original model intact.
- It leaves a reader able to see what changed, and on whose authority.

**Before you start:**

- If the workbook's own checks fail, or the model looks wrong before you touch it, audit it first with `audit-xls`.
- If the change does not fit the model's shape, see *When to rebuild instead* at the end.

**How you are running decides how you write:**

| Running | Writes go to | Original protected by |
|---|---|---|
| Live workbook (Excel tools available) | the user's open workbook, staged for their review | confirming a saved version exists before the first write |
| File on disk (headless; see `xlsx-author`) | a versioned copy | never opening the original for writing |
| Read-only worker (no write tool) | nowhere: return the mapping and variance tables | not writing at all; the writer applies the mapping |

## Workflow

### Step 1: Identify What Changed

An update has one trigger. Name it, get hold of the document or connector data that carries it, and write down the fields it reaches before you open the workbook.

| Trigger | Arrives as | Touches |
|---|---|---|
| Earnings release | a reported quarter or year | historical actuals, the LTM roll, and the forward periods the print reprices |
| Guidance change | a range, a raise, a cut, a withdrawal | the driver rows for the guided periods, and the basis note beside them |
| Estimate revision | our own changed assumption, with its reason | the driver rows it moves, labelled `judgement` or `assumption` |
| Consensus move | a revised mean estimate with its vintage | the comparison column, never the model's own drivers |
| Transcript disclosure | a number said on a call | the operating metrics it re-anchors, and any driver built on them |
| Filing | 10-K, 10-Q, 8-K, proxy | restatements, segment re-cuts, share count, the debt schedule, contingencies |
| KPI release | a monthly or quarterly operating metric | the sector KPI rows, and the revenue build above them |
| Capital structure change | a buyback, an issuance, a raise, a repayment | diluted share count, net debt, the equity bridge |
| Macro update | interest rates, FX, commodity prices | the spot anchors, the WACC inputs, the implied return |
| Event-driven | M&A, restructuring, a new product, a management change | usually a rebuild; see *When to rebuild instead* |

If one trigger is really two, such as a print that also restates a prior year, give each its own rows in Step 3 rather than blurring them into one update.

**Done when** the trigger is named, its source is in hand with an as-of date, and the list of fields it touches exists in writing.

### Step 2: Protect the Original

- **File on disk:** record a hash of the original (`shasum -a 256`), then copy it to `<name>_v<N>_<date>.xlsx` and work only on the copy. When headless, the copy goes in `./out/`, per `xlsx-author`'s output contract. Increment the version rather than overwriting a previous update, so a reader can diff two versions of the same model.
- **Live workbook:** before the first write, confirm the user has a saved version to reconcile against.

**Done when** there is a version to reconcile against, and for a file, the original's hash still matches the one taken before any edit.

### Step 3: Map Every Data Point Before Writing

Read the workbook twice: once for formulas and once for cached values (for a file, open it again with `data_only=True`). Then build the mapping table. The table is the reviewable output of this skill, and it is presented before any edit.

| Data point | New value | As-of | Source | Target sheet!cell | What is there now | Treatment |
|---|---|---|---|---|---|---|

`What is there now` is one of: declared input, formula, or absent. Read it from the workbook; do not assume it. `Treatment` comes from this closed set:

| Treatment | Holds when | What happens |
|---|---|---|
| `safe to write` | the target is a declared input cell (blue), and the new value is the same quantity on the same basis | write it, and log the write |
| `reference only` | the target holds a formula, or writing would cut a link the model depends on | record the figure beside the model, and leave the cell computing |
| `no place in the model` | the model has no line for the item | record it in the unwritten block of the change log, and raise it on delivery |
| `needs an assumption` | the cell needs something the source does not supply: an allocation, a split, a period conversion | write the chosen value into the declared input cell, label it `assumption`, and log it as an assumption |
| `requires rebuild` | the change is structural: a segment re-cut, an accounting-basis change, a driver the model does not have | write nothing, and route it per *When to rebuild instead* |

Two rules come with the table:

- **A restatement keeps both figures.** When the company restates a prior period, the row records both the original and the restated value. The model shows the restated one, so the estimate history stays readable instead of being quietly rewritten.
- **Market-sensitive inputs always carry an as-of.** Price, diluted share count, net debt, consensus, FX and rates each record the date they were captured, both in the mapping row and in the cell's source comment.

**Checkpoint.**

- *Interactive:* present the mapping table and wait for the user's go-ahead before writing.
- *Headless:* nobody is there to approve, so write only to the versioned copy, and put the mapping table first in the delivery.
- *Read-only worker:* skip the writes in Step 4, but still build its variance table, and work Steps 5 and 6 from the mapping. Return the mapping table, the variance table, and the estimate and valuation changes to the writer. Recalculation and the audit in Step 7 fall to the writer.

**Done when** every data point from Step 1 has a row, every row carries exactly one treatment, and the checkpoint above has been met.

### Step 4: Plug New Data

Write only the rows tagged `safe to write` and `needs an assumption`, and only into declared input cells. An assumption row carries its basis in the cell's source comment, so the change log can tell a sourced write from a chosen one.

**After earnings**, the variance table:

| Line Item | Prior Estimate | Consensus (vintage) | Actual | Delta vs. prior | Delta vs. consensus | Notes |
|-----------|---------------|---------------------|--------|-----------------|---------------------|-------|
| Revenue | | | | | | |
| Gross Margin | | | | | | |
| Operating Expenses | | | | | | |
| EBITDA | | | | | | |
| EPS | | | | | | |
| [Key metric 1] | | | | | | |
| [Key metric 2] | | | | | | |

State margin deltas in basis points, and level deltas in percent or currency.

**Segment detail** (if applicable): update each segment's revenue and margin, and note any shifts in segment mix.

**Balance sheet and cash flow:**

- cash and debt balances
- share count (buybacks, dilution)
- capex: actual vs. estimate
- working capital changes

**Structural edits** need care. Adding a period column or a new line item is not a value write:

- In a live workbook, insert through Excel so that references move with the cells.
- In a file, openpyxl's row and column inserts do not update formulas, defined names, chart ranges or merged cells. Add into existing blank columns where the model has them; otherwise treat the edit as `requires rebuild`.

**Change log.** The workbook gains a `Change Log` sheet with one row per write:

```
date | sheet!cell | line item | old value | new value | source | as-of | treatment | note
```

Below the written rows, the same sheet carries the unwritten block: every mapping row tagged `reference only`, `no place in the model` or `requires rebuild`, with the reason. A reader who opens only this sheet learns what moved, what did not, and why. Each written input gets a new source comment naming its source and as-of, replacing the old one.

**Done when** every written row has a `Change Log` row saying whether it was sourced or assumed, every logged cell holds its new value, and the unwritten block accounts for every mapping row that was not written.

### Step 5: Revise Forward Estimates

**Reconcile reported to adjusted first.** Reported figures and the basis the model runs on are different metrics. Say which basis the model uses (GAAP or adjusted), and bridge them, one line per adjustment:

```
Reported operating income | + stock compensation | + restructuring | + acquisition amortization | = adjusted operating income
```

When the company changes its own definition of the adjusted measure, that change is a finding. Name it, show both definitions for the affected period, and treat the periods on either side as not comparable until the bridge is restated.

**Estimate changes:**

| | Old FY Est | New FY Est | Change | Old Next FY | New Next FY | Change |
|---|-----------|-----------|--------|------------|------------|--------|
| Revenue | | | | | | |
| EBITDA | | | | | | |
| EPS | | | | | | |

**Show the walk, not just the new numbers.** Each step is one driver, and the steps add up to the new estimate:

```
Prior FY EPS | volume | price/mix | gross margin | operating expense | share count | tax | = new FY EPS
```

**Key assumption changes:** what you are changing and why. For example, revenue growth rate: old → new (reason); margin assumption: old → new (reason). Also list any new items, such as restructuring charges or one-time gains.

Then compare the revised estimates against consensus, stating the consensus vintage.

**Done when** each bridge's closing figure equals the model's new estimate cell for every period shown, and every adjustment line and driver step names its source or its reason.

### Step 6: Valuation Impact

| Valuation Method | Prior | Updated | Change |
|-----------------|-------|---------|--------|
| DCF fair value | | | |
| P/E (NTM EPS × target multiple) | | | |
| EV/EBITDA (NTM EBITDA × target multiple) | | | |
| **Price Target** | | | |
| Spot price (as of) | | | |
| Implied return | | | |

A new price target on its own tells the reader nothing about what moved it. Break the change down into four parts that add up to the total change:

- estimate revision
- discount rate or multiple change
- capital structure
- rolling forward one period

**Done when** the parts add up to the change in fair value, and the spot price and the implied return carry the same as-of.

### Step 7: Recalculate and Audit

- **Recalculate.** In a live workbook, Excel recalculates as you write. A file written with openpyxl keeps the old cached values until a spreadsheet engine (Excel, or LibreOffice where installed) recalculates it. If nothing in the environment can recalculate it, say so plainly in delivery: the displayed values are stale cached values.
- **Audit.** Run `audit-xls`: balance checks, no broken links, no hardcodes in calculation cells.
- **Checks.** Read the workbook's checks tab, if it has one, from recalculated values only. A cached value can show a passing check on a broken model.

**Done when** the workbook is recalculated (or its staleness is disclosed), `audit-xls` reports no failures, and any checks roll-up reads OK.

### Step 8: Summary & Action

**Estimate change summary:** one paragraph on what changed, why, and what it means for the stock. Is this a thesis-changing event or noise?

**Rating / price target:**

- Maintain or change the rating, on the user's or the firm's rating scale.
- A new price target, if any, with its methodology.
- Upside or downside to the current price, with its as-of.

The call that goes with the rating comes from the input-gated list in the `research-conventions` judgement rules.

**Output:**

- the updated Excel model, with its `Change Log` sheet (when the user provided a model, and this run can write);
- the mapping table and the variance table;
- the estimate change summary (markdown or Word);
- the price target derivation and the valuation breakdown from Step 6.

The delivery message carries three things:

- **The readiness posture.** Read it against the state the update leaves the model in, naming the row responsible. An assumption row means a load-bearing input rests on a chosen number. A `requires rebuild` row means the model cannot represent the change at all.
- **What was not written**, row by row, and what each row would take.
- **The monitoring items** the update creates.

**Done when** the posture is stated with the row responsible for it, and every unwritten mapping row appears in the message.

## When the Model Cannot Be Edited Safely

Some workbooks cannot take a write without breaking. The signs:

- the target cells hold formulas rather than inputs;
- the file drives external links or macros;
- it carries pivot caches or objects that openpyxl drops on save;
- it is the user's system of record, and they have not asked for it to be changed.

In that case, deliver a control pack instead: the original untouched, plus a companion workbook whose sheets say what they hold (`New Data`, `Bridge`, `Implied Impact`, `Change Log`). The pack must stand alone, because a cross-workbook link cannot be resolved. Values taken from the original are typed in, with a comment naming the sheet and cell they came from. Everything computed inside the pack is a live formula, following the `xlsx-author` color and formula conventions.

**Done when** the original is unchanged (for a file, its hash still matches), and every sheet in the pack names the cells of the original it corresponds to.

## When to Rebuild Instead

An update assumes the model's shape still fits the company. These changes break that assumption, and updating through them produces a model that ties out but misstates the company:

- the company re-cut its segments, or changed what a segment contains;
- the accounting basis changed: a new standard, a revenue-recognition change, a change of reporting currency;
- a merger, divestiture or spin changed the entity the model describes;
- the driver the update needs does not exist in the model at all.

Say so rather than forcing the write, and route it: `3-statement-model` for the operating model, `dcf-model` for the valuation. When running as the earnings-reviewer agent, raise it as a handoff to model-builder. The mapping table carries into the rebuild, because it already says what the new shape has to hold.

## Important Notes

- Always reconcile your estimates to the company's reported figures before projecting forward.
- Note any non-recurring items, and whether your estimates are GAAP or adjusted.
- Track your estimate revision history. It shows your analytical progression, and the versioned copies and the `Change Log` are that history.
- If the quarter was noisy, separate signal from noise in your estimate changes.
- Check consensus after updating: how do your revised estimates compare to the Street?
- Share count matters. Dilution from stock comp or converts, or buybacks, can materially affect EPS.
