# Third-Party Notices

## LangAlpha

`SKILL.md` and `references/expression.md` are adapted from the `trade-pitch` skill in
[ginlix-ai/LangAlpha](https://github.com/ginlix-ai/LangAlpha)
(`plugins/langalpha_research/skills/trade-pitch/`) at commit 53b81d40,
Copyright 2025 Ginlix AI, licensed under the Apache License, Version 2.0. A
copy of the license is in this repository's `LICENSE`.

**Modified files:**

- `SKILL.md`
- `references/expression.md`

**Changes from the original:**

- **Source analyses.** These map to this marketplace's skills (`dcf-model`, `comps-analysis`, `earnings-analysis`, `initiating-coverage`, `impact-analysis`, `idea-generation`). Intake follows `research-conventions` instead of LangAlpha's mandate memory.
- **Labels.** The `needs-source` label becomes `unsourced`, to match `research-conventions`.
- **Actions and sizing.** Actions use the input-gated call list. Size as a fraction of a loss budget is kept, through a matching exception added to `research-conventions`.
- **Output.** Delivery is a Word document, or slides via `pptx-author` when headless, replacing LangAlpha's docx/pptx skills. Routing to `catalyst-calendar` and an Important Notes section are added.
- **References.** In `expression.md`, `.agents/skills/...` paths are replaced with references to `research-conventions`. Spelling is changed to US English.
