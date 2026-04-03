# Repo Gaps Analysis
**Generated**: 2026-04-03

This document lists specific gaps between the current repo state and the fully harness-managed LaTeX textbook target.

## Gap 1: LaTeX Chapter Content (CRITICAL)
- **Current**: All `book/chapters/*.tex` are scaffolded stubs with section headings
- **Target**: Full prose, worked examples, toy problems, exercises
- **Source**: v0 Markdown in `manuscript/` provides content seed
- **Effort**: High (main authoring task)

## Gap 2: Per-Paper Notes (HIGH)
- **Current**: 24 stub files in `notes/papers/` with generic placeholder text
- **Target**: Structured notes with: role in textbook, narrative position, 3 key points for undergrads, consensus vs. interpretation delineation
- **Effort**: Medium

## Gap 3: Missing Paper — Optimization as a Model (MEDIUM)
- **Current**: No local folder for `optimization_as_a_model_for_few_shot_learning`
- **Target**: PDF at minimum; add to manifest as `pdf_only`
- **Action**: `corpus_pipeline.py` can download PDF with `--force-pdf`

## Gap 4: In-Context Learning Induction Heads — No TeX Source (MEDIUM)
- **Current**: PDF only in downloads; `papers/in_context_learning_and_induction_heads/` folder is empty (was created as dir stub for extraction that failed)
- **Target**: Mark as `pdf_only` in manifest; remove empty dir or add PDF reference
- **Action**: Manifest already corrected; clean empty dir if present

## Gap 5: Bibliography Completeness (MEDIUM)
- **Current**: `library.bib` has 24 entries from seed data
- **Target**: All entries should have correct author/year/venue metadata
- **Action**: Verify against arXiv metadata; some entries may need manual correction

## Gap 6: LaTeX Build Not Verified (HIGH)
- **Current**: `book/main.tex` compiles structurally (packages and structure valid)
- **Target**: Full compilation to PDF with no errors
- **Blocker**: Requires XeLaTeX + CJK fonts on the build machine

## Gap 7: Root-Level Legacy Planning Docs (LOW)
- **Current**: `book_plan.md`, `chapter_map.md`, etc. still at textbook root as separate files
- **Target**: Replace with stub redirects pointing to `docs/`
- **Action**: Write stub files with pointer to canonical location in docs/

## Gap 8: Chapter-to-Papers Mapping (LOW)
- **Current**: `docs/references/chapter_to_papers_map.md` is a planning artifact
- **Target**: Should be verifiable against actual `\cite{}` keys in chapter .tex files
- **Action**: After chapter expansion, script can extract citations and verify
