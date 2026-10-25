# Third-Party Notices

## LangAlpha

`SKILL.md` incorporates material from the `earnings-preview` skill in
[ginlix-ai/LangAlpha](https://github.com/ginlix-ai/LangAlpha)
(`plugins/langalpha_research/skills/earnings-preview/`) at commit 53b81d40,
Copyright 2025 Ginlix AI, licensed under the Apache License, Version 2.0. A
copy of the license is in this repository's `LICENSE`.

LangAlpha's version was itself adapted from this skill, as of
anthropics/financial-services-plugins commit 86726dfc.

**Modified files:**

- `SKILL.md`: merged into this skill's existing workflow.

**Changes from the LangAlpha version:**

- **Page one.** The one-page preview stays as page one, with the fuller analysis in supporting sections behind it. A one-page-only request delivers page one plus the missing-evidence block. LangAlpha's version instead makes the full note the default and rebuilds a short one on request.
- **Sources.** LangAlpha's MCP tool calls (company overview, prices, filings, float, short data, the yfinance estimate fields, the options chain and snapshot procedure) are replaced with this marketplace's connectors (FactSet, S&P Capital IQ, LSEG, Daloopa, Aiera, MT Newswires). Web search is kept as a labelled fallback for consensus.
- **Options-implied move.** It is described independently of any specific tool, and keeps the expiry-tenor caveat.
- **Kept from ours.** This skill's sector metric pack is kept, along with the scenario table, the catalyst checklist and the notes.
- **References.** `.agents/skills/...` path references are replaced with this plugin's skill names.
