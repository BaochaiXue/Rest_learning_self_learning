# Reconciled Repository State
**Generated**: 2026-04-03  
**Purpose**: Single source of truth for the current state of the entire repository. All other status documents must align with this one.

---

## 1. Canonical vs. Legacy Designations

| Component | Location | Status |
|---|---|---|
| **LaTeX Book** | `book/` | **CANONICAL** — compiled via `main.tex`, verified building to PDF |
| **Markdown Drafts** | `manuscript/` | **LEGACY** — v0 source material only, do not modify |
| **System of Record** | `docs/` | **CANONICAL** |
| **Literature Pipeline** | `scripts/corpus_pipeline.py` | **CANONICAL** (incremental, repo-relative) |
| **Legacy Pipeline** | `scripts/literature_engineer.py` | **LEGACY** — hardcoded absolute paths, do not run |
| **Manifest** | `manifests/papers_manifest.csv` | **CANONICAL** — repo-relative paths, validated |
| **Literature Corpus** | `papers/` | 22 papers with `merged_paper.tex`, 1 PDF-only, 1 missing |
| **Paper Notes** | `notes/papers/*.md` | **STALE** — all 24 are generic stubs needing rewrite |
| **Root Planning Docs** | `nested_learning_textbook/*.md` | **LEGACY** — `book_plan.md`, `final_report.md`, etc. superseded by `docs/` |
| **Writing Policy** | `docs/design-docs/pedagogy_principles.md` | **CANONICAL** — B11–B26 standard |
| **Reader Guide** | `book/frontmatter/how_to_use_neuroscience_analogies.tex` | **CANONICAL** — v2.0 |

---

## 2. Build Health (Verified 2026-04-03)

| Check | Status |
|---|---|
| `make check` (audit scripts) | ✅ Pass — all scripts exit 0, 8 content warnings only |
| `make book` (XeLaTeX) | ✅ Pass — 120+ pages, PDF generated |
| `book/build/main.pdf` | ✅ Exists (1.18 MB) |
| All `\cite{}` keys resolve | ✅ Fixed — 12 alias entries added to `library.bib` |
| Absolute paths in project code | ✅ Clean — only in downloaded paper sources (exempt) |

---

## 3. Chapter Quality Assessment (Verified by Line Count + Manual Inspection)

| Chapter | Lines | Neuroscience Boxes | Quality Tier |
|---|---|---|---|
| Ch01 — Introduction | 197 | ❌ Missing | Draft — needs boxes + expansion |
| Ch02 — Why Test-Time Learning | 154 | ❌ Missing | Draft — thinnest chapter, needs major expansion |
| Ch03 — Bilevel/Meta-Learning | 485 | ❌ Missing | **Strong** — math complete, needs boxes only |
| Ch04 — Fast Weights | 576 | ✅ Present | **Textbook-grade** |
| Ch05 — Attention/Linear Attention | 466 | ❌ Missing | **Strong** — math complete, needs boxes only |
| Ch06 — ICL | 219 | ❌ Missing | Draft — needs boxes + some expansion |
| Ch07 — Learning to TTT | 177 | ❌ Missing | Draft — needs boxes + expansion |
| Ch08 — TTT Layers | 224 | ✅ Present | Substantial draft with boxes |
| Ch09 — Titans | 546 | ✅ Present | **Textbook-grade** — reference chapter |
| Ch10 — Test-Time Regression | 170 | ❌ Missing | Draft — needs boxes + major expansion |
| Ch11 — Nested Learning | 648 | ✅ Present | **Textbook-grade** — rewritten 2026-04-03 |

### Priority for Next Work
1. **Ch02** (154 lines) — foundation chapter, needs formal TTT 2020 treatment
2. **Ch10** (170 lines) — critical bridge chapter to Ch11
3. **Ch07** (177 lines) — bridge from ICL to TTT Layers
4. **Ch03, Ch05** — already strong, only need neuroscience boxes

---

## 4. Literature Layer

| Asset | Count | Status |
|---|---|---|
| Papers with TeX source + `merged_paper.tex` | 22 | ✅ |
| Papers PDF-only | 1 | Santoro ICML 2016 |
| Papers missing | 1 | Optimization as Model for Few-Shot Learning |
| BibTeX entries in `library.bib` | 25 + 12 aliases | ✅ All citations resolve |
| Per-paper notes | 24 | ⚠️ All generic stubs — need rewrite |

---

## 5. What is NOT a Bug (Clarifications)

1. **No duplicate chapter files exist** — each chapter has exactly 1 `.tex` file in `book/chapters/`. The manuscript `.md` files have different filenames (e.g., `01_terminology_and_map.md` vs. LaTeX `01_introduction_and_terminologies.tex`) — this is correct, not a conflict.

2. **Absolute paths in `papers/` subdirectories** — these are inside original author TeX/bib source files. They are exempt from hygiene checks.

3. **`literature_engineer.py` has absolute paths** — this is a deprecated legacy script. Documented and exempt.

---

## 6. Remaining Work

### Critical Path
1. Add neuroscience + analogy boundary boxes to Ch01, 02, 03, 05, 06, 07, 10
2. Deepen Ch02, Ch07, Ch10 from draft quality to textbook grade
3. Rewrite paper notes from stubs to useful notes
4. Expand appendices (especially `appendix_math.tex`)

### Already Complete
- Build infrastructure (Makefile, latexmk, preamble, bibliography)
- Harness docs (AGENTS.md, ARCHITECTURE.md, all quality/exec-plan docs)
- Reference chapter (Ch09) and writing policy (pedagogy_principles.md)
- Multiple textbook-grade chapters (Ch03, Ch04, Ch05, Ch09, Ch11)
