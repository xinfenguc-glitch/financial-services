# Third-Party Notices

## LangAlpha

`SKILL.md` and the five files under `references/` are adapted from the
`research-conventions` skill in
[ginlix-ai/LangAlpha](https://github.com/ginlix-ai/LangAlpha)
(`plugins/langalpha_research/skills/research-conventions/`) at commit
53b81d40, Copyright 2025 Ginlix AI, licensed under the Apache License,
Version 2.0. A copy of the license is in this repository's `LICENSE`.

**Modified files:**

- `SKILL.md`
- `references/evidence.md`
- `references/judgment.md`
- `references/intake.md`
- `references/market-data-rules.md`
- `references/depth.md`

**Changes from the original:**

- **Precedence.** Added an order of precedence: agent guardrails first, then the calling skill's workflow and checkpoints, then these rules on evidence. Removed the rule that let these conventions override a skill's own pauses.
- **Source tiers.** Rewrote them against this marketplace's connectors (FactSet, S&P Capital IQ, LSEG, Daloopa, Morningstar, PitchBook, Moody's, Aiera, MT Newswires, Box, Egnyte) in place of LangAlpha's own MCP tools. Added families for credit and ratings, and for user-supplied documents.
- **Unsourced figures.** Renamed `needs-source` to `unsourced`, printed `[UNSOURCED]` in drafts for review to match the agents' guardrails, and added the review-draft exit to the unsupported-claim rule.
- **Action language.** Replaced the closed action vocabulary and its registered extensions with input-gated calls plus the user's or firm's own rating ladder. Added a sell-side audience mode.
- **Intake.** Replaced LangAlpha's user-tier mandate memory with what the conversation, project instructions, host memory and supplied files establish. Added rules for headless managed-agent runs.
- **NTM.** Allowed a connector's own NTM series with its method named, alongside the sum of four quarterly consensus means.
- **Depth.** Bands and cut order now defer to the calling skill's length and required content.
- **References.** Replaced LangAlpha path, skill and tool references with this plugin's skills.
