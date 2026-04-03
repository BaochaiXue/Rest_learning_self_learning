#!/usr/bin/env python3
"""
check_absolute_paths.py — Scan repo for hardcoded absolute paths.
Usage: python3 scripts/check_absolute_paths.py

Scans all .py, .md, .tex, .csv, .bib files for /Users/, /home/, C:\\ patterns.
Exempts: scripts/literature_engineer.py (known legacy file).
"""
import os, sys, pathlib, re

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent  # Rest_learning/
NLT_ROOT = REPO_ROOT / "nested_learning_textbook"

EXEMPT_FILES = {
    NLT_ROOT / "scripts" / "literature_engineer.py",
}

SCAN_EXTS = {".py", ".md", ".tex", ".csv", ".bib", ".txt"}
ABS_PATH_PATTERNS = [
    re.compile(r"/Users/[A-Za-z]"),
    re.compile(r"/home/[A-Za-z]"),
    re.compile(r"C:\\\\[A-Za-z]"),
    re.compile(r"/root/[A-Za-z]"),
]

hits = []

for root, dirs, files in os.walk(NLT_ROOT):
    # skip .git and build directories
    dirs[:] = [d for d in dirs if d not in {".git", "build", "__pycache__"}]
    for fname in files:
        fpath = pathlib.Path(root) / fname
        if fpath.suffix not in SCAN_EXTS:
            continue
        if fpath in EXEMPT_FILES:
            continue
        try:
            text = fpath.read_text(encoding="utf-8", errors="ignore")
            for lineno, line in enumerate(text.splitlines(), 1):
                for pat in ABS_PATH_PATTERNS:
                    if pat.search(line):
                        rel = fpath.relative_to(REPO_ROOT)
                        hits.append((str(rel), lineno, line.strip()))
                        break
        except Exception as e:
            pass

print(f"Scanning for absolute paths in {NLT_ROOT}...")
print(f"(Exempt: {len(EXEMPT_FILES)} legacy file(s))")
print()

if hits:
    print(f"FOUND {len(hits)} absolute path occurrence(s):")
    for rel, lineno, line in hits:
        print(f"  {rel}:{lineno}: {line[:120]}")
    sys.exit(1)
else:
    print("✅ No absolute paths found (outside exempted legacy files).")
