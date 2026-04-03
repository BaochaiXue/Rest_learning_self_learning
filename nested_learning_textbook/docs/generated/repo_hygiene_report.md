# Repo Hygiene Report
**Generated**: 2026-04-03  
**Method**: Automated scans via `check_absolute_paths.py` + manual audit

## 1. Absolute Path Scan

**Result**: No repo-owned files contain absolute paths (outside exempted legacy file).

### Findings

| File | Lines | Classification | Action |
|---|---|---|---|
| `scripts/literature_engineer.py` | 2 lines with `/Users/...` | **Exempted legacy file** — known, documented | Keep for reference; do not run |
| `papers/linear_transformers_*/main.tex` | ~10 lines with `/home/kazuki/...` | **Author-commented paths in downloaded paper source** | Acceptable — cannot change paper authors' source |
| `docs/project_state/current_repo_audit.md` | 1 reference to `"/Users/xinjiezhang/..."` in backtick (documentation string) | **Documentation context only** — describes what was fixed | Acceptable |

**All manifest paths**: repo-relative ✅  
**All new scripts**: repo-relative ✅  
**All new doc files**: repo-relative ✅

## 2. Manifest Integrity

**Result**: `validate_manifest.py` exits 0. All 24 entries pass all checks.

- All `source_and_merged` entries (22) have verified `merged_paper.tex` on disk ✅
- All `note_path` entries exist in `notes/papers/` ✅
- No absolute paths in CSV ✅

## 3. Book Structure

**Result**: `check_book_structure.py` exits 0. All 11 chapters included.

3 content warnings (section headings missing in ch8 and ch11):
- `chapters/08_ttt_layers_hidden_state_as_learner.tex`: missing `直觉解释` section heading (content present but under different heading)
- `chapters/11_nested_learning.tex`: missing `直觉解释` and `数学形式化` explicit headings

**Priority**: Low. Content is substantive; heading names need minor adjustment.

## 4. Orphan Files

No orphan files detected. All files belong to active components.

## 5. Empty or Stub Directories

- `book/build/` — empty by design (LaTeX output target)
- `book/figures/` — empty by design (no figures yet)
- `book/tables/` — empty by design (no standalone table files yet)
- `book/styles/` — empty by design (preamble handles styling)

## 6. Legacy Files at textbook Root

The following root-level planning files are now legacy (content absorbed into docs/):
- `book_plan.md` — absorbed into `docs/design-docs/book_scope.md`
- `chapter_map.md` — absorbed into `docs/references/chapter_to_papers_map.md`
- `consensus_vs_interpretation.md` — absorbed into `docs/quality/claim_honesty_policy.md`
- `learning_theory_scope.md` — absorbed into `docs/design-docs/`
- `math_prerequisites.md` — absorbed into `docs/design-docs/`
- `reading_list.md` — absorbed into `docs/references/`
- `final_report.md` — superseded by `docs/handoffs/latest_handoff.md`

**Recommendation**: Write stub redirects to point to canonical locations in docs/. Low priority.

## Overall Hygiene Score

| Dimension | Status |
|---|---|
| Absolute path hygiene | ✅ Pass (2 exempted cases properly documented) |
| Manifest integrity | ✅ Pass (24/24) |
| Book structure | ✅ Pass (0 errors, 3 minor warnings) |
| Orphan files | ✅ None |
| Legacy docs management | ⚠️ In progress (stubs not yet written) |
