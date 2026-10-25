# Third-Party Notices

## LangAlpha

`SKILL.md` and `references/event-lenses.md` incorporate material from the
`catalyst-calendar` skill in
[ginlix-ai/LangAlpha](https://github.com/ginlix-ai/LangAlpha)
(`plugins/langalpha_research/skills/catalyst-calendar/`) at commit 53b81d40,
Copyright 2025 Ginlix AI, licensed under the Apache License, Version 2.0. A
copy of the license is in this repository's `LICENSE`.

LangAlpha's version was itself adapted from this skill, as of
anthropics/financial-services-plugins commit 86726dfc.

**Modified files:**

- `SKILL.md`: merged into this skill's existing workflow.
- `references/event-lenses.md`: adapted with minor edits.

**Changes from the LangAlpha version:**

- **Structure and content.** Kept this skill's step layout, weekly-preview template, positioning column, color coding and notes.
- **Defaults.** The default horizon is the next two weeks, matching `/catalysts`, in place of a rolling ninety days.
- **Sources.** Replaced LangAlpha's MCP tool calls with this marketplace's connectors (FactSet, S&P Capital IQ, LSEG, Aiera, MT Newswires) and web search.
- **Escalators.** Added a pre-announcement escalator.
- **Output.** The workbook is built with live Excel tools or `xlsx-author` (headless), in place of LangAlpha's xlsx skill and recalculation script. Added an optional calendar export restricted to `hard` dates.
- **Externally clean rule.** Narrowed it to *unpublished* estimates and targets.
- **References.** Replaced `.agents/skills/...` path references with references to `research-conventions`.
