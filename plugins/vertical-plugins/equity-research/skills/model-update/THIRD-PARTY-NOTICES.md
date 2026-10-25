# Third-Party Notices

## LangAlpha

`SKILL.md` incorporates material from the `model-update` skill in
[ginlix-ai/LangAlpha](https://github.com/ginlix-ai/LangAlpha)
(`plugins/langalpha_research/skills/model-update/`) at commit 53b81d40,
Copyright 2025 Ginlix AI, licensed under the Apache License, Version 2.0. A
copy of the license is in this repository's `LICENSE`.

LangAlpha's version was itself adapted from this skill, as of
anthropics/financial-services-plugins commit 86726dfc.

**Modified files:**

- `SKILL.md`: merged into this skill's existing workflow.

**Changes from the LangAlpha version:**

- **Running modes.** Three modes are added: live workbook, file on disk, and read-only worker (for the earnings-reviewer model-updater, which returns the mapping and variance tables instead of writing).
- **Tooling.** LangAlpha's xlsx scripts (`insert.py`, `recalc.py`, `audit.py`) are replaced with Excel itself, `xlsx-author` conventions, `audit-xls`, and an explicit disclosure when a file could not be recalculated.
- **Checkpoint.** The mapping-table review stop now holds interactively. Headless runs write only to the versioned copy.
- **Kept from ours.** This skill's variance, estimate-change and valuation tables are kept, now with consensus and delta columns. So are the rating and price-target step and the notes.
- **Routing.** Rebuilds route to `3-statement-model`, `dcf-model`, or a model-builder handoff. `.agents/skills/...` path references are replaced with this plugin's skill names.
