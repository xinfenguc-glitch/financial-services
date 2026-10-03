---
description: Decode a Chinese policy statement, meeting readout, or campaign signal
argument-hint: "[statement text, link, or meeting name and date]"
---

Load the `china-macro-library` skill and follow `references/workflows/policy-read.md`.

If the user provided a statement, analyze it. If they named a meeting, retrieve the readout (and the previous comparable one, for the diff) or ask the user to paste it. Ground the political-economy read in `wright-deleveraging` ch03, ch06 and ch07. Return the workflow's output template.
