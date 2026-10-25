---
name: trade-pitch
description: Turn finished analysis on one named security into a position — variant view, falsifiable evidence, scenario tree, trade expression, risk, and monitoring — as research output for a professional reader. Triggers on "pitch this name", "should I buy", "long idea on [company]", "short idea on [company]", "trade recommendation", "position", or "risk/reward".
---

# Trade Pitch

Sourcing, evidence labels, freshness, market-data arithmetic and the readiness posture follow the `research-conventions` skill. Load it before the first figure enters the pitch.

This is where the research ends up. A finished analysis becomes a **position**:

- a direction;
- a variant view;
- the evidence that carries it;
- a scenario tree;
- an expression;
- a level that says we were wrong;
- a plan for watching it.

The pitch is research output for a professional reader. Its calls describe what the analysis supports. Execution sits outside it, and size appears only as a fraction of a stated loss budget, per the `research-conventions` judgement rules.

Every figure in a pitch is load-bearing, which makes this the deliverable where unsupported precision does the most damage.

For instrument mechanics beyond long common stock, the short-side gate, and a worked reconciliation of the two loss limits, see `references/expression.md`.

## Workflow

### Step 1: Intake and the Analysis It Rests On

Settle four things before any work starts. Take what the request and the context already answer, per the `research-conventions` intake rules, and ask only about the forks they leave open.

| Slot | Taken from | Default when unstated |
|---|---|---|
| Direction | the request | the direction the source analysis already leans, stated as an assumption |
| Horizon | the context, then the catalyst that closes the gap | two to eight quarters |
| The analysis it rests on | a named artifact: a `dcf-model` workbook, a `comps-analysis`, an `earnings-analysis` print, an `initiating-coverage` report, an `impact-analysis` exposure row, an `idea-generation` shortlist entry, or the user's own stated view | none; see below |
| Mandate | the context: vehicle, benchmark, risk posture, scope, instruments allowed | disclosed in the delivery message |

**The pitch rests on something named.** Record the artifact, its as-of, and which of its outputs the pitch uses: the fair-value range, the peer multiple, the revision path. Where no finished analysis exists, say so in one sentence and name the skill that would produce it. Then either build that first, or deliver a `screen-grade` pitch that says the underwriting is still owed.

**Posture.** State the readiness posture once, near the top. For a pitch, the inputs that count are:

- a live price;
- a valuation anchor;
- a dated catalyst;
- an established borrow, on a short leg;
- the sizing inputs in `references/expression.md`.

**Done when** direction, horizon, the source artifact with its as-of, and every mandate slot carry a value or a disclosed default, and the posture names the specific input that set it.

### Step 2: The Variant View

The variant view has four fields. A pitch without all four is a summary of someone else's work.

1. **What the market believes.** State it at the current price, in the units of the driver the position rests on: the growth rate the multiple requires, the margin the price embeds, the estimate path consensus is carrying. Ground it in the affected names and their revisions, never in an index move.
2. **What we believe.** The same driver at our number, sourced to the analysis from Step 1.
3. **Why the gap exists.** The mechanism that lets it persist, such as:
   - a disclosure lag;
   - a KPI the Street reads on the wrong basis;
   - a misclassified business;
   - a forced seller;
   - a horizon mismatch;
   - an event nobody has dated.

   A gap with no mechanism is usually an error in our own work.
4. **What closes it.** The dated event, or the arrival of evidence, that turns belief into price. Mark it scheduled, likely or speculative.

Before writing this step, read the `research-conventions` judgement rules. They cover the seven questions this section has to satisfy, the rule that price is belief rather than truth, and the requirement to answer the strongest opposing case.

**Done when** all four fields are written; the market's belief is stated in the driver's own units and sourced to the affected names; the gap names a mechanism; and the closer carries a date or window and its confidence.

### Step 3: Evidence as Falsifiable Claims

Turn the argument into two to five claims, using the falsifiable-claims table from the judgement rules plus one added column: the evidence label on each claim's evidence. The working table carries the research label. The delivered document prints the reader-facing word for it.

| Claim | Evidence today | Label | Implication if true | Test metric | Falsifier | Time to knowable |
|---|---|---|---|---|---|---|

An `unsourced` label is a drafting state only. Before delivery, either the figure is sourced or the claim takes the unsupported-claim exit in the evidence rules.

**Done when** the table holds two to five claims; each carries all seven fields; no `unsourced` label survives past review; and removing any one claim would change the recommendation.

### Step 4: Scenario Tree

Build three cases. Each starts from a driver, not from a haircut to the base target.

| Case | Driver and level | Arithmetic to price | Return from spot | Probability | Provenance |
|---|---|---|---|---|---|

Each case moves one named driver to a stated level and carries the arithmetic through to a price, so a reader can move the driver and watch the case move.

- **Provenance** is one of: the model, a source, the user, our judgement, or illustration. Each carries an as-of.
- **Returns** are discounted, or annualized against a stated hurdle, because a multi-year target price is not a return.

**Probabilities.** A complete set is mutually exclusive, covers every outcome and sums to one. When the probabilities are assumed rather than underwritten:

- label the table an **illustrative skew**;
- withhold the probability-weighted figure;
- re-read the posture against that input state.

**Bear-case survivability.** A lower price is not a downside case. State what breaks, through which line item, to what number. Then state whether the company survives it:

- liquidity through the trough;
- covenant headroom against the stressed metric;
- the maturities falling due inside the horizon.

A company that cannot fund its own bear case has a different downside from one that can, and that difference is the whole risk.

**The bear-case exit uses stressed liquidity, not normal liquidity.** Normal and stressed participation are separate lines, never one blended figure. Where the case is a gap risk, the exit price is the post-move price, not the level we would have liked. The mechanics and arithmetic are in `references/expression.md`.

**Done when:**

- each case names its driver, its level and the arithmetic to a price;
- the bear case states liquidity, covenants and maturities through the trough;
- the probability set sums to one, or the table is labelled an illustrative skew and the posture re-read against that state;
- the bear-case exit carries a stressed participation figure beside the normal one.

### Step 5: Trade Expression

| Field | Carries |
|---|---|
| Instrument | common stock, an options structure, or a pair, with the basis risk it leaves |
| Entry | a rule, not a quote ("at or below 48"), with the reference price and its as-of beside it, and the tranches where entry is staged |
| Target | from the valuation anchor in Step 1, as a range rather than a point, discounted or annualized against a stated hurdle, saying which end of the range the position underwrites |
| Exit | three levels (see below) |
| Size | a fraction of a loss budget, per the rule below |
| Binding constraint | which lens set the size: valuation, liquidity, mandate, conviction or the loss limit |

The three exit levels are:

- A **stop**: a price rule, set where the price itself is evidence. State its distance in units of the name's own volatility.
- A **re-underwrite level**: a claim rule, naming the input that broke, taken from the falsifier column.
- A **time stop**: the horizon date at which the absence of the catalyst is itself the answer.

**Size against a loss budget, not a book.** The pitch knows no positions, no net asset value and no mandate limits, so a percentage of a book would be an invented number. State size as what it risks against a budget the reader brings. For example: "at the stop, this position spends a third of a 150bp loss budget." That travels to any book size. Name the binding constraint that set it.

**The two loss limits are different constraints.** A limit stated *inside* a stress scenario ("lose no more than this by the time the bear case has played out") and an absolute cap that must hold *beyond* it ("lose no more than this in any state") give different sizes. Sometimes they give different answers about whether the position should exist at all. Resolve which one the mandate means before recommending anything. Where the mandate does not settle it, show both branches rather than picking one. `references/expression.md` works through an example.

**The short-side gate.** A short pitch carries a gate block with six rows:

- catalyst;
- valuation anchor;
- liquidity;
- borrow and carry;
- option cost;
- hedge ratio.

Mark each row `cleared`, `not cleared`, `missing`, `n/a` or `illustrative`. Any applicable row below `cleared` is named in the recommendation itself, not in a footnote. An `n/a` row is not a gap. An unhedged short cannot satisfy an absolute cap, because there is no price at which the loss stops, so under that reading the answer is a priced defined-loss structure or no position. What clears each row is in `references/expression.md`.

**Every hedge carries the scenario in which it fails.** Two rules sit beside it:

- A hedge that removes the reason the position exists is rejected, not priced.
- The alternative of taking no hedge and sizing down is always stated, so the reader can compare the two.

**Done when:**

- the six expression fields are filled;
- size is stated against a loss budget, with its binding constraint named;
- the two loss limits are resolved, or both branches are shown;
- a short carries all six gate rows, each with one of the five verdicts;
- every proposed hedge carries a failure scenario beside the size-down alternative.

### Step 6: Monitoring

| Trigger | Metric | Threshold | Source | Date or window | Action if crossed | Action if not |
|---|---|---|---|---|---|---|

Every claim in Step 3 must be testable by at least one trigger. A falsifier without a trigger is an intention, not a plan.

**What would change our mind** gets its own short block: the two or three observations that would retire the position, each with the date it becomes observable. Draw them from the falsifier column; do not write them fresh.

Hand the running ledger to `thesis-tracker`:

- the pitch's claims become its pillars;
- the Step 3 falsifiers become its break thresholds;
- the triggers here become its monitoring rows.

Route dated triggers to `catalyst-calendar`. The pitch is a dated document; the tracker is what keeps it honest afterwards.

**Done when** every trigger row carries its metric, threshold, source and date, with an action stated on each side of the threshold; every Step 3 claim is covered by at least one trigger; and the hand-off names the tracker and the first review date.

### Step 7: Output

**Actionability first, background after.** From the top, the order is:

1. **The recommendation line**: call, direction, instrument, entry, target, exit, posture and as-of.
2. **The variant view**, in one sentence.
3. **The missing-inputs block.**
4. **The scenario table.**
5. **The expression and its risk.**
6. **The claim table.**
7. **Monitoring.**
8. **The analysis the pitch rests on.**

A reader who stops after the first screen has the position; a reader who continues gets the underwriting.

**The call** comes from the input-gated list in the judgement rules, and is available only once its inputs are in hand. Without a live price, without sizing inputs, and with no position to act on, the honest calls are watchlist, wait for proof and re-underwrite. Each one names the missing input in the same sentence, and says what would turn the idea into an action.

**The missing-inputs block** is one compact block near the top, not a table of blanks. Each line names what is absent, what would supply it, and what it would change about the recommendation. A section whose input is unavailable keeps its heading and carries its labelled gap. A short pitch reads as a thin idea; a full pitch with three labelled gaps reads as the truth.

**Format.** Deliver one to three pages as a Word document, or slides when the user asks for them (`pptx-author` when running headless). When the draft runs long, see the `research-conventions` depth rules for what to cut first.

**Done when** the first screen carries the call, the position, the posture and the variant view; every label the delivered document prints is the reader-facing word for its research label; and the missing-inputs block names each absent input, with what would supply it.

## Important Notes

- Short ideas need higher conviction. Timing is harder and the risk is asymmetric, which is why shorts face the six-row gate.
- Contrarian ideas need a catalyst. Being early without one is the same as being wrong, and that is what the time stop is for.
- "No position" is a finished answer when the evidence supports declining, or when no structure fits the loss budget.
