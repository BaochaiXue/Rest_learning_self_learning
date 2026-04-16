# Findings Log

Append substantive observations here.
Each entry should link to the artifact, run, source, or file path that justifies it.

## Entry Template

### YYYY-MM-DD HH:MM | Short label

- Context:
- Action:
- Observation:
- Evidence:
- Verification:
- Next step:

### 2026-04-15 22:48 | Repo-level research OS bootstrap

- Context: Initialize durable multi-agent research infrastructure at the repo root without modifying canonical textbook content.
- Action: Added repo-level governance docs, custom agent configs, repo-scoped skills, research state files, templates, and usage docs.
- Observation: The new root-layer files parse correctly and contain no absolute paths. The child-project `make check` still fails on pre-existing absolute paths inside downloaded paper sources and generated hygiene reports.
- Evidence: `AGENTS.md`, `PLANS.md`, `README.md`, `ARCHITECTURE.md`, `.codex/config.toml`, `.codex/agents/*.toml`, `.agents/skills/*`, `research/*`, `templates/*`, `docs/*`.
- Verification: `tomllib` parsed 8 TOML files successfully. Ruby parsed 6 skill YAML files and verified frontmatter presence for 6 `SKILL.md` files. `python3 nested_learning_textbook/scripts/validate_manifest.py` passed. `python3 nested_learning_textbook/scripts/check_book_structure.py` reported warnings only. `python3 nested_learning_textbook/scripts/check_absolute_paths.py` and `make check` failed on 24 pre-existing absolute-path hits in child-project paper sources and generated reports.
- Next step: Start the first concrete topic by instantiating `research/research_plan.md` from `research/research_plan.template.md` in a fresh thread so the new custom agents can be loaded cleanly.
