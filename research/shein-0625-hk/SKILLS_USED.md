# Skills used for the SHEIN (0625.HK) initiation report

| Skill | Where it lives | What it was used for |
|---|---|---|
| `equity-research:initiating-coverage` | `plugins/vertical-plugins/equity-research/skills/initiating-coverage/` | The overall workflow and report format: company research (task 1), financial model (task 2), valuation (task 3), charts (task 4) and report assembly (task 5), plus the page-1 report template. |
| `financial-analysis:xlsx-author` | `plugins/vertical-plugins/financial-analysis/skills/xlsx-author/` | Conventions for the Excel earnings model: formula-driven cells, blue inputs, black formulas, green cross-sheet links, named ranges and a checks tab. |
| `dataviz` | Built into Claude Code | The 35 charts: chart-type choice, the colour palette (checked with its validator script), mark and label styling. |
| `anthropic-skills:docx` | Claude account skill | Building the Word report with docx-js and checking the rendered pages. |
| `humanizer` | `.claude/skills/humanizer/` (from [blader/humanizer](https://github.com/blader/humanizer) v3.1.0) | Editing the report prose to remove AI-writing patterns, without changing any figure. |

The repo's `financial-analysis:dcf-model` and `financial-analysis:3-statement-model` skills were not used; the DCF and three-statement model follow the initiating-coverage task 2 and task 3 references.
