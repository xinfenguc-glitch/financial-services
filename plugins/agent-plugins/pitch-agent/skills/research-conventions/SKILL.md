---
name: research-conventions
description: The shared evidence, sourcing, freshness, judgement, intake and market-data rules every equity research deliverable follows. Load before the first deliverable of a research task; when a number has no source; when two sources disagree; when a figure may be stale; when deciding what to ask the user; and before any valuation, thesis, rating or recommendation.
---

# Research Conventions

This is the shared layer under the research skills. Each research skill says what to build. This one says what a figure has to carry, how far the evidence lets the language go, what is worth asking before starting, and how periods, windows and returns are computed. The rules live here so that no skill has to re-derive them.

## Precedence

1. **Agent guardrails win.** When you are running as a named agent (earnings-reviewer, market-researcher, pitch-agent and the rest), its guardrails hold over anything here: review stops, `[UNSOURCED]` marking, no distribution.
2. **The calling skill owns its deliverable.** Nothing here changes its workflow, format, length band, required sections or its own checkpoints. For example, `initiating-coverage` still runs one task per request.
3. **This skill owns evidence.** How a figure is sourced, labelled, dated and computed follows these rules. If a calling skill names a weaker source (web search for consensus, say), use the higher tier from `references/evidence.md` when that connector is available. Otherwise fall back to the skill's source and label it.

## Reference files

Load each file when its trigger applies. None needs to be read up front.

- `references/evidence.md`: before the first figure lands in a deliverable; when a number has no source, two sources disagree, a figure may be stale, or you are deciding how densely to cite.
- `references/judgment.md`: before a valuation, a thesis, a rating or price target, a scenario set, or any section that ends in what to do.
- `references/intake.md`: before asking the user anything at the start of a task, and when deciding whether to ask at all.
- `references/market-data-rules.md`: before the first market-data pull for anything that prints a period label, a multiple, a growth rate, a margin or a return.
- `references/depth.md`: when choosing how long a deliverable runs, when a draft is over its length band, or when the user asks for a short version of something already built.

## Readiness posture

Every deliverable states one posture, once, near the top, in the reader's language. Posture describes the inputs, not conviction. A high-conviction view that rests on stale inputs is not decision-grade, and saying so is what makes the rest of the artifact usable.

| Posture | Holds when | Forced down by |
|---|---|---|
| `decision-grade` | every load-bearing figure is sourced and inside its freshness threshold, the downside is built through line items, and the inputs the recommended action needs are in hand | one load-bearing figure that is stale, unsourced or contested |
| `review-ready` | the analysis is complete and sourced, and one check or one input is still open | an unresolved conflict on a load-bearing claim, or a check that fails |
| `screen-grade` | coverage or depth is deliberately thin and the artifact says so | a headline conclusion that outruns the coverage behind it |
| `not-ready` | a load-bearing claim is unsupported, stale or contested with nothing to settle it, and the conclusion rests on it | already the floor for a claim problem; state what would lift it |
| `blocked` | an input cannot be obtained at all (a connector that is not available, an undisclosed metric, a document we do not have) | already the floor; name the missing input and what would unblock it |

A posture below `decision-grade` names the figure or input responsible, so the reader can decide whether it matters to them. Read the posture from this table against the current state of the inputs. Never step it up or down from a previous value: when an input changes state, re-read the rows. This is the only readiness scale. A skill that needs a finer status for one of its objects can label that object, but the artifact still carries one posture from this table.

An agent draft that stops for analyst review is usually `review-ready` or lower. The analyst's approval does not raise the posture. Only fixing the inputs does.
