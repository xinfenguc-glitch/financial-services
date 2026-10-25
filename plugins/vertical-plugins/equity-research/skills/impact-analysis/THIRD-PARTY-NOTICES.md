# Third-Party Notices

## LangAlpha

`SKILL.md` and `references/channels.md` are adapted from the `impact-analysis` skill in
[ginlix-ai/LangAlpha](https://github.com/ginlix-ai/LangAlpha)
(`plugins/langalpha_research/skills/impact-analysis/`) at commit 53b81d40,
Copyright 2025 Ginlix AI, licensed under the Apache License, Version 2.0. A
copy of the license is in this repository's `LICENSE`.

**Modified files:**

- `SKILL.md`
- `references/channels.md`

**Changes from the original:**

- **Sources.** LangAlpha's MCP tool calls are replaced with this marketplace's connectors: screening, filings, fundamentals, estimate history, prices, and macro series from FactSet, S&P Capital IQ, LSEG or Daloopa, plus web search and fetch for primary rule text.
- **Revisions.** The priced-in test reads revision direction from a connector's consensus history, replacing the rating-change workaround.
- **Intake.** Intake follows `research-conventions` rather than LangAlpha's user-tier mandate memory. Actions use the input-gated call list instead of the closed verb vocabulary.
- **Layout.** The step layout now matches this plugin's skills. Routing to `trade-pitch` and `catalyst-calendar` is added, along with an Important Notes section.
- **References.** In `channels.md`, tool references are replaced with named public series and `.agents/skills/...` paths with this plugin's skill names. Spelling is changed to US English.
