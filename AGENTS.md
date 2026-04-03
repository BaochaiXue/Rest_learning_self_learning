# AGENTS.md — Navigation Map

This file is the **entry point for any agent or contributor**.  
Read this first. Do not skip to writing content without reading the authoritative docs first.

## What This Repo Is

A harness-managed, LaTeX-canonical undergraduate textbook on **Inference-Time Learning**,  
tracing the path: TTT (2020) → meta-learning → fast weights → attention → ICL → TTT layers → Titans → Nested Learning.

**Canonical manuscript**: `nested_learning_textbook/book/` (LaTeX, xelatex + ctexbook)  
**Legacy v0 draft**: `nested_learning_textbook/manuscript/` (Markdown, source material only — do not treat as canonical)  
**System of record**: `nested_learning_textbook/docs/` (all design decisions, plans, QA)  
**Literature corpus**: `nested_learning_textbook/papers/` (one folder per paper, with `merged_paper.tex`)  
**Manifests**: `nested_learning_textbook/manifests/papers_manifest.csv` (ground truth of corpus state)

## Before You Start Any Task

1. Read `nested_learning_textbook/docs/index.md` — docs map
2. Read `nested_learning_textbook/docs/project_state/current_repo_audit.md` — real current state
3. Read `nested_learning_textbook/docs/handoffs/latest_handoff.md` — last known progress
4. Read `nested_learning_textbook/docs/exec-plans/active/` — what is planned next
5. Check `nested_learning_textbook/docs/quality/qa_rubric.md` — quality standards

## Fixed Execution Rules

- **Never write absolute paths** (`/Users/...`). Use repo-relative paths everywhere.
- **Never overwrite `manuscript/*.md`** — those are v0 legacy, preserved as source material.
- **Always update `docs/handoffs/latest_handoff.md`** after any substantial work.
- **Canonical manuscript is `book/`** — all new chapter content goes into `book/chapters/*.tex`.
- **Manifest is ground truth** — if `papers_manifest.csv` says a paper is missing, it is missing.
- **Run `make check` before claiming a phase done** (or equivalent scripts).

## Key File Locations

| Purpose | Path |
|---|---|
| Docs index | `nested_learning_textbook/docs/index.md` |
| Book entry point | `nested_learning_textbook/book/main.tex` |
| Manifest (CSV) | `nested_learning_textbook/manifests/papers_manifest.csv` |
| Bibliography | `nested_learning_textbook/book/bibliography/library.bib` |
| Audit report | `nested_learning_textbook/docs/project_state/current_repo_audit.md` |
| Hygiene report | `nested_learning_textbook/docs/generated/repo_hygiene_report.md` |
| Latest handoff | `nested_learning_textbook/docs/handoffs/latest_handoff.md` |
| QA rubric | `nested_learning_textbook/docs/quality/qa_rubric.md` |
| Claim policy | `nested_learning_textbook/docs/quality/claim_honesty_policy.md` |
| Corpus audit | `nested_learning_textbook/docs/generated/corpus_audit.md` |

## Script Entry Points

```bash
# From repo root (nested_learning_textbook/ as working dir):
python3 scripts/validate_manifest.py       # check manifest against filesystem
python3 scripts/check_absolute_paths.py    # scan for hardcoded paths
python3 scripts/check_book_structure.py    # verify LaTeX chapter inclusion
python3 scripts/corpus_pipeline.py         # incremental literature pipeline

# From book/ directory:
latexmk -xelatex main.tex                  # compile book
```

Or use the Makefile at repo root:
```bash
make audit    # run all check scripts
make corpus   # run corpus pipeline
make book     # compile LaTeX
make check    # all checks
make clean    # clean build artifacts
```

## Claim Honesty Policy

See `docs/quality/claim_honesty_policy.md`. Short version:  
- Mechanism-level consensus = can state as fact  
- Interpretive framing (ICL = GD, NL as unifying view) = must frame as "一种视角" / "研究议程"  
- Never state speculative claims as theorems
