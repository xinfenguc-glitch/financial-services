# Skills used for the SITC (1308.HK) initiation report

| Skill | Where it lives | What it was used for |
|---|---|---|
| `equity-research:initiating-coverage` | `plugins/vertical-plugins/equity-research/skills/initiating-coverage/` | The overall workflow and report format: company research (task 1), financial model (task 2), valuation (task 3), charts (task 4) and report assembly (task 5), plus the page-1 layout. |
| `equity-research:research-conventions` | `plugins/vertical-plugins/equity-research/skills/research-conventions/` | Evidence labels (reported, management statement, our estimate, our judgement), as-of dates, the priced-in and reverse-DCF tests, the strongest counterargument, falsifiable claims and monitoring items, and the complete probability set for the scenarios. |
| `financial-analysis:xlsx-author` | `plugins/vertical-plugins/financial-analysis/skills/xlsx-author/` | Conventions for the Excel model: formula-driven cells, blue inputs, black formulas, green cross-sheet links, named ranges and a Checks tab. |
| `anthropic-skills:xlsx` | Claude account skill | Building the workbook with openpyxl and recalculating it in LibreOffice to confirm zero formula errors. |
| `dataviz` | Built into Claude Code | The 35 charts: chart-type choice, the colour palette (checked with its validator script), mark and label styling. |
| `anthropic-skills:docx` | Claude account skill | Building the Word report with docx-js, validating the file and checking the rendered pages. |

The repo's `financial-analysis:dcf-model` and `financial-analysis:3-statement-model` skills were not used; the DCF and three-statement model follow the initiating-coverage task 2 and task 3 references.
