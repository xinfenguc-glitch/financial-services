---
name: china-macro-library
description: "Hub for the China macro library: source registry, policy timeline, key data, and analyst workflows for China's credit cycle, shadow banking, PBOC and regulatory policy signals, property and LGFV/local-government debt, default contagion, and Beijing's policy scenarios (rates, CNY, commodities, trade). Use for any China macro question, to run a China credit pulse, decode a Politburo/PBOC/financial-work-conference statement, map where credit risk sits, or build China policy scenarios; routes to the source knowledge bases (e.g. wright-deleveraging) for depth."
---

<!-- argument-hint: [question, workflow name, or source slug] -->

# China Macro Library

A growing library of China macro knowledge. Each **source** (a book, report or paper) becomes its own knowledge-base skill. This hub holds what applies across sources: workflows, the policy timeline, key data and the routing table.

## How to Use

1. **Answering a question**: check the routing table below, load the source chapter it points to, then answer. Cite the source and chapter, e.g. "(Wright 2023, ch05)".
2. **Running analysis**: follow a workflow in `references/workflows/`:
   - [credit-pulse.md](references/workflows/credit-pulse.md): where China's credit cycle is now
   - [policy-read.md](references/workflows/policy-read.md): decode an official statement or campaign signal
   - [risk-ladder.md](references/workflows/risk-ladder.md): where default and contagion risk sits
   - [scenarios.md](references/workflows/scenarios.md): Beijing's strategic options and their market implications
3. **Context**: [timeline.md](references/timeline.md) (2008 to the present, with sources marked), [key-data.md](references/key-data.md) (baseline figures with vintages), [sources.md](references/sources.md) (the library catalog and how to add a source).

## Library rules

- **Label data vintage.** Source figures are historical. Write "RMB 57 trillion LGFV debt (2021, Wright 2023)", never a bare number presented as current.
- **Pair frameworks with current data.** For live questions, get current data from the user, from a connected data source (the `financial-analysis` connectors such as LSEG, S&P Global or FactSet, or the `lseg` plugin's `macro-rates-monitor`), or from official releases (PBOC, NBS, MoF, NFRA). If none is available, say so and give the framework-based view with the data gaps listed.
- **Keep source claims and your inferences separate.** Mark inferences as yours.
- **Events after a source's publication date** come from [timeline.md](references/timeline.md)'s post-report section (verify before citing) or from fresh research, never from the source skill.
- **Steelman the other camps.** For contested judgments (was deleveraging a success?), present the competing views the sources record.

## Core lens (synthesized from the library's sources)

1. **Credit is the growth model.** Post-2008 growth relied on credit expanding faster than GDP. Once credit growth slowed (2017 onward), so did potential growth. The question is always *who can still borrow, and from whom*. → wright-deleveraging ch02, ch06
2. **Guarantees drive the system.** Implicit state backing of borrowers and lenders creates moral hazard. Breaking a guarantee is how risk gets priced, and also how contagion starts. → wright-deleveraging ch02, ch04, ch06
3. **Risk relocates.** Every squeeze displaces financing, for example from shadow banks to presales to households. Track the substitute channel. → wright-deleveraging ch01, ch05
4. **Contagion runs from the periphery to the core.** P2P lenders, then small banks, local SOEs, trusts, developers, households, and next LGFV bonds and then banks. → wright-deleveraging ch01, ch04
5. **Signals precede policy.** Authoritative-personage articles, Politburo readouts, PBOC report language and work conferences set campaigns. Under centralization, the leader's rhetoric prices the guarantee. → wright-deleveraging ch03, ch06, ch07
6. **The endgame is fiscal and monetary.** Local debt is too large to outgrow, so expect fiscalization, falling rates, PBOC balance-sheet support, CNY depreciation pressure, weaker commodity demand and persistent trade surpluses. → wright-deleveraging ch07

## Routing table

| Topic | Go to |
|---|---|
| Shadow banking: WMPs, trusts, NCDs, P2P, channel business | wright-deleveraging ch02, ch03, ch04 |
| PBOC operations, tightening and easing, money-market rates | wright-deleveraging ch03, ch07 |
| Regulatory toolkit (asset management rules, LMR, MPA, 334 checks) and regulator structure | wright-deleveraging ch03; timeline.md |
| Credit measurement (TSF vs bank assets), credit/GDP | wright-deleveraging ch04, ch06; workflows/credit-pulse.md |
| Property: presales, developers, three red lines, mortgages | wright-deleveraging ch05, ch06, ch07 |
| LGFVs, local fiscal stress, SRBs, land sales, debt swaps | wright-deleveraging ch03, ch05, ch07; timeline.md |
| SOEs vs private sector credit | wright-deleveraging ch05, ch06 |
| Defaults and contagion | wright-deleveraging ch01, ch04; workflows/risk-ladder.md |
| Politics: campaigns, centralization, credibility | wright-deleveraging ch03, ch06, ch07; workflows/policy-read.md |
| Policy scenarios; CNY, rates, commodities, trade | wright-deleveraging ch07; workflows/scenarios.md |
| US–China financial policy (listings, investment flows) | wright-deleveraging ch07 |
| Inflation (CPI/PPI), household income | wright-deleveraging ch02, ch05 |

## Sources in the library

| Slug | Source | Coverage |
|---|---|---|
| `wright-deleveraging` | Logan Wright, *Grasping Shadows: The Politics of China's Deleveraging Campaign* (CSIS, April 2023) | Shadow banking, the 2016–19 deleveraging campaign, the property bubble, LGFVs, policy options to 2023 |

To add a source, see [sources.md](references/sources.md#adding-a-source).
