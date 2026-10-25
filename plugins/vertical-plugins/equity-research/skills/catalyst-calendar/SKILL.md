---
name: catalyst-calendar
description: Build and maintain a calendar of upcoming catalysts across a coverage universe — earnings dates, conferences, product launches, regulatory decisions, flow events, and macro releases — ranked by what each event can change, with honest date confidence, prep owners, and a weekly preview. Helps prioritize attention and position ahead of events. Triggers on "catalyst calendar", "upcoming events", "what's coming up", "earnings calendar", "event calendar", "catalyst tracker", or "what should I prepare for".
---

# Catalyst Calendar

Sourcing, evidence labels, freshness, market-data arithmetic and the readiness posture follow the `research-conventions` skill. Load it before the first deliverable.

A list of dates is not a catalyst calendar. A catalyst calendar ranks events by **decision pressure**. An event earns its place because it can move:

- the estimate path
- the narrative
- the multiple
- position size
- the downside case
- liquidity
- the odds of another event

Proximity alone ranks nothing. A high-materiality readout in eleven weeks outranks a routine print on Thursday, and the routine print belongs in the hygiene block.

## Workflow

### Step 1: Define Coverage Universe

Settle four things:

- **Universe**: tickers or names, a portfolio or watchlist file, a sector, or an index.
- **Horizon**: the next two weeks, a month, a quarter, or through the next reporting season.
- **Macro scope**: whether macro releases and policy dates are in scope, or only issuer events.
- **Destination**: whether the output stays on the desk or goes outside it. This decides the externally clean rule in Step 7.

Take what the request and the context already answer, and ask only about what is left open, per the intake rules in `research-conventions`. The universe has no default, so ask for it when nothing names one. The others default as follows; disclose each default you take:

- **Horizon**: the next two weeks, matching `/catalysts`.
- **Macro scope**: the macro releases that bind the universe's sectors.
- **Destination**: the desk.

**Done when** the universe resolves to a named list of issuers, the horizon has dates, and both the macro decision and the destination are recorded.

### Step 2: Gather Catalysts and Classify Them

Pull live rather than recalling, using whichever connectors are available (tiers in `research-conventions` `references/evidence.md`):

- Event calendars from FactSet, S&P Capital IQ or LSEG: earnings dates and sessions, conferences, shareholder meetings.
- The macro release calendar from the issuing agency or a connector.
- The prior call's transcript (Aiera, FactSet, S&P Capital IQ) for guided timing language.
- Newswires (MT Newswires) for announced dates.
- Web search and fetch for the events no calendar feed carries: regulatory dockets, trial registries, conference agendas, lockup terms, contract expiries.

Company, regulator and exchange sources override an aggregator. When two sources disagree on a date, keep both, set the row's confidence to the lower of the two, and write the disagreement as a conflict-register row.

#### Event groups

**Earnings and financial**
- Quarterly results, with session (pre-market or post-close)
- Annual shareholder meeting
- Investor day, analyst day, capital markets day
- Guidance updates
- Debt maturities and refinancings
- Dividend and buyback authorizations

**Corporate**
- Product launches or announcements
- Regulatory decisions, including FDA milestones and the steps before them
- Contract renewals and expirations
- M&A milestones: shareholder vote, regulatory clearance, close
- Management transitions
- Litigation dates

**Industry**
- Major conferences: dates, which companies are presenting, and which are conspicuously absent
- Trade shows and expos
- Regulatory comment periods and rulings
- Recurring industry data: monthly sales, traffic, channel checks

**Macro**
- FOMC and other central bank decisions (ECB, BOJ, etc.)
- Jobs, CPI and GDP releases
- Scheduled geopolitical dates with market impact

**Index and passive flow**
- Index additions, deletions, rebalances and reconstitutions
- Lockup expiries
- Secondaries and block trades
- Convertible issuance and conversion
- Buyback blackout windows
- Float changes

Each flow event carries the fields that make it assessable:

- the expected flow, in shares and in days of average daily volume
- the holder base behind the supply
- the float change, in percentage points

Flow is mechanical supply and demand, so keep it apart from anything fundamental in the write-up.

#### Classify by the path, not the headline

The class decides what the row must contain to be useful, so classify each event as you capture it. For example:

- A merger date needs the spread, the implied probability and the break-price arithmetic.
- A spin-off needs a sum-of-the-parts value and a forced-selling estimate.
- An activist date needs the vote arithmetic.
- A litigation date needs the merits, the timing, the damages and the settlement path.
- A flow event needs its flow against average daily volume.

Each class has its own core question, required outputs and must-extract list from the primary document, in `references/event-lenses.md`. Read it when a captured event falls outside the earnings and macro classes you already handle, and again when a `P1` row needs its action block (Step 5).

#### Timing fields

Every row carries a date type and a date confidence. They are kept separate because a rumoured hard date and a company-guided window fail in different ways.

| Date type | Renders as |
|---|---|
| `hard` | a single date, with the session where it matters |
| `window` | its span, everywhere: in the table, the workbook and any export |

| Confidence | Basis |
|---|---|
| `confirmed` | a primary source states it: the issuer, the regulator, the exchange, the docket |
| `guided` | the company said roughly when, without committing to a date |
| `expected` | a reliable aggregator or connector carries it, and the issuer has not confirmed it |
| `inferred` | derived from the reporting cadence, a statutory clock or a contractual term |
| `rumoured` | reported by media or a market participant, with no primary support |
| `undated` | thesis-critical, but no date can be established yet |

Never render a window as one day. Presenting "second half" as one Tuesday manufactures a date the issuer never gave. A calendar export carries only `hard` rows.

Undated thesis-critical events are kept, in a review table that records what would date them: a statutory clock, a filing, a conference agenda. They are not dropped.

Each row also records:

- the source name
- the retrieval date
- the publication date of the date itself, when it differs
- a last-checked timestamp

**Done when** every captured event carries a category, a class, a date type, a date confidence and its source details, and every undated thesis-critical event sits in the review table.

### Step 3: Score Materiality and Actionability

Give each event two independent scores from one to five. Combine them by judgement; do not multiply them.

- **Materiality**: how much the event can move the estimate path, the narrative, the multiple, the downside case, position size, liquidity, or the odds of a later event. A 5 changes the thesis; a 1 changes nothing we track.
- **Actionability**: how much we can do about it. A 5 has prep time, a tradable expression and the inputs a decision needs; a 1 is a fact we learn afterwards.

Priority is `P1`, `P2` or `P3`, written with the sentence that justifies it. A high-materiality, low-actionability event is still `P1` when its outcome resets the model.

**Escalators.** Any one of these promotes an event above its base score, and the row names which one fired:

1. It lands within a week and the prep is not done.
2. Date confidence is low while materiality is high.
3. It collides with another portfolio-critical event.
4. Expected volatility is high, or the name trades thinly.
5. The market setup is one-sided: crowded positioning, a stretched multiple, consensus clustered.
6. The asymmetry is not reflected in consensus.
7. It can trigger follow-on catalysts.
8. Missing data is blocking a clean risk decision.
9. The company has a history of pre-announcing, which moves the date that matters earlier.

**Clustering.** Flag every date that carries events for two or more correlated positions, and flag the week where portfolio-level event risk concentrates. A cluster is its own catalyst.

**Done when** every row carries both scores, a priority with its one-line justification, the escalators that fired, and a cluster flag where a date is shared.

### Step 4: Calendar View

The full field set for each event, all of it in the workbook:

- `event_id`, stable across refreshes
- issuer and ticker
- category and subcategory
- event name and a one-line description
- date, date type, date confidence, session and time zone
- source, retrieval date, the date's publication date, last checked
- materiality, actionability, priority and escalators fired
- expected outcome, and what to watch for variance
- prep required, prep owner, prep due date, follow-up date
- decision implication and post-event action
- our positioning: long, short or neutral (desk version only)

The markdown view shows the readable subset:

| Date | Type / confidence | Company/Sector | Event | Class | Materiality | Actionability | Priority | Our Positioning | Prep owner | Due | Decision it supports |
|------|-------------------|----------------|-------|-------|-------------|---------------|----------|-----------------|------------|-----|----------------------|
| | | | | | | | P1/P2/P3 | Long/Short/Neutral | | | |

Routine dates that nothing hangs on go in a hygiene block underneath, listed but unranked. Color-code by priority: red for `P1`, yellow for `P2`, green for `P3` and the hygiene block.

**Done when** every row shows its date type and confidence beside the date, every `window` row shows a span, and every `P1` and `P2` row names the decision it supports.

### Step 5: Prep Plan and Weekly Preview

Each `P1` and `P2` event gets a prep item: the work product, the owner, the due date, and the decision it supports. A prep item with no due date is a wish.

**Per-event action block**, written for every `P1`:

- **Setup and current debate**: what the market is arguing about going in.
- **Metrics that will matter**: the two or three numbers the reaction hangs on.
- **Expectation frame**: guidance; consensus with its vintage; the buy-side bogey where it can be observed; the options-implied move with its session; prior commentary.
- **Our variant view**: where we differ, and the evidence behind the difference.
- **Confirm and disconfirm thresholds**: the level on each side that changes something.
- **Prep plan**: the prep items above, with owners.
- **Post-event playbook**: what each outcome triggers. Write it before the event, so the reaction is not composed under time pressure.

**Weekly preview**, the recurring note:

**This Week's Key Events:**
1. [Day]: [Company] Q[X] earnings: consensus [$X EPS] ([source], as of [date]), our estimate [$X], key focus: [metric]
2. [Day]: [Event]: why it matters for [stocks]
3. [Day]: [Macro release]: expectations and positioning

**Next Week Preview:**
- What needs prep started now

**Position Implications:**
- Events that could move specific positions
- Prep still outstanding
- The risk decision each binary event forces

**Beyond the two-week view:**
- The next thirty days carry high-materiality events, overdue prep and unresolved source conflicts.
- Sixty days carry the events whose pre-work starts now.
- Ninety days carry long-lead work: a model rebuild, an expert call, a channel check.

**Done when** every `P1` and `P2` event has a named prep owner and a due date, every `P1` carries its action block including the post-event playbook, and the preview names next week's prep starts.

### Step 6: Refresh Without Destroying History

A refresh appends. Match incoming events on `event_id`, keep every prior row, and record what changed:

- **A date that moved**: keep the row, update the date, and add the prior date and the source that moved it to the row's history.
- **A row the sources no longer carry**: mark it `stale` with the date it was last confirmed. Do not delete it.
- **A confidence that improved** (for example `expected` to `confirmed`): update it and note the primary source that confirmed it.
- **A row that resolved**: mark it complete, record the actual outcome against the expected outcome, and keep it. The archive of what happened against what was expected is what makes the next preview sharper.

Produce a dated change log with three counts and their rows: added, changed, flagged.

**Done when** the change log lists every row added, changed and flagged, and no prior row was deleted or overwritten in place.

### Step 7: Output

- **Excel workbook** with the full field set, sortable and filterable by priority, class and date. Drive the live workbook when the Excel tools are available. When running headless, use `xlsx-author`.
- **Weekly preview note** in markdown, for email or Slack.
- **Single-event brief**, when the user asks about one date. It covers:
  - timing, with its type, confidence and source
  - the setup and the market expectation
  - what could surprise
  - confirming and disconfirming evidence
  - the prep
  - the post-event action
  - the source caveats
- **Optional calendar export** (an .ics file, or Google Calendar where it is connected), carrying `hard` rows only.

**Externally clean output.** A calendar that leaves the desk carries dates, sources, confidence and public expectations only. These stay in the desk version:

- our positions and cost basis
- unpublished estimates and targets
- the variant view
- trade intent

The two versions are separate files. One file with hidden columns does not count.

#### Delivery checklist

Run this before handing the calendar over. Two checks are hard: they pass, or the calendar does not go out.

| Hard check | Fails when |
|---|---|
| File safety | a user file was overwritten rather than extended, or the desk version left the desk |
| Date honesty | a readout or approval window was rendered as one day, its endpoint is unstated, or a date is presented as firmer than its type and confidence support |

The rest are research checks, covering the errors this artifact actually makes. Any check still failing is disclosed on its own line in the delivery note, with what it costs the calendar's coverage.

| Research check | Fails when |
|---|---|
| Date provenance | an earnings date came from a secondary source and no primary source confirms it |
| Flow completeness | a lockup or secondary appears with no share count, holder base or days of volume |
| Regulatory precision | filing, acceptance, advisory committee, decision and launch are used interchangeably |
| Macro relevance | a macro release is listed with no stated link to a name in the universe |
| Conference reality | a conference is listed without confirming which issuers present |
| Timestamped expectations | consensus or guidance appears without its vintage |
| Scheduled work | an event requires a model update and no prep item carries it |
| Priority sanity | an event with a direct thesis link sits at `P3` |
| Calendar hygiene | duplicates survive, time zones are mixed, or a cluster is unflagged |
| PM usefulness | a row says what happens without saying what could change |

**Done when** both hard checks pass, one readiness posture is stated near the top of the calendar, and every research check either passes or is named individually in the delivery note with its effect on coverage.

## Important Notes

- Earnings dates shift. Re-check each one against the company's IR page or announcement closer to the date, and move its confidence only when a primary source confirms it.
- Some catalysts recur, such as monthly industry data. Build a template and auto-populate it, but date each instance from its own release calendar.
- Conference attendance lists are valuable. Which companies are presenting, and which are conspicuously absent?
- Archive past catalysts with the actual outcome (Step 6). That record builds pattern recognition over time.
