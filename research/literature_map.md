# Literature Map

Use this file to track candidate sources and what each one contributes.
Keep each row small and atomic so it can be reviewed or batch-processed later.

## Source Contract

- One row per source.
- Mark `Primary?` as `yes` or `no`.
- Mark `Status` as `queued`, `uncertain`, or `verified`.
- Prefer primary sources over summaries.
- If a claim only comes from a secondary source, keep it `uncertain` until verified.

| Source ID | Type | Primary? | Status | Relevance | Key Contribution | Evidence Pointer | Follow-up | Notes |
|---|---|---|---|---|---|---|---|---|
| source-20260415-001 | paper | yes | queued | user-added root research library entry; relevance to active topic not yet triaged | Cross-species pretrained neural encoder plus end-to-end Brain-to-Text framework for speech decoding; reports improved WER and cross-task transfer | `research/library/a_cross_species_neural_foundation_model_for_end_to_end_speech_decoding/paper_note.md` | Verify whether it belongs to an active topic or stays as background library material | Added from arXiv 2511.21740 on 2026-04-15 |
| source-20260415-002 | paper | yes | queued | directly relevant to multi-agent/harness research methods | Training-free latent-space collaboration framework for LLM multi-agent systems; claims accuracy, token, and latency gains over text-mediated MAS | `research/library/latent_collaboration_in_multi_agent_systems/paper_note.md` | Triaged next if the active topic touches multi-agent collaboration or agent runtime efficiency | Added from arXiv 2511.20639 on 2026-04-15 |
| source-000 | paper / doc / benchmark / repo | yes / no | queued / uncertain / verified | [fill in] | [fill in] | [repo-relative path or URL] | [what still needs checking] | Template row |

## Notes

- Reclassify rows in place when a source moves from tentative to verified.
- Keep evidence pointers repo-relative whenever the evidence lives in the repo.
- If a row supports a claim, mirror that claim in `research/claims_registry.md`.
