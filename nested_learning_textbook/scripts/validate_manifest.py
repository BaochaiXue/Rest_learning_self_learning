#!/usr/bin/env python3
"""
validate_manifest.py — Check papers_manifest.csv against the real filesystem.
Usage: python3 scripts/validate_manifest.py [--fix]

All paths in the manifest must be repo-relative (relative to the git repo root).
This script resolves them to absolute paths using the script's own location.
"""
import csv, os, sys, pathlib

# Resolve repo root = parent of nested_learning_textbook/
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent  # Rest_learning/
NLT_ROOT = REPO_ROOT / "nested_learning_textbook"
MANIFEST = NLT_ROOT / "manifests" / "papers_manifest.csv"

errors = []
warnings = []
ok_count = 0

def check(condition, msg, level="error"):
    if not condition:
        if level == "error":
            errors.append(msg)
        else:
            warnings.append(msg)

with open(MANIFEST, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Validating {len(rows)} manifest entries against {REPO_ROOT}...")

for row in rows:
    slug = row["slug"]
    folder_rel = row["local_folder"]
    merged_rel = row["merged_tex"]
    note_rel = row["note_path"]
    status = row["status"]

    # Check for absolute paths
    for field in ["local_folder", "note_path"]:
        val = row[field]
        if val and (val.startswith("/") or val.startswith("C:\\")):
            errors.append(f"[{slug}] {field} is an absolute path: {val!r}")

    # If folder should exist, check it
    if folder_rel:
        folder_abs = REPO_ROOT / folder_rel
        check(folder_abs.exists(), f"[{slug}] local_folder not found: {folder_rel}")

    # If merged_tex claimed, check it
    if merged_rel and folder_rel:
        merged_abs = REPO_ROOT / folder_rel / merged_rel
        check(merged_abs.exists(), f"[{slug}] merged_tex not found: {folder_rel}/{merged_rel}")

    # Note file
    if note_rel:
        note_abs = REPO_ROOT / note_rel
        check(note_abs.exists(), f"[{slug}] note_path not found: {note_rel}", level="warning")

    # Status vs reality
    has_folder = folder_rel and (REPO_ROOT / folder_rel).exists()
    has_merged = has_folder and merged_rel and (REPO_ROOT / folder_rel / merged_rel).exists()
    if status == "source_and_merged" and not has_merged:
        errors.append(f"[{slug}] status=source_and_merged but merged_paper.tex missing")
    if status == "missing" and has_folder:
        warnings.append(f"[{slug}] status=missing but folder exists — consider updating status")

    if not errors:
        ok_count += 1

print(f"\n{'='*60}")
if errors:
    print(f"ERRORS ({len(errors)}):")
    for e in errors: print(f"  ✗ {e}")
if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings: print(f"  ⚠ {w}")
if not errors and not warnings:
    print(f"✅ All {len(rows)} manifest entries validated successfully.")
elif not errors:
    print(f"✅ No errors. {len(warnings)} warning(s).")
else:
    print(f"\n✗ {len(errors)} error(s) found.")
    sys.exit(1)
