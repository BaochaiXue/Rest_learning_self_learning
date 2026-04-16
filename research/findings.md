# Findings Log

Append substantive observations here.
This file is append-only in practice: do not rewrite history unless you are correcting a clear factual error.

## Logging Contract

- Every substantive action gets an entry.
- Keep observation and interpretation separate.
- Link each entry to the artifact, run, source, or file path that justifies it.
- If code or experiment state changes, log it here before moving on.
- Prefer one concise entry per coherent work chunk.

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

### 2026-04-15 22:50 | Added execution-contract layer

- Context: Tighten the root research OS so a future topic can move from planning into bounded execution without inventing ad hoc formats.
- Action: Added a live `research/research_plan.md` shell, hardened the research state guidance, expanded the queue and note templates, and added a root-level research check target.
- Observation: The repo now has a direct path from plan to sprint contract to logged findings, and the structure is still small enough to keep context load low.
- Evidence: `research/README.md`, `research/research_plan.md`, `research/research_plan.template.md`, `research/findings.md`, `research/literature_map.md`, `research/claims_registry.md`, `research/decision_log.md`, `research/open_questions.md`, `research/paper_queue.csv`, `research/experiment_queue.csv`, `research/reviews/repro_checklist.md`, `templates/sprint_contract.md`, `scripts/research_check.py`, `Makefile`.
- Verification: `python3 scripts/research_check.py` and `make research-check` both passed; `git diff --check` was clean.
- Next step: Instantiate `research/research_plan.md` for the first concrete topic, then create a sprint contract from `templates/sprint_contract.md` before any implementation work.

### 2026-04-15 23:05 | Harness-engineering refactor integrated

- Context: Restructure the root layer so vibe research is managed more like a harness-engineered repo with docs-as-map, explicit handoffs, evaluation gates, and bounded execution contracts.
- Action: Added a root docs system of record under `docs/`, tightened custom agents and skills into clearer generator/evaluator style roles, expanded the root research check to cover docs plus research state, and wired `make check` to run root validation before child-project audit.
- Observation: The root repo now has a map-first entrypoint, phase-handoff files, quality policies, execution-plan scaffolding, a live research plan shell, and stricter agent/skill contracts. The remaining failing check is still the child-project absolute-path audit in downloaded paper sources and generated reports.
- Evidence: `AGENTS.md`, `README.md`, `ARCHITECTURE.md`, `docs/index.md`, `docs/design-docs/core-beliefs.md`, `docs/exec-plans/`, `docs/handoffs/latest_handoff.md`, `docs/quality/`, `docs/reliability.md`, `.codex/config.toml`, `.codex/agents/*.toml`, `.agents/skills/*`, `research/*`, `templates/*`, `scripts/research_check.py`, `Makefile`.
- Verification: `python3 scripts/research_check.py`, `make research-check`, and `git diff --check` passed. `make check` still fails in `nested_learning_textbook/scripts/check_absolute_paths.py` on pre-existing child-project absolute-path hits.
- Next step: Start the first concrete research topic in a fresh thread, instantiate `research/research_plan.md`, create a sprint contract, and use `docs/index.md` plus `docs/handoffs/latest_handoff.md` as the resumable coordination layer.

### 2026-04-15 23:20 | Added two arXiv papers to root research library

- Context: User requested that arXiv papers 2511.21740 and 2511.20639 be added to the research library without polluting the textbook-specific child corpus.
- Action: Created two root-library entries under `research/library/`, downloaded local PDFs, added note files, and registered both papers in `research/literature_map.md` and `research/paper_queue.csv`.
- Observation: The generic root research OS can now hold user-added papers independently of `nested_learning_textbook/manifests/papers_manifest.csv`, which avoids mixing unrelated papers into the textbook corpus.
- Evidence: `research/library/index.md`, `research/library/a_cross_species_neural_foundation_model_for_end_to_end_speech_decoding/paper_note.md`, `research/library/a_cross_species_neural_foundation_model_for_end_to_end_speech_decoding/paper.pdf`, `research/library/latent_collaboration_in_multi_agent_systems/paper_note.md`, `research/library/latent_collaboration_in_multi_agent_systems/paper.pdf`, `research/literature_map.md`, `research/paper_queue.csv`.
- Verification: Bibliographic metadata checked against arXiv abstract pages 2511.21740 and 2511.20639 on 2026-04-15. Local PDF downloads completed successfully. `python3 scripts/research_check.py` still passed after the update.
- Next step: Run `literature_scout` on these entries when a concrete topic needs them, and update claim status only after a paper-level reading pass.
