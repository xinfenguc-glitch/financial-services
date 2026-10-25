---
name: earnings-preview
description: Build pre-earnings analysis with estimate models, scenario frameworks, and key metrics to watch. Use before a company reports quarterly earnings to locate the expectation bar, set up bull/bear scenarios, plan call questions, and identify what will move the stock. Triggers on "earnings preview", "what to watch for [company] earnings", "pre-earnings", "earnings setup", or "preview Q[X] for [company]".
---

# Earnings Preview

Sourcing, evidence labels, freshness, market-data arithmetic and the readiness posture follow the `research-conventions` skill. Load it before the first deliverable.

Everything in the preview locates the stock against one object: the **bar**, the level of results the market is already positioned for. Consensus is one input to the bar, not the bar itself. The preview says:

- where the bar sits;
- what could clear it or miss it;
- what to listen for on the call;
- how the stock is likely to react if the print lands each way.

After the print, route to `earnings-analysis`.

**Missing inputs never shorten the preview.** A section whose input is unavailable keeps its heading and carries a labelled gap that says what is missing and what would supply it. A short note reads as a thin setup. A full note with three labelled gaps reads as the truth.

**Preview-specific correctness rules**, on top of the shared market-data rules:

- **Freeze the clock.** Record one as-of moment for the whole set of time-sensitive inputs (consensus, whisper, options, price, positioning) and state it at the top. An input with no as-of is a gap, not an estimate.
- **No percent change on an unstable base.** When the denominator is zero, negative or definitionally unstable, show the absolute change instead.
- **Flag broken comparisons.** Mark a year-over-year comparison non-comparable when the company changed the metric's definition and published no restated bridge.

## Workflow

### Step 1: Gather Context

Pull the setup using whichever connectors are available. The source rankings are in `research-conventions`.

- **Consensus, earnings history and price targets**: FactSet, S&P Capital IQ or LSEG. Use web search only as a fallback, labelled with the outlet and the retrieval time.
- **Reported history and KPIs**: Daloopa or the fundamentals connector, checked against the filings.
- **Guidance in force**: the prior quarter's release, its 10-Q or 10-K, and any 8-K since.
- **The prior call**: its full transcript (Aiera, FactSet or S&P Capital IQ), for guidance language and commentary. Work from the transcript, not a summary.
- **Price history and the event window**: a market-data connector.
- **Positioning**: short interest and ownership, at their publication lags.
- **News since the last report**: MT Newswires and web search.

Confirm the earnings date and session (pre-market or after-hours) from the company's own announcement or an event calendar. Never infer them.

Pin a **period map** once and reuse it everywhere: the preview quarter, the prior quarter, the year-ago quarter, and the quarter two years ago. Take each fiscal label from the name of the earnings event. Every table, chart, scenario and options reference uses those same four labels. Ask the user only when the preview quarter is genuinely ambiguous, for example when the company reports two quarters within one month.

**Done when** the four period labels are written down, the freeze-time as-of is recorded, and the earnings date is confirmed from a primary source or an event calendar.

### Step 2: Build the Expectation Bar

There are five expectation sources. Keep them separate, because they say different things, and collapsing them is how a preview ends up measuring the print against the wrong number.

| Source | What it is | Where it comes from |
|---|---|---|
| Company guide | the range management put in force, with its date and venue | the prior release, the prior transcript, any 8-K since |
| Published consensus | the mean estimate and the analyst count, with its vintage | FactSet, S&P Capital IQ or LSEG; otherwise web search, labelled with its retrieval time |
| Whisper | the buy-side number, when it is genuinely sourced | see the whisper rules below |
| Our base | what we expect, built from the drivers | our own model, or the driver work in this preview |
| Last-reported baseline | the run rate the company actually printed last quarter | the prior release |

Close the table with one sentence stating where the bar sits and why: which of the five sources the stock is trading against, and how far the others sit from it.

**Whisper rules.** Whisper numbers from buy-side surveys are often more relevant than published consensus, but only when they are real:

- Never blend a whisper into consensus without showing the bridge.
- With strong support, carry the whisper as a value, with its source and a confidence label.
- With weak support, turn it into qualitative setup language rather than a number.
- With no outside whisper at all, either derive an implied whisper from the guide midpoint plus this management's beat history, labelled `model-derived`, or write "not provided" and leave the row empty.

**Done when** all five rows are filled or carry the reason they are absent, and the bar sentence states the chosen bar's value, source, vintage and basis. Label it `judgement` wherever the five rows leave competing bars in play.

### Step 3: Watch the EPS Quality

Headline EPS is a poor proxy for recurring earnings more often than a preview assumes, and the items that distort it are knowable in advance.

| Item | Why it distorts | Pre-print risk | What resolves it after the print | Model line it hits |
|---|---|---|---|---|

Screen at least these:

- the effective tax rate, against the guided or trailing rate;
- the diluted share count: buyback timing, issuance, convertible dilution;
- below-the-line and mark-to-market items;
- FX translation and remeasurement;
- disposals, impairments, restructuring and litigation.

Then check the basis: does published consensus measure the same thing the company reports? If it does not, say so, and say which figure the bar actually rests on. The real bar is often revenue, operating income, segment profit or free cash flow rather than EPS, and a preview that assumes EPS can end up measuring the wrong number.

**Done when** each screened item carries a pre-print risk, and the preview states whether the consensus and company bases match.

### Step 4: Bridge the Guide to an Implied Bar

A guide is a starting point, not an expectation. Convert it using this management's own record:

- **Beat frequency** over the last eight quarters against its own guide, per metric.
- **Typical beat size**, in currency for level metrics and in basis points for rate metrics.
- **Trend in conservatism**: whether it is steady, widening or fading, and what changed if it moved.
- **Limits of the sample**: how many quarters it covers, and whether the management team or the guidance policy changed within it.

**Done when** the implied bar is stated as a number or a range, with the beat history that produced it, and the sample's limits are named.

### Step 5: Key Metrics Framework

**Financial metrics:**
- Revenue vs. the bar (total and by segment)
- EPS vs. the bar
- Margins (gross, operating, net): expanding or contracting?
- Free cash flow
- Forward guidance vs. consensus

**Operational metrics** (sector-specific default pack):
- Tech/SaaS: ARR, net retention, RPO, customer count
- Retail: same-store sales, traffic, basket size, inventory
- Industrials: backlog, book-to-bill, price vs. volume
- Financials: NIM, credit quality, loan growth, fee income
- Healthcare: scripts, patient volumes, pipeline updates
- Energy and materials: volumes, realized price, unit cost

**Selection rule.** The issuer's own disclosure model beats the generic pack. Use the metrics this company guides on and gets asked about. If an important sector metric is not disclosed, list it as a data request; do not drop it silently. Rank the list by which metric moves the stock, not by which one leads the P&L.

Flag as material:

- a gap between guide, consensus and whisper wider than the sector norm;
- a metric breaking its trailing four-quarter slope;
- growth decelerating, or margin compressing, past a stated threshold in basis points.

For a seasonally distorted metric, or one with a distorted base year, show the two-year stacked growth rate beside the year-over-year rate.

**Done when** the metric list is ranked, each entry carries the expectation it will be measured against, and undisclosed metrics appear as data requests.

### Step 6: Read-Throughs

| Name | Relationship | What they reported | Why it matters here | Read-through | Confidence |
|---|---|---|---|---|---|

Cover these, for the period since the subject's last report:

- competitors, suppliers, customers and sector bellwethers that have reported;
- the macro releases that bear on the quarter.

A read-through with no named transmission channel is a coincidence, not a signal. State the channel, or drop the row.

**Done when** every row names its channel and carries a confidence label, and the table says which read-throughs consensus already reflects.

### Step 7: Scenario Analysis

Build three scenarios against the bar, not against last year:

| Scenario | Revenue | EPS | Key Driver | Management tell | Falsifier | Stock Reaction |
|----------|---------|-----|------------|-----------------|-----------|----------------|
| Bull | | | | | | |
| Base | | | | | | |
| Bear | | | | | | |

For each scenario, say what would need to happen operationally and what management commentary would signal it.

Calibrate the reaction column on history rather than intuition:

| Quarter | Result vs. the bar | Next-day move | What drove the move | Continued or reversed |
|---|---|---|---|---|

Then state what is already priced in, and the two asymmetries that matter:

- what would make a weak print buyable;
- what would make a strong print fadeable.

**Options-implied move.** Pull it from a connector's options data in the same session the preview is written:

- the at-the-money straddle mid for the first expiry after the print, divided by spot;
- the expiry, recorded beside the figure.

The implied move tells you what the market expects; compare it to your scenarios. It is an earnings hurdle only when the expiry brackets the event tightly. When the nearest expiry sits well past the print, relabel the figure as volatility context for that expiry, keep it out of the headline, and say what it does and does not measure. With no options data available, the row carries a labelled gap.

**Done when** each scenario names its driver and its falsifier, the reaction column rests on the historical table, and any implied move carries its expiry.

### Step 8: Catalyst Checklist and Call Questions

Rank three or four **must-watch** items, the things that will decide the stock's reaction, and put nothing else at the top. A list of eight equally weighted questions is not a plan.

Each must-watch item carries four things:

1. Why it matters, in one clause tied to the bar or a thesis pillar.
2. The answer that validates the view.
3. The answer that breaks it.
4. The specific phrases to listen for, including the hedges that signal an answer is being avoided.

Any material news since the last report that creates a contradiction or an open diligence item becomes a question here, not a standalone news bullet. Everything else, including sector add-ons and second-tier items, goes in an overflow bank below the must-watch list, which can run to eight or so.

**Done when** the must-watch list is three or four ranked items with all four parts, and every open news item is either a question or explicitly closed.

### Step 9: Output

**Page one** is the preview a PM reads in two minutes:

- Company, quarter, earnings date and session, freeze-time as-of, readiness posture
- The expectation bar table and the bar sentence
- Key metrics to watch, ranked, with the materiality flags
- The bull/base/bear scenario table
- The must-watch call questions
- Trading setup: recent stock performance, positioning, and the implied move with its expiry
- The call: from the input-gated list in the `research-conventions` judgement rules. Without a sourced implied move, positioning context and adequate consensus or whisper evidence, the preview delivers a setup and a reaction framework, not a trade-ready call, and names the missing input.

**Supporting sections** follow:

- the EPS-quality watch;
- the guide-to-bar bridge;
- peer and macro read-throughs;
- historical reactions and what is priced;
- the overflow question bank;
- the **missing evidence** block: each input that must be refreshed before taking event risk, what supplies it, and the conclusion it currently blocks. The block appears even when it is empty.

When the user asks for a one-page preview only, deliver page one plus the missing-evidence block. Deliver as markdown, or as a Word document when the user wants one.

**Lead with what moves the stock.** When a growth rate, an acceleration, a surprise percentage or a change in guidance is what moves the stock, that is the headline number, and the absolute figure is supporting detail. Trend charts use the margin the business is actually run on (operating, adjusted operating, EBITDA, contribution or free cash flow) rather than defaulting to net margin, and the preview says which one and why.

### Pre-delivery checks

- [ ] Period map explicit, with the same four labels used in every table and chart.
- [ ] Freeze-time as-of stated, and every time-sensitive figure inside its freshness threshold or marked aging.
- [ ] Every bar number carries its source, as-of, unit and definition.
- [ ] Guidance, consensus and whisper appear as separate rows, never blended.
- [ ] EPS-quality section present whenever EPS is the bar, with the consensus-basis check stated.
- [ ] Rate figures in basis points; level figures in percent or currency; no percent change on an unstable denominator.
- [ ] Chart axes agree with the units in the adjacent table.
- [ ] Each scenario states its driver and its falsifier.
- [ ] Implied move either brackets the event or is relabelled as context for its expiry.
- [ ] Must-watch questions capped at four, and ranked.
- [ ] Missing-evidence block present, and every gap labelled rather than dropped.
- [ ] Readiness posture stated; when it is below `decision-grade`, it names the input holding it back.

## Important Notes

- Consensus estimates change. Always note the source and the date of the estimates.
- Historical earnings reactions help calibrate expectations. Build the reaction table from price history, not from memory.
- A preview with no view is a calendar entry. The bar sentence and the must-watch list are where the view lives.
