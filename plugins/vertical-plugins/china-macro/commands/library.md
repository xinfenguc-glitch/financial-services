---
description: Browse or query the China macro library (sources, chapters, timeline, key data)
argument-hint: "[question, topic, source slug, or 'summary']"
---

Load the `china-macro-library` skill.

- No argument: list the sources in the library, the four workflows, and the reference files.
- `summary`: return `wright-deleveraging/summary.md` (or a named source's summary).
- A topic or question: use the hub's routing table to load the right source chapter(s), then answer with citations (source and chapter) and data vintages.
- A source slug: load that source's `SKILL.md` and show its chapter index.
