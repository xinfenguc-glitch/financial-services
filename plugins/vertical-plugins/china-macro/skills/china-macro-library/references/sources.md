# Source Registry

Every source in the library has its own knowledge-base skill under `plugins/vertical-plugins/china-macro/skills/<slug>/`, plus an entry here.

## Catalog

### `wright-deleveraging`
- **Title**: *Grasping Shadows: The Politics of China's Deleveraging Campaign*
- **Author**: Logan Wright (director of China markets research, Rhodium Group)
- **Publisher**: CSIS Trustee Chair in Chinese Business and Economics, April 2023, 101 pp. (© CSIS; this library holds synthesized notes, not the text)
- **Data vintage**: mostly through 2021–22, with some early-2023 references (births, FX reserves, March 2023 work report, new leadership)
- **Source file**: `plugins/The Politics of China's Deleveraging Campaign.pdf` on the `China-Macro` branch (new sources go in `china-macro-sources/`)
- **Files**: `SKILL.md` (frameworks and index), `summary.md` (an 800–1,000 word summary), `chapters/ch01–ch07`, `glossary.md`, `patterns.md`, `cheatsheet.md`
- **Best for**: shadow banking mechanics; the 2016–19 campaign's tools and sequencing; credit measurement; the property presale bubble; LGFV and local-debt dynamics; the politics of campaigns and centralization; Beijing's post-2023 option set
- **Companion work cited**: Wright and Rosen, *Credit and Credibility* (2018); Orlik, *China: The Bubble That Never Pops* (2020)
- **Perspective note**: a US think-tank report and a skeptical-structural view. Chapter 6 records the competing camps (Orlik and the CBIRC on success; Xu Zhong and Xu Gao on overdone; Miller and Balding on "didn't happen").

## Adding a source

0. **Locate**: new files arrive in `china-macro-sources/` at the repo root (the inbox). Check which ones have no catalog entry yet. Read each one in full, and confirm with the user whether it is a new source or an update to an existing slug (if it is an update, merge it into that skill's chapters, glossary and indexes instead of creating a new skill).
1. **Convert**: build a knowledge base in the same shape as `wright-deleveraging/`: `SKILL.md` (frameworks first, under ~4,000 tokens, with chapter and topic indexes), `summary.md`, `chapters/chNN-<slug>.md`, `glossary.md`, `patterns.md`, `cheatsheet.md`. Slug convention: `<author-lastname>-<core-concept>`. Synthesize, never paste raw text.
2. **Place**: `plugins/vertical-plugins/china-macro/skills/<slug>/`.
3. **Register**: add a catalog entry above (title, author, publisher, vintage, source location, files, best for, perspective).
4. **Route**: update the hub `SKILL.md`: add rows or links to the routing table, add the source to "Sources in the library", and fold any new cross-source principle into the core lens with a pointer.
5. **Timeline and data**: add dated events to `timeline.md` and baseline figures to `key-data.md`, tagged with the source slug.
6. **Reconcile**: where sources disagree, note it in the routing table or core lens rather than silently picking one view.
7. **Validate**: run `python3 scripts/check.py` from the repo root.

Candidate sources already in this repo: Ray Dalio's *Principles for Navigating Big Debt Crises* and *The Changing World Order* material (on the `Dalio-sources` branch). The debt-cycle chapters bear directly on China's deleveraging.
