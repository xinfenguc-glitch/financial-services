# Judgement

Reference file for `research-conventions`. Load it before writing a valuation, a thesis, a rating or price target, a scenario set, or any section that ends in what to do.

The evidence rules decide what may be said. This file decides whether what is said is worth a reader's time.

## The seven questions

A substantial output answers all seven somewhere, in whatever order its own structure wants. A section that answers none of them is background, and background is the first thing to cut when the artifact runs long.

1. **Variant view.** What do we believe that the market does not, and which evidence creates the difference?
2. **What is priced.** At the current price, what does the market already assume? Apply the `priced in` test below.
3. **Estimate path.** Where do estimates go over the next two to four quarters, and which way does revision risk lean?
4. **Mechanical downside.** What breaks, through which line item, and to what number? A narrative risk is not a downside case.
5. **Catalyst.** Which dated event turns the view into a price move, and is it scheduled, likely or speculative?
6. **Falsifier.** Which observation would prove us wrong, and when will we be able to see it?
7. **Action.** What does the reader do, at what level, and what would change it?

## Action language, gated by inputs

Each call has to be earned by the inputs in hand:

| Call | Available once you have |
|---|---|
| add, initiate, increase | a live price, a valuation anchor, and a catalyst inside the horizon |
| hold, trim, exit | a known existing position to act on |
| hedge | the instrument, its cost, and the basis risk it leaves |
| watchlist | a trigger level or a dated event |
| wait for proof | the named proof, and where it will show up |
| re-underwrite | the specific input that broke |

Without holdings, sizing inputs or live execution data, which is the usual case, the honest calls are watchlist, wait for proof and re-underwrite. Name the missing input in the same sentence, and say what would turn the screen into an action.

Ratings are a separate vocabulary. A rating (and a change to one: upgrade, downgrade, maintain) describes the published view, and it sits beside the call, never in place of it. Use the rating ladder the user, the firm or the calling skill sets. When none is set, use Buy / Hold / Sell and say so. A price target is a valuation anchor: it carries its method, its horizon and the range around it.

Position sizes and execution instructions are outside these skills. They draft analysis for a professional to review and act on.

## Price is belief, not truth

The current price says what the market expects, not what is true. Keep the two claims apart in the writing. "The multiple implies growth of X" is a statement about belief. "The company grows at X" is a statement about the company. The view is the gap between them, so blurring the two erases the view.

## Priced in

A claim is `priced in` when two things already reflect its effect on the line item, in the right direction and at roughly the right size:

- the affected names' price move, and
- their estimate revisions.

A multiple that sits where the news implies supports the label, but on its own it is not the test. Anything short of both reads `needs proof`, and the label names the print, filing or release that would put the claim into the numbers, with its date. Base the test on the affected names and their revisions, never on an index move.

## The strongest counterargument

Every conclusion carries the best case against it, put as strongly as someone who believes it would put it. Then answer it with one of four verdicts: weaker, later, already priced, or it wins. When it wins, the conclusion changes to match, and the artifact says the counterargument moved it. A counterargument you can dismiss in a clause was not the strongest one available.

## Name the binding constraint

When several lenses give different answers (valuation, liquidity, mandate, conviction, risk budget), the answer is the most restrictive credible one. The output names which lens bound it. That name is what lets someone re-derive the answer when one input moves.

## Every remedy carries its failure

Any proposed mitigation (a hedge, a staged entry, a stop, a diversification) ships with at least one scenario in which the mitigation itself fails. Set it beside the plain alternative of simply taking less risk.

## Monitoring items

A monitored item names six things:

- the metric
- the threshold
- the source that will show it
- the date or window when it becomes observable
- the action if the threshold is crossed
- the action if it is not

As a table that is `| Metric | Threshold | Source | Window | Action if crossed | Action if not |`. A skill that tracks items over time may lay its table out differently or add columns, such as confirming and disconfirming signals or provenance, but each monitored item still names these six.

"Watch the next print" is a placeholder. "Net revenue retention below 108% in the Q3 release on 2026-11-04 retires pillar two" is an item.

## Falsifiable claims

Before an artifact is finished, turn its narrative into two to five claims. Each carries six fields:

| Claim | Evidence today | Implication if true | Test metric | Falsifier | Time to knowable |
|---|---|---|---|---|---|

Fewer than two claims means the artifact holds no view. More than five means the view was never prioritized.

## Asymmetric readiness

Evidence sufficient to decline is not evidence sufficient to initiate. A short, well-sourced answer that says the work does not support a position, and names what would, is a finished answer. It is not a failure to deliver. Say which side of the asymmetry the evidence reaches.

## Discounting

A case built on forward earnings times an exit multiple is not a return until it is discounted. Show a present value with the discount rate stated, or an annualized return against a stated hurdle, and state the horizon either way. An undiscounted terminal value flatters every multi-year case by exactly the time value it skipped.

## Probabilities

A probability set is complete when its states are mutually exclusive, cover the space, and sum to one. When a set is incomplete:

- withhold the weighted figure;
- show the scenarios unweighted, labelled as an illustrative skew;
- say why the set is incomplete.

An expected value computed from a set that does not sum to one supports no conclusion, however carefully the scenarios were built.

## Orders of effect

Report direct, second-order and third-order effects in separate rows or paragraphs, each with its own confidence level. A direct effect names the channel and the line item it lands on. A second-order effect names whose behaviour has to change in between. When you cannot name the transmission channel, the claim is not ready to write. Go back to the sources instead.

## Row-merge discipline

In any exposure, driver or comparison table, two names share a row only when three things match: the channel (or dimension), the first line item it lands on, and the direction.

Thematic adjacency is not a reason to merge:

- Two names touched by the same shift through different line items are two rows.
- A name exposed through two channels with different signs or lags is two rows.

A merged row that hides a difference in direction is the failure this rule exists to catch.

## Audience modes

The facts stay the same; the first paragraph changes. Take the mode from what the user has said, or from the context per `intake.md`, and lead with what that reader reads first.

| Mode | Reads first | Ends on |
|---|---|---|
| Sell-side publication | the rating, the price target and what changed | the estimate changes and the risks to the target |
| Long-only, benchmark-aware | the position against the benchmark weight, and what the estimate path does to it | overweight, underweight or avoid relative to the benchmark, with the benchmark risk named |
| Long/short | the variant view, and whether the short leg can be put on at all | the expression and its falsifier |
| Event | the dated event, its conditions and the payoff around it | timing risk, and what breaks the event |
| Index-aware | flows, weight changes and what is mechanically forced | the dates the flows happen on |
