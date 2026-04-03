# Reconciled Repository State
**Generated**: 2026-04-03
**Purpose**: Single source of truth resolving conflicting claims across legacy status documents. Authoritative baseline for Phase 1.

---

## 1. Actual Current Tree & Canonical Designations

The repository has undergone a partial migration. The true state of the filesystem is as follows:

| Component | Actual Location | Canonical/Legacy Status |
|---|---|---|
| Project Root | `/Rest_learning` | Root level is the harness. |
| Textbook Root | `nested_learning_textbook/` | The actual project directory. |
| **LaTeX Book** | `nested_learning_textbook/book/` | **CANONICAL**. This is the active, primary manuscript. Compiled via `main.tex`. |
| **Markdown Drafts** | `nested_learning_textbook/manuscript/` | **LEGACY SOURCE MATERIAL**. v0 drafts. preserved for content seeding ONLY. |
| System of Record | `nested_learning_textbook/docs/` | **CANONICAL**. Authoritative docs (index, design-docs, handoffs, quality rubric). |
| Legacy Planning | `nested_learning_textbook/*.md` | **LEGACY/STALE**. e.g., `book_plan.md`, `final_report.md`, `README.md` (inside `nested_learning_textbook/`). Superseded by `docs/` and root README. |
| Literature Pipeline | `scripts/corpus_pipeline.py` | **CANONICAL**. The incremental pipeline. |
| Legacy Script | `scripts/literature_engineer.py` | **LEGACY**. Do not use. |
| Literature Manifests | `manifests/papers_manifest.csv` | **CANONICAL**. Uses repo-relative paths. |
| Literature Corpus | `papers/` | Contains 22 downloaded and merged papers. |
| Paper Notes | `notes/papers/` | All 24 files are generic stubs. Needs actual notes. |

## 2. Doc Disagreements and Contradictions Resolved

There were several conflicting narratives in the repo. This document formally dictates the *truth* which will be enforced via cleanup:

### Contradiction A: What is the main manuscript?
- **False Claim:** `nested_learning_textbook/README.md` and `final_report.md` claim `manuscript/` contains the manuscript and outputs.
- **True State:** `book/` is the canonical LaTeX manuscript. `manuscript/` is v0 legacy.
- **Resolution:** `nested_learning_textbook/README.md` and `final_report.md` will be stubbed/demoted.

### Contradiction B: What is the literature script?
- **False Claim:** `nested_learning_textbook/README.md` claims `scripts/literature_engineer.py` is the pipeline.
- **True State:** `scripts/corpus_pipeline.py` is the active, incremental script with repo-relative paths. `literature_engineer.py` has hardcoded absolute paths and is deprecated.
- **Resolution:** `nested_learning_textbook/README.md` will be corrected.

### Contradiction C: Chapter Completion Status
- **False Claim:** `docs/project_state/current_repo_audit.md` (from older scan) claims the 11 LaTeX chapters in `book/chapters/` are mere "scaffolded stubs" needing content migration.
- **True State:** As per `latest_handoff.md` and manual file inspection:
    - `09_titans_and_multi_timescale_memory.tex` is a full rewrite with math and analogy boxes.
    - `04_fast_weights_memory_and_timescales.tex` has been expanded and includes neuroscience boxes.
    - `08_ttt_layers_hidden_state_as_learner.tex` has been expanded and includes neuroscience boxes.
    - The other chapters (01, 02, 03, 05, 06, 07, 10, 11) are indeed varying degrees of stubs or migrated raw text lacking the full B11-B26 standard.
- **Resolution:** `current_repo_audit.md` will be updated to reflect that Ch04, 08, 09 are substantially advanced.

## 3. Actually Complete vs. Claimed Complete

### Complete
- **Corpus Files**: 22 papers have TeX sources and `merged_paper.tex`. 1 is PDF-only. 1 is missing.
- **LaTeX Infrastructure**: `book/main.tex`, `preamble.tex`, `latexmkrc` are configured.
- **Harness Infrastructure**: `docs/` is structured correctly. `AGENTS.md` and `Makefile` correctly point to current systems.

### Claimed Complete but Actually INCOMPLETE
- **LaTeX Chapters**: Not all are scaffolded stubs, but not all are complete either. They require extensive content deepening, math rigorousness, and neuroscience rollout according to the B11-B26 `pedagogy_principles.md`.
- **Paper Notes (`notes/papers/*.md`)**: Claimed to exist, but all 24 are generic placeholder stubs. They must be rewritten.
- **Build Health**: Claimed as possible but untested on a live pipeline with recent changes.
- **Book completion**: The LaTeX book currently contains duplicate chapter files (`01_introduction_and_terminologies.tex` vs `01_terminology_and_map.tex` and `09_titans_and_multi_timescale_memory.tex` vs `09_titans_multi_timescale_memory.tex`) that must be consolidated.

---
**Next Action**: Demote/modify stale documents (`nested_learning_textbook/README.md`, `final_report.md`, `current_repo_audit.md`) to align with this re-established truth. Then consolidate the book structure.
