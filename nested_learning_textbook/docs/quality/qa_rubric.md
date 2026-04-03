# QA Rubric
**Version**: 1.0 | **Date**: 2026-04-03

This rubric defines what "done" means for each dimension of this project.  
Run this checklist after each major phase.

---

## Dimension 1: Repo Legibility

| Check | Pass Criteria | Tool |
|---|---|---|
| `AGENTS.md` exists and is < 150 lines | File must be present and actionable | Manual |
| `docs/index.md` navigates to all key docs | All links resolve | `check_book_structure.py` |
| Handoff is up to date | `docs/handoffs/latest_handoff.md` matches actual state | Manual |
| No orphan planning docs at root | Root-level `.md` planning files are stubs or redirects | Manual |

---

## Dimension 2: Harness Completeness

| Check | Pass Criteria | Tool |
|---|---|---|
| All phase plans exist | `docs/exec-plans/active/*.md` for all phases | Manual |
| Makefile targets work | `make check` exits 0 | `make check` |
| QA rubric exists | This file | Manual |
| Claim honesty policy exists | `docs/quality/claim_honesty_policy.md` | Manual |

---

## Dimension 3: Literature Integrity

| Check | Pass Criteria | Tool |
|---|---|---|
| All 24 seed papers in manifest | 24 rows in CSV | `validate_manifest.py` |
| Status codes correct | No paper marked `source_and_merged` without actual files | `validate_manifest.py` |
| All claimed `merged_paper.tex` exist | File present on disk | `validate_manifest.py` |
| All notes files exist | 24 `.md` files in `notes/papers/` | `validate_manifest.py` |
| No empty paper folders | Folders have at least one `.tex` or download reference | Manual |

---

## Dimension 4: Manifest Correctness

| Check | Pass Criteria | Tool |
|---|---|---|
| No absolute paths in CSV | `grep "/Users/" papers_manifest.csv` returns 0 lines | `check_absolute_paths.py` |
| All local_folder paths are relative | Paths start with `nested_learning_textbook/` | `validate_manifest.py` |
| `last_verified` field populated | All rows have a date | Manual |

---

## Dimension 5: Absolute-Path Hygiene

| Check | Pass Criteria | Tool |
|---|---|---|
| No `/Users/` in scripts | 0 matches | `check_absolute_paths.py` |
| No `/Users/` in manifests | 0 matches | `check_absolute_paths.py` |
| No `/Users/` in docs | 0 matches | `check_absolute_paths.py` |
| `literature_engineer.py` flagged | Legacy; OK to have paths only in this file | Manual note |

---

## Dimension 6: Bibliography Health

| Check | Pass Criteria | Tool |
|---|---|---|
| `library.bib` exists | File present | Manual |
| All 24 papers have entries | 24 `@article` or `@inproceedings` entries | Manual / biber |
| No duplicate keys | biber reports no `duplicate entry` warnings | `make book` |
| Citation keys used in chapters match bib | All `\cite{key}` resolve | `make book` |

---

## Dimension 7: LaTeX Build Health

| Check | Pass Criteria | Tool |
|---|---|---|
| `book/main.tex` exists | File present | Manual |
| All chapters included in `main.tex` | `\input{chapters/NN_...}` for all 11 chapters | `check_book_structure.py` |
| `latexmk -xelatex main.tex` exits 0 | PDF generated, no fatal errors | `make book` |
| `build/main.pdf` present after build | File exists | Manual |

---

## Dimension 8: Pedagogical Specificity

| Check | Pass Criteria | Tool |
|---|---|---|
| Each chapter has core question stated | `\section{本章想回答什么问题}` present | `check_book_structure.py` |
| Each chapter has at least 1 formula | `\begin{equation}` or `$$` present | Manual |
| Each chapter has worked example | `\begin{example}` or equivalent section | Manual |
| Each chapter has exercises | `\section{练习题}` or equivalent | Manual |
| Each chapter has misconceptions | `\section{常见误解}` | Manual |
| Toy problem appears (at least in reference) | "在线线性回归" or "键值检索" mentioned | Manual |

---

## Dimension 9: Claim Honesty

| Check | Pass Criteria | Tool |
|---|---|---|
| No speculative claims in theorem environments | Theorems only for mathematically rigorous statements | Manual |
| ICL = GD framed as interpretation | Must say "一种视角" or equivalent, not "已证明等价于" | Manual |
| NL framed as research agenda | Must not present NL as "社区共识" | Manual |
| "共识层" and "解释层" distinguished in chapters | At least Ch 6 and Ch 11 have explicit distinction | Manual |

---

## Dimension 10: Chapter Completeness

For each of the 11 chapters, the following must be present:

| Section | Required |
|---|---|
| 本章想回答什么问题 | ✅ Required |
| 最小例子 | ✅ Required |
| 直觉解释 | ✅ Required |
| 数学形式化 | ✅ Required (at least one equation) |
| 代表论文 | ✅ Required (at least one \cite) |
| 和前后章节的关系 | ✅ Required |
| Lab / 实验 | ✅ Required |
| 常见误解 | ✅ Required |
| 练习题 | ✅ Required (at least 2) |
| 本章小结 | ✅ Required |

---

## Dimension 11: Textbook Teaching Quality

| Check | Pass Criteria | Tool |
|---|---|---|
| Self-containedness | Readers understand mechanisms without reading papers. No "details omitted" cop-outs. | `check_chapter_depth.py` + Manual |
| Explanatory sufficiency | Concepts are actually explained, not just namedropping. Prose is dense and explanatory. | `check_chapter_depth.py` + Manual |
| Prerequisite leakage | No assuming reader knows advanced topics secretly. Definitions provided when needed. | Manual |
| Notation hygiene | Every symbol is explained upon first usage. | Manual |
| Worked-example completeness | Every key equation has a numeric or geometric example. | `check_chapter_completeness.py` |
| Derivation sufficiency | Equations have clear intuitions/derivations, not just dumped. | Manual |
| Cross-chapter continuity | Clear structural bridges ("Why this chapter exists" and "Where it leads"). | `check_chapter_completeness.py` |
| Consensus vs interpretation discipline | Strict boundaries between mechanism consensus and interpretive agendas. | Manual |
| Chapter depth | Prose word count > 2500/3500 depending on importance. Not an outline. | `check_chapter_depth.py` |
| Appendix support | Math/opt appendices cover linear algebra, gradients, RLS, MAML basics. | Manual |

---

## Dimension 12: Neuroscience Analogy Discipline

| Check | Pass Criteria | Tool |
|---|---|---|
| Analogy Usefulness | The analogy clarifies the math/mechanism rather than obfuscating it. | Manual |
| Strict Separation | Both `\begin{neurosciencebox}` and `\begin{analogyboundarybox}` exist. | `check_chapter_completeness.py` |
| Mechanism != Metaphor | The text never claims "models are brains". Limitations explicitly listed. | Manual |
| Frontmatter Guide | `frontmatter/how_to_use_neuroscience_analogies.tex` is present. | Manual |
| Glossary Coverage | ML terms mapping to bio terms are defined to prevent confusion. | Manual |

---

## Overall Pass/Fail

**Minimum to call a phase "done"**: All ✅ checks in dimensions 1–5 must pass.  
**To call book "draft complete"**: All dimensions 1–12 must pass mechanically and manually.
