# Claims Registry

Track research claims at sentence-level granularity when possible.
This is the place to decide whether a claim is `verified`, `uncertain`, or `rejected`.

## Claim Contract

- Keep claims small enough to support or reject directly.
- Record the supporting source, experiment, or file path.
- Update the registry when a claim changes status, not only when writing prose.

| Claim ID | Claim | Status | Evidence Type | Evidence Pointer | Support Scope | Gap / Risk | Owner | Last Reviewed |
|---|---|---|---|---|---|---|---|---|
| claim-000 | [replace with a concrete claim] | uncertain / verified / rejected | source / run / file | [repo-relative path or URL] | [what the evidence actually covers] | [what still needs checking] | [agent or human] | [YYYY-MM-DD] |

## Status Rules

- `verified`: directly supported by a source, run artifact, or file path
- `uncertain`: plausible but not fully supported yet
- `rejected`: investigated and not supported

## Notes

- Do not let the registry drift behind the prose draft.
- If a claim is split into multiple subclaims, give each subclaim its own row.
