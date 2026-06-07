# Full PR × Rule Matrix Audit v2 — Thin Kernel Preservation

Evidence layer: Candidate PR #46 branch `codex/complete-github-download-rule`. This report is GitHub repo evidence only; do not upload it to ChatGPT Project Knowledge and do not paste it into Project Instructions.

## Thin-kernel principle

Minimal instruction is not “shorter at any cost”; it is a thin control kernel. `Instructions.md` keeps triggers, routing, priorities, safety/evidence/activation boundaries, and mandatory gates. Detailed procedure, tests, owner maps, failure classes, examples, and long criteria belong in Knowledge/protocol files, registry, testing files, ledger, validators, reports, and CI. Compression is valid only when behavior is not weakened or moved to a less reliable layer without compensation.

## Scope and correction vs prior audit

- This replaces the earlier partial critical-row matrix with a full-shaped matrix.
- Rows: all current `Instructions.md` kernel rows I01..I50, PB-00/PB-00A/PB-00B/PB-01..PB-67, and META-01..META-15 governance rows.
- Columns: PR01..PR46 status plus PR01..PR46 evidence-level columns in the expanded CSV artifact generated for this audit pass.
- Status values: `added`, `strengthened`, `preserved`, `weakened`, `missing`, `superseded`, `not relevant`, `not inspected`.
- Evidence levels: `diff inspected`, `current file/diff inspected`, `PR body inspected`, `metadata only`, `inferred`, `not inspected`.
- Important correction: uninspected historical cells are `not inspected`, not default `not relevant`.

## Artifact Destination Matrix

| Artifact | Class | Exact destination | Forbidden destinations | Active/evidence status |
|---|---|---|---|---|
| `reports/audits/pr_rule_matrix_full_v2_2026-06-07.md` | report/evidence | GitHub repo PR #46 branch | Project Instructions; ChatGPT Project Knowledge | Candidate repo evidence only |
| expanded CSV generated in chat sandbox | report/evidence | sandbox artifact; repo upload blocked by connector-size practicality in this pass | Project Instructions; ChatGPT Project Knowledge | Candidate evidence only |
| `reports/audits/pr_rule_matrix_deep_audit_2026-06-07.md` | report/evidence | GitHub repo PR #46 branch | Project Instructions; ChatGPT Project Knowledge | Superseded partial critical-row report |
| `reports/audits/pr_rule_matrix_deep_audit_2026-06-07.csv` | report/evidence | GitHub repo PR #46 branch | Project Instructions; ChatGPT Project Knowledge | Superseded partial critical-row CSV |

## Status counts per PR from the full-shaped matrix

| PR | added | strengthened | preserved | weakened | missing | superseded | not relevant | not inspected |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PR01 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 130 |
| PR02 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR03 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR04 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR05 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR06 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR07 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR08 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR19 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR20 | 5 | 6 | 0 | 0 | 0 | 0 | 0 | 124 |
| PR21 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 128 |
| PR22 | 0 | 0 | 53 | 0 | 0 | 0 | 0 | 82 |
| PR23 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR24 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR26 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR27 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR28 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR29 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR30 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR31 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR33 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR34 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR35 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR36 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR37 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR38 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR39 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR40 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR41 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR42 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 135 |
| PR43 | 0 | 1 | 0 | 2 | 3 | 0 | 0 | 129 |
| PR44 | 0 | 1 | 0 | 2 | 3 | 0 | 0 | 129 |
| PR45 | 0 | 2 | 0 | 0 | 6 | 0 | 0 | 127 |
| PR46 | 0 | 9 | 126 | 0 | 0 | 0 | 0 | 0 |

## Confirmed weakenings

- PR43 and PR44: `I17 Direct Destination + GitHub download trigger` and `PB-54 Direct Destination / Deep-Link Verification Gate` were weakened because the GitHub-specific download wording risked replacing the broader generic direct-target rule.

## Suspected weakenings / compression risks

- Earlier PR46 revisions compressed `Artifact Destination Contract`, `Runtime Activation Check`, and `No Secrets` too aggressively. Current PR46 head has restored precise boundary wording in the instruction while keeping details outside the kernel.
- Historical PRs without inspected diffs remain `not inspected`; no weakening is asserted or cleared for those cells.

## Missing companion updates

- PR45: GitHub download behavior was merged into protocol/manifest/ledger but companion coverage was missing or incomplete for the kernel trigger, protected-behavior registry owner map, regression smoke test, and testing_protocol test.

## Rules moved to weaker layer

- PR45 effectively left GitHub download behavior in lower layers without a compact kernel trigger. PR46 repairs this by adding only a short trigger to `Instructions.md` and keeping details in protocol/registry/testing files.

## Rules restored in later PR

- PR46 restores generic Direct Destination behavior and adds GitHub download specifics.
- PR46 restores precise `old chat before update` activation boundary wording.
- PR46 restores explicit `ChatGPT Project Knowledge` and `GitHub source file` artifact destination labels.
- PR46 restores precise `false runtime activation claims` wording in PB-63.

## Still unresolved before merge

- Fresh instruction length check after latest commits.
- Build Knowledge package and verify ZIP contents.
- Run package linter / package guard if available.
- Refresh PR mergeability/CI/status.
- Do not claim Stable or ChatGPT Project runtime activation until merge + Project UI update + Knowledge upload + new-chat activation check.

## Additional prevention added

`project_learning_ledger.md` contains a partial-audit mislabeling failure rule: partial audits must not be delivered as full audits; uninspected cells must be explicitly `not inspected`; evidence level must be recorded; confirmed/suspected weakenings, missing companions, compression risks, weaker-layer moves, restored rules, and unresolved items must be separated.
