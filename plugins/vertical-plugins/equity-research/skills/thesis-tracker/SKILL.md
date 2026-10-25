---
name: thesis-tracker
description: Maintain and update investment theses for portfolio positions and watchlist names. Tracks pillar status, an append-only evidence ledger, monitoring triggers, and thesis drift, with separate verdicts on the business and on the stock. Use when updating a thesis with new information, reviewing position rationale, or checking if a thesis is still intact. Triggers on "update thesis for [company]", "is my thesis still intact", "thesis check", "add data point to [company]", "post-earnings thesis check", "re-underwrite", or "review my positions".
---

# Thesis Tracker

Sourcing, evidence labels, freshness, market-data arithmetic and the readiness posture follow the `research-conventions` skill. Load it before the first deliverable.

Every update gives two verdicts, because they can move apart:

- The **company thesis** says whether the business is doing what we underwrote.
- The **security call** says whether the stock is a decision we can act on today.

A business can improve while the stock gets worse, because expectations rerate faster than evidence arrives. A weakening business does not justify a trim when we have no price, no valuation frame and no position context. A single status column hides both cases.

The tracker is **append-only**. Prior pillars, thresholds and ledger rows stay as written. A row that no longer holds is marked `superseded` or `stale` with its date, or is contradicted by a named later row, and its replacement is a new row. Drift only shows against a history nobody edited, and catching drift is what the tracker is for.

## Workflow

### Step 1: Define or Load Thesis

The mode comes from what the user supplies. Each mode's default runs without asking.

| Supplied | Mode | Default behavior |
|---|---|---|
| Nothing | blank shell | Produce the empty structure, list the minimum inputs, populate nothing |
| A ticker only | frame | Draft candidate pillars from filings and consensus. Each carries the evidence label its support earns, and `draft` provenance until the user confirms it |
| An existing thesis | load | Parse it into pillar records, and mark each field the source did not carry as missing |
| A thesis plus a development | update | Run the remaining steps on the change only |
| A print, transcript or filing | post-earnings | An update, with the evidence-quality parse in Step 2 done first |
| Several positions | portfolio review | For each name: aggregate status and security call. Then four groups: priority actions; names deteriorating; names where evidence improved but risk/reward worsened; catalysts inside the horizon |
| A long and a short as a pair | paired | One tracker per leg, plus what breaks the pair (as opposed to either leg) |

A new thesis records:

- **Company**: name and ticker.
- **Position**: long or short.
- **Thesis statement**: the one- or two-sentence core thesis. For example: "Long ACME — margin expansion from pricing power + operating leverage as mix shifts to software."
- **Pillars**: three to five, each a claim that evidence could kill. A claim nothing could disconfirm is a preference, not a pillar.
- **Key risks**: three to five risks that would invalidate the thesis, each tied to the pillar it attacks.
- **Valuation anchor**: what the stock is worth if the thesis plays out, with method and horizon.
- **Exit trigger**: the break threshold the thesis was written with.

Every pillar carries these fields:

| Field | Carries |
|---|---|
| Claim | one falsifiable sentence |
| Priority | `core` or `supporting`; core pillars drive the reconciliation rule in Step 3 |
| Baseline | the figure at underwriting, with its as-of |
| Expected path | what the metric does, and by when |
| Confirm / warning / break thresholds | three levels, each with a provenance label; the break level is the exit trigger |
| Latest evidence | the ledger row id and date from Step 2 |
| Signal | the current direction, on the Step 2 scale |
| Evidence quality | the label from the `research-conventions` evidence rules |
| Provenance | `inherited`, `draft` or `approved`, per the note below |
| Model line | the line item this pillar drives, so a break has somewhere to land |
| Implied action | what a break implies, from the call list in Step 2 |
| Next proof point | the dated release or event that tests it |
| Owner | who does the work |

**Provenance** records approval, not evidence. Every pillar, threshold and action trigger carries one of three labels:

- `inherited`: written in the original underwriting.
- `draft`: our proposal, awaiting confirmation.
- `approved`: an agreed monitoring rule.

A pillar or level we introduce stays `draft` until the user confirms it, so an exit price we chose reads as a proposal rather than a rule. A pillar drawn from a filing is `fact` on the evidence labels and still `draft` until someone signs off on it.

**Blank shell.** With no thesis supplied, deliver the empty structure and ask for the minimum inputs:

- ticker
- direction
- horizon
- the two or three claims the position rests on
- any thresholds the user already runs

Fill nothing from memory, and say plainly which fields are still waiting.

**Done when** the mode is named, every pillar carries all thirteen fields or names each missing one, every pillar and threshold has a provenance label, and no field holds a figure without a source.

### Step 2: Update Log

The update log is an evidence ledger: one row per data point, appended and never rewritten.

| Field | Carries |
|---|---|
| Id and date | a stable row id, and the date the fact arrived |
| Reporting period | the fiscal period the fact belongs to, labelled per the `research-conventions` market-data rules |
| Source and type | the document or connector, and its evidence label |
| Fact | what was reported, in figures |
| Our prior expectation | what we had modelled |
| Market expectation | consensus or the visible bogey, with its vintage |
| Interpretation | what it means for the claim, in one sentence |
| Pillar | which pillar it lands on |
| Signal and magnitude | from the scale below |
| Evidence quality | per the evidence labels |
| Impact | on the model, the valuation and our confidence, plus the action taken |
| Follow-up and owner | the next piece of work, and who holds it |

**Signal scale.** The values are strongly confirming, confirming, mildly confirming, neutral, mildly weakening, weakening and strongly weakening, plus `mixed`, `invalidating` and `untested`. The scale is a discipline, not arithmetic. Read the spread of signals across a pillar and state its direction in words. Summing them into a composite score invents precision the evidence does not have.

**Evidence-quality parse.** A headline beat becomes evidence only once it is broken down. Check each of these:

- volume against price against mix
- cost actions
- tax rate
- share count and buyback
- currency
- one-time items
- the quality of KPI definitions
- the shape of guidance
- revisions beyond the next quarter
- cash conversion

Name which component carried the beat and whether it recurs. A beat that came from tax and share count leaves every operating pillar `untested`.

**Management credibility.** Commentary earns weight when it is quantified, consistent with what was said last quarter, specific about the mechanism, and candid about what went wrong. Vague optimism, a changed KPI definition and selective disclosure earn none. Say which of the two you are looking at.

**Accounting red flags.** Each of these lowers evidence quality on the pillar it touches, and opens a dated follow-up:

- a KPI definition or disclosure change
- non-GAAP adjustments growing as a share of earnings
- a revenue-recognition change
- receivables or inventory building faster than sales
- cash conversion falling away from reported earnings
- a spike in capitalized costs
- a segment restatement
- an auditor or CFO departure
- related-party transactions
- "one-time" charges that recur

**Action.** The call comes from the input-gated list in the `research-conventions` judgement rules (no change → hold; increase; trim; exit; hedge; watchlist; wait for proof; re-underwrite), and each call needs its inputs in hand. On a short leg, exit reads as cover. The tracker also has two workflow outcomes, which sit beside the call rather than replacing it:

- `update model`, when the change lands in a line item.
- `escalate`, when a threshold in Step 7 fires.

**Updated conviction**: High, Medium or Low, with the sentence that justifies it.

**Done when** every new data point is one ledger row naming its pillar, its signal and its evidence quality, prior rows are unchanged, and every call has its inputs in hand.

### Step 3: Thesis Scorecard

Each pillar takes exactly one of eight statuses:

| Status | Means |
|---|---|
| `strengthening` | evidence beat the expected path, and the path ahead is unchanged or better |
| `intact` | evidence is consistent with the expected path |
| `watch` | a warning threshold was touched, or the evidence is mixed; the next proof point decides it |
| `impaired` | a break threshold was crossed here, while the thesis still stands on the other pillars |
| `broken` | the claim failed, and the reason to own the stock is gone |
| `changed` | the business is doing something other than what we underwrote, so the old claim no longer applies |
| `untested` | no evidence has reached this pillar since underwriting |
| `retired` | deliberately closed, with the date and the reason |

**Reconciliation.** The aggregate status follows the core pillars:

- One core pillar at `impaired` with an aggregate better than `watch` requires an evidenced override: one sentence naming what offsets it and the evidence behind the offset.
- Two or more core pillars at `impaired` set the aggregate to `impaired`.
- A core pillar at `broken` or `changed` sets the aggregate to the same.

This rule is what stops drift. Without it, the aggregate sits at `intact` for a year while the pillars underneath it rot.

The scorecard shows one row per pillar:

| Pillar | Priority | Expected path | Latest evidence | Signal | Status |
|--------|----------|---------------|-----------------|--------|--------|
| Revenue growth >20% | core | >20% y/y through FY | Q3 was 22% (10-Q) | confirming | intact |
| Margin expansion | core | +200bp over two years | margins flat y/y (10-Q) | weakening | watch |
| New product launch | supporting | launch in Q1 | delayed to Q2 (company claim) | mildly weakening | watch |

**Scoring honesty.** Weighted pillar scores and conviction charts appear only when the user's own method defines the weights. Otherwise the aggregate is one of the eight statuses, plus the sentence that justifies it.

**Done when** every pillar carries one of the eight statuses, the aggregate is reconciled or its override sentence is written, and no numeric score appears that the user did not define.

### Step 4: Security Call

| Call | Holds when |
|---|---|
| `callable` | the call and every input it needs are in hand |
| `conditional` | callable once one named input arrives; name it, and the date it arrives |
| `re-underwrite` | the thesis changed, so the call goes back through initiation rather than through a trim |
| `inputs missing` | an input the call needs is missing |

These four values are the status of one object, the security call. They are not a readiness scale: the artifact still carries one readiness posture, read against its inputs.

**The gate.** The security call needs three inputs: a current price, a valuation frame, and the position context (size, cost basis, benchmark weight). Without all three it is `inputs missing`, and it says which is missing. A weakening company thesis then becomes a `re-underwrite` or a monitoring item, and a valuation-led action waits for the valuation input.

**Price action is a signal to break down.** Before a price move enters the update as evidence, split it across these drivers:

- fundamentals
- estimate revisions
- multiple change
- factor and sector beta
- positioning and crowding
- liquidity and flows
- options and hedging
- macro

Attribute what the data supports, and say what stays unattributed. A move nobody can attribute is a question, not a confirmation. Price remains a statement of what the market believes, not what is true.

**Done when** the security call carries one of the four values, any value other than `callable` names the missing input and what would supply it, and every price move cited in the update carries its breakdown.

### Step 5: Catalysts and Monitoring

Every next proof point is a monitored item:

| Metric | Threshold | Source | Window | Confirming signal | Disconfirming signal | Action if crossed | Action if not | Provenance |
|---|---|---|---|---|---|---|---|---|

The KPI tracker has one row per tracked metric, with every comparison basis present:

| KPI | This period | Prior period | Our estimate | Guidance | Consensus | Threshold | Peers |
|---|---|---|---|---|---|---|---|

A comparison you cannot get is marked `n/a`, with the reason in the cell. Dropping the column would hide that the KPI was never compared against the thing that would have moved the thesis.

For which KPIs each sector rewards tracking, and the warning sign that shows up first in each, see `references/sector-signals.md`. Read it when the name is outside a sector you have already framed pillars for.

Each dated catalyst carries its date type and date confidence in the `catalyst-calendar` terms. For more than a handful of dated events, or a calendar across positions, use `catalyst-calendar`.

**Done when** every monitored item names the action on each side of its threshold, and every KPI row shows all six comparison bases or marks each missing one with its reason.

### Step 6: Drift and Red Team

In every update, mark each drift pattern present or absent, by name:

1. **The reason changed.** Today's rationale is not the underwriting rationale, and no re-underwrite recorded the switch.
2. **Catalyst laundering.** A catalyst passed without the expected result and was replaced by qualitative rationale, rather than by a new dated proof point.
3. **Valuation substitution.** "It is cheap" quietly took over from the growth or margin pillar we actually underwrote.
4. **Dismissal by horizon.** Repeated disconfirming evidence is being set aside as long-term noise.
5. **Protection as reason.** Downside protection became the reason to hold a position taken for upside.

Then red-team the current view:

- the strongest opposing case, put the way someone who holds it would put it
- the evidence behind it
- what would make it right
- what would change our recommendation
- the open questions
- the next review date

Prompts that help in any sector:

- Is the debate about growth, margin, multiple, balance sheet, management credibility or regulation?
- Is the KPI we track a leading or a lagging indicator?
- Is the weakness cyclical, company-specific or structural?
- What does the current price already assume?

**Done when** each of the five patterns is marked present or absent, and the red team names a view someone actually holds, with the evidence that supports it.

### Step 7: Output

The artifact opens with the operating model, so the reader knows who acts and when:

| Slot | Value |
|---|---|
| PM decision owner | |
| Analyst owner | |
| Evidence and ledger owner | |
| KPI and model owner | |
| Review cadence | quarterly at minimum, and on every catalyst |
| Post-catalyst update deadline | the number of working days after an event within which the ledger and statuses are updated |
| Escalation triggers | a break threshold crossed; the aggregate at `impaired` or worse; or the security call at `inputs missing` for two consecutive cycles |
| Next review gate | the date, and the decision that gate makes |

The deliverable runs in this order:

1. **Header**: aggregate status, security call, conviction, readiness posture, as-of.
2. **Operating model.**
3. **Pillar scorecard.**
4. **KPI tracker.**
5. **Monitoring table.**
6. **Ledger rows added** since the last version.
7. **Drift and red team.**
8. **Next gate.**

Use concise markdown for a morning meeting, or a Word document for a portfolio review or risk committee pack.

Route the work the tracker uncovers rather than doing it here:

- dated events → `catalyst-calendar`
- a changed line item → `model-update`
- a `re-underwrite` call → `initiating-coverage`
- a print that needs a full breakdown → `earnings-analysis`

**Done when** both verdicts and the posture appear on the first screen of the artifact, the ledger section lists every row added since the previous version, and the next review gate carries a date.

## Important Notes

- A thesis should be falsifiable. If nothing could disprove it, it is not a thesis.
- Track disconfirming evidence as rigorously as confirming evidence.
- Review theses at least quarterly, even when nothing dramatic has happened.
- If the user manages multiple positions, offer a full portfolio review (the portfolio review mode in Step 1).
- Store thesis data in a structured format so it can be referenced across sessions. Because the tracker is append-only, each version extends the last rather than replacing it.
