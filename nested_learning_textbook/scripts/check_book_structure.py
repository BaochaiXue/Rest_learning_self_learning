#!/usr/bin/env python3
"""
check_book_structure.py — Verify LaTeX book structural integrity.
Usage: python3 scripts/check_book_structure.py

Checks:
1. main.tex exists
2. All expected chapters are \input'd in main.tex
3. All chapter files exist on disk
4. Each chapter has required section headings
"""
import os, sys, pathlib, re

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
BOOK_ROOT = REPO_ROOT / "nested_learning_textbook" / "book"
CHAPTERS_DIR = BOOK_ROOT / "chapters"
MAIN_TEX = BOOK_ROOT / "main.tex"

EXPECTED_CHAPTERS = [
    "01_terminology_and_map.tex",
    "02_why_models_can_learn_at_test_time.tex",
    "03_bilevel_optimization_and_meta_learning.tex",
    "04_fast_weights_memory_and_timescales.tex",
    "05_attention_linear_attention_and_recurrence.tex",
    "06_is_in_context_learning_really_learning.tex",
    "07_learning_to_learn_at_test_time.tex",
    "08_ttt_layers_hidden_state_as_learner.tex",
    "09_titans_multi_timescale_memory.tex",
    "10_test_time_regression_and_unified_views.tex",
    "11_nested_learning.tex",
]

REQUIRED_SECTIONS = [
    "本章想回答什么问题",
    "最小例子",
    "直觉解释",
    "数学形式化",
]

errors = []
warnings = []

print(f"Checking LaTeX book structure in {BOOK_ROOT}...")

# 1. main.tex exists
if not MAIN_TEX.exists():
    errors.append("main.tex not found")
else:
    main_content = MAIN_TEX.read_text(encoding="utf-8", errors="ignore")

    # 2. Each expected chapter is input'd
    for ch in EXPECTED_CHAPTERS:
        ch_stem = ch.replace(".tex", "")
        if ch_stem not in main_content and ch not in main_content:
            errors.append(f"Chapter not included in main.tex: {ch}")

# 3. Each chapter file exists
for ch in EXPECTED_CHAPTERS:
    ch_path = CHAPTERS_DIR / ch
    if not ch_path.exists():
        errors.append(f"Chapter file missing: chapters/{ch}")
    else:
        # 4. Check required sections
        content = ch_path.read_text(encoding="utf-8", errors="ignore")
        for sec in REQUIRED_SECTIONS:
            if sec not in content:
                warnings.append(f"chapters/{ch}: missing section '{sec}'")

print()
if errors:
    print(f"ERRORS ({len(errors)}):")
    for e in errors: print(f"  ✗ {e}")
if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings: print(f"  ⚠ {w}")
if not errors and not warnings:
    print(f"✅ Book structure check passed ({len(EXPECTED_CHAPTERS)} chapters verified).")
elif not errors:
    print(f"✅ No structural errors. {len(warnings)} content warning(s).")
else:
    sys.exit(1)
