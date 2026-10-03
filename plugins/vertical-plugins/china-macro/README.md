# China Macro Plugin

A China macro library for Claude. Each source (book, report or paper) is converted into a structured knowledge base of frameworks, chapter notes, a glossary, patterns, a cheatsheet and a summary. A hub skill adds cross-source analyst workflows, a policy timeline and baseline data.

## Installation

```bash
claude plugin install china-macro@claude-for-financial-services
```

Pair with **financial-analysis** for data connectors (LSEG, S&P Global, FactSet, …) when running the live-data workflows.

## Commands

| Command | Description |
|---|---|
| `/china-macro:library [topic]` | Browse or query the library; `summary` returns a source summary |
| `/china-macro:credit-pulse` | Where China's credit cycle is and who is still borrowing |
| `/china-macro:policy-read [statement]` | Decode a Politburo, PBOC or work-conference signal |
| `/china-macro:risk-ladder [focus]` | How far default risk has moved toward the core, plus guarantee credibility |
| `/china-macro:scenarios` | Weigh Beijing's four strategic options and map market implications |

## Skills

| Skill | Description |
|---|---|
| **china-macro-library** | Hub: routing table, core lens, workflows, timeline (2008 to present), key data with vintages, source registry |
| **wright-deleveraging** | Knowledge base from Logan Wright, *Grasping Shadows: The Politics of China's Deleveraging Campaign* (CSIS, April 2023) |

## Sources

| Slug | Source | Coverage |
|---|---|---|
| `wright-deleveraging` | Wright, *Grasping Shadows* (CSIS, 2023) | Shadow banking; the 2016–19 deleveraging campaign; credit measurement; the property presale bubble; LGFVs; the politics of campaigns; Beijing's option set |

To add a source, upload it to [`china-macro-sources/`](../../../china-macro-sources/) at the repo root and ask Claude to add it to the library. The steps are in that folder's README; Claude's conversion procedure is in `skills/china-macro-library/references/sources.md#adding-a-source`.

## Notes

- Source knowledge bases hold synthesized notes, not source text.
- Source data is historical. The workflows require labeling vintages and pairing frameworks with current data.
