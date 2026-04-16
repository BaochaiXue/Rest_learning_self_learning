#!/usr/bin/env python3
"""Lightweight validation for the repo-level research OS."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MD_REQUIRED = {
    "docs/index.md": [
        "# docs/index.md",
        "## Read Order",
        "## Map",
        "## Where To Write What",
    ],
    "docs/design-docs/core-beliefs.md": [
        "# Core Beliefs",
    ],
    "docs/exec-plans/index.md": [
        "# docs/exec-plans/index.md",
        "## Structure",
        "## Rules",
    ],
    "docs/exec-plans/active/index.md": [
        "# docs/exec-plans/active/index.md",
        "## Recommended File Shape",
        "## Update Rule",
    ],
    "docs/exec-plans/completed/index.md": [
        "# docs/exec-plans/completed/index.md",
        "## Move Rule",
    ],
    "docs/handoffs/latest_handoff.md": [
        "# Latest Handoff",
        "## Current State",
        "## What Changed",
        "## Next Recommended Action",
    ],
    "docs/quality/qa_rubric.md": [
        "# QA Rubric",
        "## Criteria",
        "## Practical Threshold",
    ],
    "docs/quality/claim_honesty_policy.md": [
        "# Claim Honesty Policy",
        "## Rules",
    ],
    "docs/reliability.md": [
        "# Reliability",
        "## What Reliability Means Here",
        "## Operating Rules",
        "## Failure Handling",
    ],
    "research/README.md": [
        "# Research State",
        "## Operating Model",
        "## File Roles",
        "## Working Rules",
        "## Resume Sequence",
        "## Handoff Rule",
    ],
    "research/findings.md": [
        "# Findings Log",
        "## Logging Contract",
        "## Entry Template",
    ],
    "research/literature_map.md": [
        "# Literature Map",
        "## Source Contract",
    ],
    "research/claims_registry.md": [
        "# Claims Registry",
        "## Claim Contract",
        "## Status Rules",
    ],
    "research/decision_log.md": [
        "# Decision Log",
        "## Decision Contract",
        "## Entry Template",
    ],
    "research/open_questions.md": [
        "# Open Questions",
        "## Notes",
    ],
    "research/research_plan.template.md": [
        "# Research Plan Template",
        "## Topic",
        "## Scope / Non-Goals",
        "## Inputs / Dependencies",
        "## Work Breakdown",
        "## Execution Contract",
        "## Verification Plan",
        "## Failure / Rollback Plan",
        "## Completion Checklist",
    ],
    "research/research_plan.md": [
        "# Active Research Plan",
        "## Status",
        "## Activation Checklist",
        "## Resume Note",
    ],
    "research/library/index.md": [
        "# Research Library",
        "## Entries",
    ],
    "research/reviews/repro_checklist.md": [
        "# Reproducibility Checklist",
        "## Environment",
        "## Data And Evaluation",
        "## Randomness And Stability",
        "## Artifacts",
        "## Decision",
    ],
    "templates/experiment_note.md": [
        "# Experiment Note Template",
        "## Goal",
        "## Setup",
        "## Result",
        "## Interpretation",
        "## Write-Back",
    ],
    "templates/paper_note.md": [
        "# Paper Note Template",
        "## Source",
        "## What It Contributes",
        "## Relevance To Current Topic",
        "## Claim Write-Back",
    ],
    "templates/sprint_contract.md": [
        "# Sprint Contract Template",
        "## Objective",
        "## Scope / Non-Goals",
        "## Inputs / Dependencies",
        "## Acceptance Checks",
        "## Artifacts To Write Back",
        "## Failure / Rollback Plan",
        "## Review Gate",
        "## Handoff",
    ],
}

CSV_HEADERS = {
    "research/paper_queue.csv": [
        "id",
        "query_or_citation",
        "source_type",
        "priority",
        "status",
        "owner",
        "depends_on",
        "write_back",
        "artifact_path",
        "review_gate",
        "last_updated",
        "notes",
    ],
    "research/experiment_queue.csv": [
        "id",
        "hypothesis_slice",
        "priority",
        "status",
        "owner",
        "depends_on",
        "runbook_path",
        "artifact_path",
        "verification_gate",
        "write_back",
        "last_updated",
        "notes",
    ],
}

ABS_PATH_PATTERNS = [
    re.compile(r"/Users/"),
    re.compile(r"file://"),
    re.compile(r"C:\\\\"),
]


def fail(message: str) -> None:
    print(f"[research-check] {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"cannot read {path.relative_to(ROOT)}: {exc}")


def check_required_files() -> None:
    for rel in list(MD_REQUIRED) + list(CSV_HEADERS):
        path = ROOT / rel
        if not path.exists():
            fail(f"missing required file: {rel}")


def check_markdown_headings() -> None:
    for rel, headings in MD_REQUIRED.items():
        text = read_text(ROOT / rel)
        for heading in headings:
            if heading not in text:
                fail(f"{rel} is missing heading: {heading}")


def check_csv_headers() -> None:
    for rel, expected in CSV_HEADERS.items():
        path = ROOT / rel
        with path.open(newline="", encoding="utf-8") as fh:
            reader = csv.reader(fh)
            try:
                actual = next(reader)
            except StopIteration:
                fail(f"{rel} is empty")
        if actual != expected:
            fail(f"{rel} header mismatch\nexpected: {expected}\nactual:   {actual}")


def check_absolute_paths() -> None:
    for rel in list(MD_REQUIRED) + list(CSV_HEADERS):
        text = read_text(ROOT / rel)
        for pattern in ABS_PATH_PATTERNS:
            if pattern.search(text):
                fail(f"{rel} contains an absolute path or file URL: {pattern.pattern}")


def main() -> None:
    check_required_files()
    check_markdown_headings()
    check_csv_headers()
    check_absolute_paths()
    print("research OS checks passed")


if __name__ == "__main__":
    main()
