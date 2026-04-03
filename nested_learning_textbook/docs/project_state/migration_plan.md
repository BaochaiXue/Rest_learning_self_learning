# Migration Plan
**Generated**: 2026-04-03  
**Strategy**: Non-destructive incremental upgrade

## Principles

1. **Preserve everything**: No existing file is deleted without replacement
2. **Upgrade in place**: Existing directory structure is extended, not replaced
3. **Repo-relative always**: All new paths use `nested_learning_textbook/...` notation
4. **LaTeX is new canonical**: `book/` is the target; `manuscript/` is preserved as seed

## Phase Status

| Phase | Name | Status |
|---|---|---|
| 0 | Real Repo Audit | ✅ Complete |
| 1 | Harness Scaffold | ✅ Complete |
| 2 | Corpus Stabilization | ✅ Complete (manifest rebuilt, paths fixed) |
| 3 | LaTeX Book Scaffold | ✅ Complete (structure + preamble + all chapters stubbed) |
| 4 | Content Migration | 🔄 In Progress (stubs ready, content expansion needed) |
| 5 | Chapter Expansion | ⏳ Pending |
| 6 | QA Pass | ⏳ Pending |
| 7 | Handoff Update | ⏳ Pending |

## What Was Done (Phases 0–3)

### Phase 0: Audit
- Scanned real filesystem; documented actual state vs. expected
- Identified: 22 papers with TeX, 1 misnamed file, 1 missing paper, absolute paths in manifest + script

### Phase 1: Harness Scaffold
- Created `AGENTS.md`, `ARCHITECTURE.md`, `README.md`, `Makefile`, `.gitignore` at repo root
- Created full `docs/` hierarchy with index, project_state, design-docs, exec-plans, handoffs, quality, decisions, references, generated
- Created QA rubric, claim honesty policy, hygiene policy
- Created 4 stub check/pipeline scripts in `scripts/`

### Phase 2: Corpus Stabilization
- Fixed mislabeled PDF (`in_context_learning_and_induction_heads.tar.gz` → `.pdf`)
- Rebuilt `manifests/papers_manifest.csv` with repo-relative paths and correct status codes
- Superseded `scripts/literature_engineer.py` with `scripts/corpus_pipeline.py`
- `in_context_learning_and_induction_heads` folder: has merged_paper.tex (was already extracted from the earlier session, confirmed by audit)

### Phase 3: LaTeX Scaffold
- Created `book/` with `main.tex`, `preamble.tex`, `latexmkrc`
- Scaffolded all 11 chapters as `.tex` files with section templates
- Created frontmatter (preface + how to read)
- Created appendices (math, labs, glossary)
- Generated `book/bibliography/library.bib` with 24 entries

## What Remains (Phases 4–7)

### Phase 4: Content Migration (next priority)
For each chapter `.tex` file, read the corresponding `manuscript/*.md` and expand it into proper LaTeX prose, maintaining:
- Chinese prose
- LaTeX theorem/example/remark environments
- `\cite{}` references to `library.bib` keys
- Toy problem linkage

### Phase 5: Chapter Expansion
Full prose expansion beyond the v0 seed material. Each chapter needs:  
- Worked example with explicit math  
- Code lab description  
- Exercises (at least 3 per chapter)  
- Common misconceptions box  

### Phase 6: QA Pass
Run `make check` and fix all failures:  
- Check absolute paths (should be 0)  
- Validate manifest (all status codes accurate)  
- Check book structure (all chapters included in main.tex)  
- Attempt LaTeX compilation  

### Phase 7: Update Handoffs
Update `docs/handoffs/latest_handoff.md` with final status after each pass.

## Migration Rules for Specific Files

| Original File | Action | New Location |
|---|---|---|
| `book_plan.md` | Absorbed | `docs/design-docs/book_scope.md` |
| `chapter_map.md` | Absorbed | `docs/references/chapter_to_papers_map.md` |
| `consensus_vs_interpretation.md` | Absorbed | `docs/quality/claim_honesty_policy.md` |
| `learning_theory_scope.md` | Absorbed | `docs/design-docs/learning_theory_scope.md` |
| `math_prerequisites.md` | Absorbed | `docs/design-docs/math_prerequisites.md` |
| `reading_list.md` | Absorbed | `docs/references/reading_list.md` |
| `final_report.md` | Superseded | `docs/handoffs/latest_handoff.md` |
| `scripts/literature_engineer.py` | Kept as legacy | Superseded by `corpus_pipeline.py` |
| `manuscript/*.md` | Preserved | v0 source material, used as content seed |
