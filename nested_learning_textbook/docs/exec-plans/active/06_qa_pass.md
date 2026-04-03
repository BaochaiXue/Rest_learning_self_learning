# Phase 06: Qa Pass
Status: active

## Goal
Run make check; attempt LaTeX build; fix failures

## Inputs
- Current chapter .tex stubs in `book/chapters/`
- v0 Markdown in `manuscript/`
- Merged paper sources in `papers/*/merged_paper.tex`

## Outputs
- Expanded chapter .tex files
- Compilation report from `make book`
- Updated `docs/handoffs/latest_handoff.md`

## Entry Point
```bash
cd nested_learning_textbook
# Review manuscript/*.md for content seed
# Expand book/chapters/*.tex
make check
make book
```

## Success Criteria
See `docs/quality/qa_rubric.md` Dimensions 8–10.
