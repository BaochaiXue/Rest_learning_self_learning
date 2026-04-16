# Usage Examples

Use these prompts as copyable starting points.
Adjust the topic and constraints, but keep the file targets explicit.

## 1. Start A New Research Question

```text
Read AGENTS.md, docs/index.md, PLANS.md, research/README.md, and .agents/skills/problem-framing/SKILL.md.
Use $problem-framing to create `research/research_plan.md` from `research/research_plan.template.md`.
The topic is: [replace with topic].
Define scope, non-goals, success criteria, risks, and the smallest verification path.
```

## 2. Parallel Literature Triage

```text
Read AGENTS.md, docs/index.md, `research/research_plan.md`, and the literature-related files in `research/`.
Spawn `literature_scout` and `novelty_auditor` in parallel.
Use $literature-triangulation to update `research/literature_map.md` and `research/claims_registry.md`.
Wait for both agents before synthesizing.
The question to check is: [replace with claim, method family, or benchmark].
```

## 3. Design The Minimum Experiment

```text
Read AGENTS.md, docs/index.md, `research/research_plan.md`, `research/open_questions.md`, and `.codex/agents/experiment_designer.toml`.
Spawn `experiment_designer`.
Produce the smallest defensible experiment plan, then update `research/experiment_queue.csv` and add any necessary write-back instructions for `research/findings.md`.
Keep the plan minimal and include verification gates.
```

## 4. Audit A Claim Before Writing

```text
Read AGENTS.md, docs/quality/claim_honesty_policy.md, `research/findings.md`, `research/claims_registry.md`, and `.agents/skills/claim-audit/SKILL.md`.
Use $claim-audit on these candidate claims: [replace with claims].
Downgrade unsupported claims to uncertain, point to missing evidence, and update `research/claims_registry.md`.
```

## 5. Run A Reproducibility Check Before Sharing

```text
Read AGENTS.md, docs/reliability.md, docs/quality/qa_rubric.md, `research/findings.md`, `research/reviews/repro_checklist.md`, and `.agents/skills/repro-check/SKILL.md`.
Spawn `repro_reviewer`.
Use $repro-check to review whether the current result is safe to share externally.
Update `research/reviews/repro_checklist.md`, `research/open_questions.md`, and `docs/handoffs/latest_handoff.md` with blockers and risk level.
```

## 6. Update A Phase Handoff

```text
Read AGENTS.md, docs/handoffs/latest_handoff.md, docs/exec-plans/active/index.md, and `research/decision_log.md`.
Summarize the phase boundary in `docs/handoffs/latest_handoff.md`.
Include what changed, what remains open, and the next agent or check that should run.
Keep the handoff brief and factual.
```
