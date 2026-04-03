# ARCHITECTURE.md — Information Architecture

## Repository Overview

```
Rest_learning/                        ← git repo root
├── AGENTS.md                         ← agent navigation map (read first)
├── ARCHITECTURE.md                   ← this file
├── README.md                         ← human-readable overview
├── Makefile                          ← task runner
└── nested_learning_textbook/         ← project root
    ├── book/                         ← CANONICAL LaTeX manuscript
    ├── docs/                         ← SYSTEM OF RECORD (design, plans, QA)
    ├── manuscript/                   ← LEGACY v0 Markdown draft (source material)
    ├── papers/                       ← literature corpus (one folder per paper)
    ├── manifests/                    ← ground truth of corpus state
    ├── notes/papers/                 ← per-paper reading notes
    ├── scripts/                      ← automation tools
    └── downloads/                    ← overflow PDFs without public TeX source
```

## Key Boundaries

### Legacy vs. Canonical

| Asset | Location | Role |
|---|---|---|
| v0 Markdown drafts | `manuscript/*.md` | Source material; do not delete or treat as canonical |
| Canonical book | `book/` | LaTeX source; single source of truth for published book |
| Planning docs | `docs/design-docs/` | Design decisions; supersede root-level `.md` planning files |

### Why Markdown → LaTeX migration?

The initial v0 was written quickly in Markdown. Markdown lacks:
- Fine-grained theorem/definition/remark environments
- Proper cross-referencing between chapters
- Bibliography integration with citations
- Index and glossary
- Consistent formatting for a professional textbook

`ctexbook` + `xelatex` is the canonical stack because:
1. Native CTeX support for Chinese typesetting
2. Full LaTeX ecosystem for math, tables, algorithms
3. `latexmk` for reproducible builds
4. No dependency on private fonts (uses system CJK fonts)

### Why Preserve Markdown?

The v0 Markdown drafts contain substantial pedagogical content written by a prior agent.  
They are the **seed material** for the LaTeX chapters — not the final form.  
Do NOT delete them; use them as reference when expanding chapter content.

## Literature Pipeline Architecture

```
papers_def (seed definitions)
    ↓
scripts/corpus_pipeline.py
    ↓
papers/{slug}/              ← extracted TeX source
    merged_paper.tex        ← single-file merged source
    *.tex (original)
    ↓
manifests/papers_manifest.csv   ← ground truth status
    ↓
book/bibliography/library.bib   ← BibTeX entries for citation
    ↓
docs/references/corpus_index.md ← human-readable index
```

### Manifest Fields (canonical)

`title, slug, category, page_url, source_url, pdf_url, local_folder, status, main_tex, merged_tex, note_path, source_type, last_verified`

All paths in the manifest are **repo-relative** (relative to git root).  
Absolute paths are a bug; run `scripts/check_absolute_paths.py` to detect.

## Docs Architecture

`docs/` is the single authoritative system of record for:
- Design decisions (why we did X instead of Y)
- Active and completed execution plans (what work is in progress)
- Handoff artifacts (state at phase boundaries)
- Quality rubrics (what "done" means)
- Generated reports (automated scan outputs)
- Reference indexes (corpus → chapter mapping)

The root-level files (`book_plan.md`, `chapter_map.md`, etc.) are **legacy planning docs**.  
Their content has been absorbed into `docs/design-docs/` equivalents.  
They are kept as stubs for backwards compatibility.

## Build Architecture

```
book/main.tex
  └── \input{preamble.tex}
  └── \input{frontmatter/*.tex}
  └── \input{chapters/*.tex}      ← one file per chapter
  └── \input{appendices/*.tex}
  └── \bibliography{bibliography/library.bib}

Compiled with: xelatex → biber → xelatex → xelatex
Runner: latexmk -xelatex (configured in book/latexmkrc)
Output: book/build/main.pdf
```

## QA Architecture

```
scripts/validate_manifest.py      → manifests health
scripts/check_absolute_paths.py   → path hygiene
scripts/check_book_structure.py   → LaTeX structure  
scripts/corpus_pipeline.py        → literature state
make check                        → runs all above + reports to docs/generated/
```

Quality rubric at `docs/quality/qa_rubric.md`.  
Evaluation reports at `docs/generated/evaluation_report.md`.
