# Inference-Time Learning: From TTT to Nested Learning

**A harness-managed LaTeX textbook for CS undergraduates.**

## What This Is

This repository hosts a structured undergraduate textbook tracing the evolution of  
**inference-time / test-time learning** — from Test-Time Training (2020) through  
meta-learning, fast weights, attention, ICL, TTT layers, Titans, and Nested Learning.

Canonical book source: `nested_learning_textbook/book/` (LaTeX)  
Literature corpus: `nested_learning_textbook/papers/` (22 papers with merged TeX)

---

## Current Status

| Component | State |
|---|---|
| Literature corpus | 22 papers with `merged_paper.tex`, 2 PDF-only |
| v0 Markdown drafts | 14 chapters in `manuscript/` (source material) |
| LaTeX book scaffold | `book/` structure created, chapters scaffolded |
| Bibliography | `book/bibliography/library.bib` generated |
| Harness docs | `docs/` system of record established |

See `nested_learning_textbook/docs/project_state/current_repo_audit.md` for details.

---

## Quick Start

### 1. Re-build the literature corpus

```bash
cd nested_learning_textbook
python3 scripts/corpus_pipeline.py
```

### 2. Compile the book

```bash
cd nested_learning_textbook/book
latexmk -xelatex main.tex
# or from repo root:
make book
```

### 3. Run all checks

```bash
make check
```

---

## Navigation

| What | Where |
|---|---|
| Agent nav map | `AGENTS.md` |
| Repo architecture | `ARCHITECTURE.md` |
| Current state | `nested_learning_textbook/docs/project_state/current_repo_audit.md` |
| Latest handoff | `nested_learning_textbook/docs/handoffs/latest_handoff.md` |
| Active plans | `nested_learning_textbook/docs/exec-plans/active/` |
| Quality rubric | `nested_learning_textbook/docs/quality/qa_rubric.md` |
| Paper manifest | `nested_learning_textbook/manifests/papers_manifest.csv` |

---

## Prerequisites

- XeLaTeX (TeX Live 2022+)
- Python 3.9+
- `latexmk`
- System CJK fonts (macOS: built-in Songti/Heiti; Linux: install `fonts-noto-cjk`)

## Textbook Narrative Thread

```
Test-Time Training 2020 (distribution shift)
→ Bilevel optimization / meta-learning (MAML)
→ Fast weights / external memory
→ Attention = associative memory / linear attention = fast weights
→ In-Context Learning as implicit gradient descent
→ Learning to (Learn at Test Time) — the bridge
→ TTT Layers: hidden state as learner
→ Titans: multi-timescale memory
→ Test-time regression / associative memory (unifying view)
→ Nested Learning (final synthesis)
```

**Important**: This book distinguishes two lines of TTT research:
1. *TTT 2020*: update network weights at test time via self-supervised auxiliary tasks
2. *TTT Layers 2024*: hidden state as a learner; no external backprop needed
