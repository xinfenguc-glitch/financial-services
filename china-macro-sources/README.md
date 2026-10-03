# China Macro Sources (inbox)

Drop source files for the China macro library here: books, reports, papers, speeches or data notes. The library itself lives in `plugins/vertical-plugins/china-macro/`.

This folder sits outside `plugins/` on purpose, so the original files are never shipped inside the plugin. Only Claude's synthesized notes are.

## How to add files

1. On GitHub, open this folder on the branch `claude/awesome-babbage-f70biu`, then choose **Add file → Upload files**. Drag in one or more files and commit. The web upload limit is 25 MB per file; larger files need `git push` from a computer.
2. In a Claude Code session on this repo, say:
   > Add the new files in china-macro-sources/ to the China macro library.

   Optional hints: what to emphasize, and whether a file is a **new source** or an **update** to an existing one (for example a newer edition, or a follow-up report by the same author).

## What Claude does with each file

- Builds a knowledge base at `plugins/vertical-plugins/china-macro/skills/<author-concept>/` with frameworks, chapter notes, glossary, patterns, cheatsheet and an 800–1,000 word summary.
- Registers it in the hub's `references/sources.md` and routing table, and adds its dates and figures to `timeline.md` and `key-data.md`.
- Notes where the new source agrees or disagrees with existing sources.
- Runs `python3 scripts/check.py`, then commits and pushes.

Supported formats: PDF, EPUB, DOCX, HTML, Markdown, TXT, RTF. Scanned PDFs need OCR and take longer.

## Copyright

Third-party books and reports are copyrighted. If this repository is public, committing them here republishes them. Keep the repository private, or keep the originals on a separate unshared branch.
