# Third-Party Notices

## LangAlpha

`SKILL.md` and `references/sector-signals.md` incorporate material from the `thesis-tracker` skill in
[ginlix-ai/LangAlpha](https://github.com/ginlix-ai/LangAlpha)
(`plugins/langalpha_research/skills/thesis-tracker/`) at commit 53b81d40,
Copyright 2025 Ginlix AI, licensed under the Apache License, Version 2.0. A
copy of the license is in this repository's `LICENSE`.

LangAlpha's version was itself adapted from this skill, as of
anthropics/financial-services-plugins commit 86726dfc.

**Modified files:**

- `SKILL.md`: merged into this skill's existing workflow.
- `references/sector-signals.md`: adapted with minor edits.

**Changes from the LangAlpha version:**

- **Kept from ours.** This skill's step layout and the thesis-definition fields (position, thesis statement, key risks, valuation anchor, exit trigger) are kept, along with the H/M/L conviction field, the scorecard example rows and the notes.
- **Action calls.** Actions use the input-gated call list in `research-conventions` instead of LangAlpha's closed verb vocabulary. Conviction stays a High/Medium/Low word with its reason.
- **Catalysts.** Dated catalysts use `catalyst-calendar`'s date-type and confidence terms. Fuller calendars route to that skill.
- **References.** `.agents/skills/...` path references are replaced with this plugin's skill names. In `sector-signals.md`, the pointer to a LangAlpha-only idea-generation reference is removed, and spelling is changed to US English.
