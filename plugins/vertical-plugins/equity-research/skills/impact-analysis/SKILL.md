---
name: impact-analysis
description: Translate a macro, policy, rate, commodity, geopolitical, or industry shock into equity exposure through a named transmission channel — which names are hit or helped, through which line item, by how much, when, and whether the market has already priced it. Triggers on "what does X mean for", "impact of", "exposure to", "who benefits from", "tariff", "rate cut", "oil shock", or "new regulation".
---

# Impact Analysis

Sourcing, evidence labels, freshness, market-data arithmetic and the readiness posture follow the `research-conventions` skill. Load it before the first deliverable.

This skill is built around one object, the **transmission chain**: event, then channel, then driver, then line item, then action. A shock reaches a share price only by reaching a named landing: a financial line item, or the valuation input a discount rate moves directly. A claim that cannot name where it lands is a mood about a theme, and it does not ship.

This is the work between `morning-note`, which says something happened, and the models, which say what a company is worth.

**The default output is an exposure map.** Unless the user supplied a position list, the report names candidates in research-queue language, and says in one sentence what would turn the screen into an action. Every name in it is a research candidate until the user says otherwise.

## Workflow

### Step 1: Frame the Shock

Write the event in one sentence that carries four things:

- what changed;
- who decided it;
- the date it takes effect;
- what was expected before it.

The last one is the whole analysis in miniature: a fully anticipated shock reaches the line item but never reaches the price.

**Timing bucket.** Every claim in the report carries one of four buckets. The headline claim carries its bucket in the first two sentences.

| Bucket | Window | What lands here |
|---|---|---|
| `immediate` | days | the multiple, sentiment, anything that reprices before a number moves |
| `this quarter` | the current reporting period | a line item that moves before the next print |
| `this year` | the next four quarters | contract resets, hedges rolling off, inventory turning over |
| `structural` | beyond four quarters | where capacity is sited, supply chains relocating, a changed cost curve |

**Freeze the as-of.** Record one moment for the whole set of time-sensitive inputs (prices, consensus, the macro series, the policy text as published), and state it at the top. An input with no as-of is a gap, not an estimate.

**Scope and depth.** Take scope (sectors, geographies), horizon and benchmark from the request and the context, per the `research-conventions` intake rules. Ask only about the forks they leave open. Depth defaults to `working analysis`; a single "what does this mean for X" is a `first pass`.

**Done when** the event sentence carries its effective date and what was expected before it, the headline claim carries one timing bucket, the freeze-time as-of is written down, and the output is stated as either an exposure map or a list of names the user supplied.

### Step 2: Name the Channel

Every impact is one written chain with five links:

**Event** → **channel** (the mechanism that carries it) → **driver** (the operating quantity that moves: units, price per unit, input cost per unit, the rate paid, days of working capital) → **line item** → **action**.

The landing comes from a closed set:

- revenue (net interest income, for a bank or lender);
- gross margin;
- opex;
- interest;
- tax;
- capex;
- working capital;
- share count;
- the valuation input itself (the discount rate, and the multiple that carries it), for a shock that reaches the price through no operating line at all.

Which of these a given channel reaches first is set out in `references/channels.md`.

*Worked example:* a 100bp policy-rate cut runs through the rates channel. It lowers the coupon on the floating-rate half of the debt, and lands in interest expense from the next reset date. The action is to watch interest expense in the first print after that reset.

**A claim with no channel goes back to source work.** The next move is a search, not a softer sentence. Look for:

- the primary text of the rule or release;
- the company's segment and geographic disclosure;
- the input-cost or hedging note.

Where the chain still will not close, the item ships as an observation with no implication attached, and the report says what would close it.

When the event runs through a channel you have not mapped, or the first affected line item is not obvious from the disclosure, read `references/channels.md`. For each standard channel it gives the line item it reaches first, its typical lag, and the early sign that it is happening.

**Done when** every impact claim in the draft is one chain with all five links written out. Every claim that will not complete its chain is either removed or listed as source work, naming the document that would complete it.

### Step 3: Separate the Orders of Effect

There are three orders of effect, each at lower confidence than the last. Report them in separate rows or paragraphs, and never blend them into one conclusion.

| Order | What it must name | Confidence ceiling |
|---|---|---|
| direct | the channel, and the line item on the company's own statements | as strong as the disclosure that sizes it |
| second | whose behavior has to change in between (a third party, never the subject), and what they do differently | always below the direct claim behind it |
| third | both intermediaries, and the price, policy or competitive position that shifted between them | directional only: a sign and a mechanism, never a magnitude |

A second-order claim inherits the uncertainty of the direct claim underneath it, and adds a behavioral assumption. So a conclusion that blends a direct and a third-order effect at one confidence reads as evidence while actually being arithmetic on a guess. Where a third-order effect is the whole reason a name is in the table, say so in the row.

**Done when** every claim carries its order, the orders sit in separate rows or paragraphs, and no second- or third-order claim is stated in language reserved for a sourced one.

### Step 4: Build the Exposure Table

**Find the names from disclosure, not reputation.** A name enters the table because a disclosed figure puts it there. Use whichever connectors are available:

- **Candidate universe:** a connector's screening (FactSet, S&P Capital IQ), or the peer set from `sector-overview` or `idea-generation`.
- **The filings:** the segment note, the geographic revenue split, the input-cost and hedging notes, the debt maturity schedule, and the risk-factor section, which often names the exposure in the company's own words.
- **Fundamentals connectors** (FactSet, S&P Capital IQ, LSEG, Daloopa): the line item the channel lands on, and its trailing sensitivity.
- **Consensus and estimate history, prices since the event, and the multiple against its own range:** the same connectors.
- **The macro series behind the shock, and the release calendar** that will confirm or deny it: the issuing agency or a connector.
- **The primary text of the instrument** (the rule, the tariff schedule, the agency release, the company statement), by web search and fetch. The text of the instrument beats every summary of it.

| Name | Order | Channel | First line item | Direction | Magnitude | Timing | Confidence | Priced-in | Label | As-of |
|---|---|---|---|---|---|---|---|---|---|---|

Rank by sign first, then by magnitude, timing, confidence, directness, and priced-in status, so that the most exposed and least priced names sit at the top.

**Magnitude comes from a disclosed figure, with its arithmetic shown,** in the units the line item uses: basis points for a margin, percent or currency for a level. Where the disclosure will not size it, write a bound instead of a point, and name the disclosure that would size it. For example: "Imported inputs are under 20% of cost of sales, so the gross-margin effect is at most 180bp."

**One shock, two channels, two rows.** A name reached by one shock through two channels with different signs or lags gets two rows, never one merged row. The general rule for sharing a row is in the `research-conventions` judgement rules.

**Show both signs, or say why there is only one.** A shock with only losers usually means the search stopped at the obvious side. Look for the domestic substitute, the toller who passes the cost through, the supplier of the workaround. A one-sided table carries a sentence explaining why the other side is empty.

**Done when:**

- every row names its channel, first line item and direction;
- every magnitude is either sized with its arithmetic shown, or written as a bound that names the disclosure that would size it;
- every row carries an evidence label and an as-of;
- both signs are populated, or the reason for one side being empty is written;
- no two rows were merged on theme alone.

### Step 5: Split Priced-In from Needs-Proof

For each name in the top rows, take three readings, all against the freeze-time as-of and one common base date set at the event:

- **The move since the event**, with the same base and end dates for every name in the table.
- **The direction of revisions**: consensus now against consensus at the event, from a connector's estimate history, with both vintages. Where no estimate history is available, label the row an evidence gap rather than inferring the earlier level.
- **The multiple against its own historical range.**

Then give each name one of two labels, using the "priced in" test in the `research-conventions` judgement rules:

- **Priced in**: both the move and the revisions already carry the channel's effect. The row says which move and which revisions.
- **Needs proof**: anything short of both. The row names the print, filing or release that would put the claim into the numbers, with its date.

**Attribute the move.** A move nobody can attribute is a question, not a confirmation. Attribute what the data supports, and say what stays unattributed.

**Done when** every top-ranked name carries its move with the common base date, its revision direction with the consensus vintages, and exactly one of the two labels, and every needs-proof label names a dated event that would settle it.

### Step 6: Answer the Strongest Counterargument

State the best case against the conclusion, as someone who holds it would state it. Then answer it with exactly one of four verdicts:

- **Weaker**: the channel is real, but smaller than it looks.
- **Later**: the lag pushes the effect past the horizon the report is written for.
- **Already priced**: Step 5 found it in the revisions.
- **It wins**: the conclusion changes to match, and the report says the counterargument moved it.

A counterargument you can dismiss in a clause was not the strongest one available.

Five mechanisms defeat impact claims often enough that each should be tested by name:

1. **Pass-through.** Who actually absorbs the cost? A supplier with pricing power moves the effect onto its customer, and the name in the table is then the wrong one.
2. **Substitution and re-routing.** The input, the route or the jurisdiction changes, and the exposure the filing describes stops being the one the company actually runs.
3. **Contracts and hedges.** A hedge book or a fixed-price contract can delay the whole effect past the horizon. That turns a magnitude claim into a timing claim.
4. **Reversal and carve-outs.** Exemptions, transition provisions, phase-ins and litigation move the effective date recorded in Step 1.
5. **Offsetting exposure inside one name.** The same shock reaching a company through two channels with opposite signs nets to less than either row implies.

**Done when** the counterargument names a mechanism rather than a mood; the answer is one of the four verdicts, with the evidence behind it; the conclusion has changed wherever the verdict was "it wins"; and each of the five mechanisms is either tested or listed as open, with what would test it.

### Step 7: Output

Sections, in order:

1. The answer, in the first two sentences.
2. The event, its effective date, and the freeze-time as-of.
3. Posture and depth, in one sentence.
4. The transmission map.
5. Orders of effect.
6. The exposure table.
7. Priced-in against needs-proof.
8. The counterargument.
9. Monitoring.
10. Missing evidence.

**Format.** Answer a short ask inline, at `first pass` depth. Build a Word document when the user wants one, or when the work runs to `working analysis` or deeper.

**Posture.** Below `decision-grade`, the posture names the input responsible. For this skill that is usually the disclosure that would size a magnitude, or an effective date the rule text has not yet fixed.

**Monitoring table:** one row per item, every field present.

| Metric | Threshold | Source | Date or window | Action if crossed | Action if not |
|---|---|---|---|---|---|

The metric is the one the channel moves first, so each row is the channel's early sign from Step 2 turned into a dated observation.

**Missing evidence:** present even when empty. Each missing input, what would supply it, and the conclusion it blocks.

**The call.** The call comes from the input-gated list in the `research-conventions` judgement rules. With an exposure map and no holdings, the honest calls are watchlist, wait for proof and re-underwrite, each naming its trigger level or its dated proof point. For a name the user wants taken further, route it to `trade-pitch`; for a dated proof point, route it to `catalyst-calendar`.

**Done when** the answer sits in the first two sentences; posture and depth travel together in one sentence near the top; every monitoring row has all its fields; the missing-evidence block is present; every call has its inputs in hand; and the artifact sits inside its depth band.

## Important Notes

- The rule text beats the headline. Announcement date and effective date are different facts, and only the second one moves a line item.
- Lag belongs to the buffer between the event and the line item (inventory, contracts, hedges, reset dates), not to the event. That is why two companies hit by one shock report it two quarters apart.
- A one-sided table, or a table full of third-order names, is usually a sign the source work is not done.
