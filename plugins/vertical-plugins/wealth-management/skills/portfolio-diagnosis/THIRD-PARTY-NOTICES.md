# Third-Party Notices

## LangAlpha

`SKILL.md` is adapted from the `portfolio-diagnosis` skill in
[ginlix-ai/LangAlpha](https://github.com/ginlix-ai/LangAlpha)
(`plugins/langalpha_research/skills/portfolio-diagnosis/`) at commit 53b81d40,
Copyright 2025 Ginlix AI, licensed under the Apache License, Version 2.0. A
copy of the license is in this repository's `LICENSE`.

**Modified files:**

- `SKILL.md`

**Changes from the original:**

- **Audience.** The skill is recast from a retail self-check into an advisor's diagnosis of a client portfolio.
- **Inputs.** Holdings come from custodian or portfolio-system exports, and the client's IPS and risk profile replace LangAlpha's profile files and system-prompt block.
- **Data.** LangAlpha's yfinance and price-data tool calls and its `execute_code` runtime are replaced with this marketplace's market-data connectors (FactSet, LSEG, Morningstar) and a Python script. The benchmark comes from the IPS first. Fund look-through is added where holdings data exists.
- **Findings.** Adds IPS drift-band and liquidity-need findings, and uses firm risk bands when supplied.
- **Follow-ups.** These route to this plugin's skills (`portfolio-rebalance`, `tax-loss-harvesting`, `client-review`, `investment-proposal`, `financial-plan`, `client-report`).
