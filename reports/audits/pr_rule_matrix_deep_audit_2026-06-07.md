# Deep PR × Rule Matrix Audit — Thin Kernel Preservation

Evidence layer: Candidate PR #46 branch `codex/complete-github-download-rule`. This report is GitHub repo evidence only, not active ChatGPT Project Knowledge and not Project Instructions.

## Thin-kernel principle

Minimal instruction is not “shorter at any cost”; it is a thin control kernel. `Instructions.md` should keep only triggers, routing, priorities, safety/evidence/activation boundaries, and mandatory gate references. Detailed procedures, tests, owner maps, failure classes, examples, and long criteria belong in Knowledge/protocol files, registry, testing files, ledger, validators, reports, and CI. Compression is valid only when behavior is not weakened or moved to a less reliable layer without compensation.

## Scope

- Matrix rows: current `Instructions.md` kernel lines, PB-00..PB-67, and registry/package-governance meta-rules.
- Matrix columns: PR #1..#46.
- Allowed cell values: `added`, `strengthened`, `preserved`, `weakened`, `missing`, `superseded`, `not relevant`, `not inspected`.
- This report deepens the prior matrix by adding rule class, finding, and PR46 action-status columns in the CSV.

## Artifact Destination Matrix

| Artifact | Class | Exact destination | Forbidden destinations | Active/evidence status |
|---|---|---|---|---|
| `reports/audits/pr_rule_matrix_deep_audit_2026-06-07.md` | report/evidence | GitHub repo PR #46 branch | Project Instructions; ChatGPT Project Knowledge | Candidate evidence only |
| `reports/audits/pr_rule_matrix_deep_audit_2026-06-07.csv` | report/evidence | GitHub repo PR #46 branch | Project Instructions; ChatGPT Project Knowledge | Candidate evidence only |

## Methodology limits

- Historical PRs were assessed from available PR metadata, bodies, and selected diffs inspected in the conversation. The report does not falsely claim full line-by-line reconstruction for every closed/superseded PR.
- `not inspected` means available evidence was insufficient for a row-level claim.
- `not relevant` means the PR did not appear to touch that rule class.
- `missing` means a companion rule/test/registry/file update was expected for that PR’s change class but absent.
- `weakened` means a change reduced the precision, trigger strength, layer separation, or runtime/evidence safety of the rule as compared with the prior behavior.

## Status counts per PR

| PR | added | strengthened | preserved | weakened | missing | superseded | not relevant | not inspected |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PR01 | 3 | 3 | 0 | 0 | 0 | 0 | 120 | 0 |
| PR02 | 3 | 3 | 0 | 0 | 0 | 0 | 120 | 0 |
| PR03 | 0 | 0 | 2 | 0 | 0 | 0 | 124 | 0 |
| PR04 | 5 | 2 | 0 | 0 | 0 | 0 | 119 | 0 |
| PR05 | 0 | 3 | 0 | 0 | 0 | 0 | 123 | 0 |
| PR06 | 0 | 7 | 0 | 0 | 0 | 0 | 119 | 0 |
| PR07 | 0 | 5 | 0 | 0 | 0 | 0 | 121 | 0 |
| PR08 | 0 | 3 | 0 | 0 | 0 | 0 | 123 | 0 |
| PR09 | 0 | 3 | 0 | 0 | 0 | 0 | 123 | 0 |
| PR10 | 0 | 4 | 0 | 0 | 0 | 0 | 122 | 0 |
| PR11 | 0 | 4 | 0 | 0 | 0 | 0 | 122 | 0 |
| PR12 | 3 | 0 | 0 | 0 | 0 | 0 | 123 | 0 |
| PR13 | 0 | 0 | 0 | 0 | 0 | 0 | 126 | 0 |
| PR14 | 25 | 0 | 0 | 0 | 0 | 0 | 101 | 0 |
| PR15 | 0 | 19 | 0 | 0 | 0 | 0 | 107 | 0 |
| PR16 | 14 | 0 | 0 | 0 | 0 | 0 | 112 | 0 |
| PR17 | 0 | 0 | 0 | 0 | 0 | 5 | 121 | 0 |
| PR18 | 6 | 4 | 0 | 0 | 0 | 0 | 116 | 0 |
| PR19 | 0 | 8 | 0 | 0 | 0 | 0 | 118 | 0 |
| PR20 | 7 | 4 | 0 | 0 | 0 | 0 | 115 | 0 |
| PR21 | 0 | 0 | 0 | 0 | 0 | 7 | 119 | 0 |
| PR22 | 0 | 6 | 50 | 0 | 0 | 0 | 70 | 0 |
| PR23 | 0 | 16 | 0 | 0 | 0 | 0 | 110 | 0 |
| PR24 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 126 |
| PR25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 126 |
| PR26 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 126 |
| PR27 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 126 |
| PR28 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 126 |
| PR29 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 126 |
| PR30 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 126 |
| PR31 | 0 | 5 | 0 | 0 | 0 | 0 | 121 | 0 |
| PR32 | 5 | 0 | 0 | 0 | 0 | 0 | 121 | 0 |
| PR33 | 0 | 0 | 0 | 0 | 0 | 6 | 120 | 0 |
| PR34 | 0 | 3 | 0 | 0 | 0 | 0 | 123 | 0 |
| PR35 | 0 | 0 | 0 | 0 | 0 | 1 | 125 | 0 |
| PR36 | 3 | 4 | 0 | 0 | 0 | 0 | 119 | 0 |
| PR37 | 4 | 3 | 0 | 0 | 0 | 0 | 119 | 0 |
| PR38 | 0 | 3 | 0 | 0 | 0 | 0 | 123 | 0 |
| PR39 | 0 | 6 | 0 | 0 | 0 | 0 | 120 | 0 |
| PR40 | 4 | 0 | 0 | 0 | 0 | 0 | 122 | 0 |
| PR41 | 0 | 2 | 0 | 0 | 0 | 0 | 124 | 0 |
| PR42 | 0 | 4 | 0 | 0 | 0 | 0 | 122 | 0 |
| PR43 | 0 | 2 | 0 | 3 | 0 | 0 | 121 | 0 |
| PR44 | 0 | 2 | 0 | 3 | 0 | 0 | 121 | 0 |
| PR45 | 0 | 3 | 0 | 0 | 4 | 0 | 119 | 0 |
| PR46 | 0 | 6 | 4 | 0 | 0 | 0 | 116 | 0 |

## Critical rule rows / PR46 repair check

| Rule_ID | Rule | Relevant historical issue | PR46 status/action |
|---|---|---|---|
| I01 | Designer role/scope/language child EN | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I02 | Authority and conflict honesty | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I03 | Request Check | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I04 | Default audit-plus-patch | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I05 | Delegation boundaries and connector/Codex/API | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I06 | Architecture first and matrix | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I07 | Super-Pipeline trigger | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I08 | Combination Search | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I09 | Action Discovery | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I10 | Execution Substrate Selection / Failover | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I11 | User-Facing Russian Output | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I12 | Minimal User Action / User Work Firewall | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I13 | Target Placement and Result Lock | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I14 | Problem-Class Generalization | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I15 | External UI Handoff | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I16 | Approval-to-Execution Handoff | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I17 | Direct Destination + GitHub download trigger | PR43:weakened, PR44:weakened, PR45:missing | PR46=strengthened; Historical weakening in PR43, PR44. Missing companion coverage in PR45. PR46 must include kernel/protocol/registry/testing companion coverage when relevant. No further rule change required in PR46 for this row, subject to build/length gates. |
| I18 | Copy-Ready Actions | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I19 | Artifact Destination Contract | No historical defect; relevant to PR46 coverage | PR46=preserved; No further rule change required in PR46 for this row, subject to build/length gates. |
| I20 | Repo-only Controls Exclusion | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I21 | Codex/GitHub Direct Handoff | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I22 | Runtime Activation Check | No historical defect; relevant to PR46 coverage | PR46=preserved; No further rule change required in PR46 for this row, subject to build/length gates. |
| I23 | Delegation Failure Reframe | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I24 | Evidence Claim and layer labels | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I25 | Verification Target | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I26 | Instruction Equivalence | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I27 | Answer Preservation | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I28 | Rational Route | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I29 | Durable Ledger | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I30 | State Reconciliation | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I31 | Completion Ledger | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I32 | Activation Semantics | No historical defect; relevant to PR46 coverage | PR46=not relevant; Manual review performed against current PR46 kernel wording; no broad new rule added to keep Instructions minimal. |
| I33 | Plan/State Separation + Audit-only Before Patch | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I34 | Cost/Capability + Free-Route Fallback | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I35 | No Secrets | No historical defect; relevant to PR46 coverage | PR46=preserved; No further rule change required in PR46 for this row, subject to build/length gates. |
| I36 | Patch State Machine | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I37 | Patch Lock | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I38 | Builder/Auditor split | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I39 | Kernel self-preservation list | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I40 | Current package truth | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I41 | Right-sized architecture | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I42 | Registry/PB diff/deletion burden for inst/file changes | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I43 | File changes decision | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I44 | Behavior-only files | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I45 | Complete package + Artifact Destination Matrix | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I46 | Run testing_protocol before delivery | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I47 | Current/high-stakes source verification | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I48 | Safety refusal boundary | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I49 | Child-system inheritance | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| I50 | Final gate list | No historical defect; relevant to PR46 coverage | PR46=not relevant; No action required. |
| PB-22 | Regression smoke tests | PR45:missing | PR46=strengthened; Missing companion coverage in PR45. PR46 must include kernel/protocol/registry/testing companion coverage when relevant. No further rule change required in PR46 for this row, subject to build/length gates. |
| PB-30 | Instruction Equivalence Gate | No historical defect; relevant to PR46 coverage | PR46=preserved; No further rule change required in PR46 for this row, subject to build/length gates. |
| PB-54 | Direct Destination / Deep-Link Verification Gate | PR43:weakened, PR44:weakened, PR45:missing | PR46=strengthened; Historical weakening in PR43, PR44. Missing companion coverage in PR45. PR46 must include kernel/protocol/registry/testing companion coverage when relevant. No further rule change required in PR46 for this row, subject to build/length gates. |
| PB-56 | Artifact Destination Contract | No historical defect; relevant to PR46 coverage | PR46=preserved; No further rule change required in PR46 for this row, subject to build/length gates. |
| PB-63 | Mutation Testing | No historical defect; relevant to PR46 coverage | PR46=preserved; No further rule change required in PR46 for this row, subject to build/length gates. |
| PB-65 | Blocked-Route and Short-Route Handoff Gate | PR45:missing | PR46=strengthened; Missing companion coverage in PR45. PR46 must include kernel/protocol/registry/testing companion coverage when relevant. No further rule change required in PR46 for this row, subject to build/length gates. |

## Deep audit conclusions

1. PR #43 and PR #44 were the only inspected changes that clearly weakened the generic Direct Destination kernel while adding a GitHub-specific download rule. The defect was not the GitHub rule itself; the defect was replacing a broader generic link/target trigger with a narrower GitHub download trigger.
2. PR #45 correctly merged the durable protocol/manifest/ledger layer but left companion gaps: no kernel trigger, no protected-registry owner-map update, no smoke test, and no testing_protocol test.
3. PR #46 now repairs those gaps without moving detailed procedure into `Instructions.md`: the kernel has only a compact GitHub download trigger; detail lives in `github_download_link_protocol.md`, PB-54/PB-65 registry wording, T35, and testing_protocol.
4. The last corrective commits restored important precision in `Instructions.md`: `ChatGPT Project Knowledge`, `GitHub source file`, `old chat before update`, and a more precise repository/security wording. This follows the minimal-instruction principle because these are boundary labels, not long procedures.
5. Before merge, strict release gates still require package build and fresh instruction length check. Runtime activation must not be claimed from this PR.

## Required pre-merge checks still NOT EXECUTED in this pass

- Recalculate `Instructions.md` character count after the latest corrective commit.
- Run `python scripts/build_knowledge_package.py --output <zip>` and verify ZIP contains only `Instructions.md` and `Knowledge/*.md` from active manifest.
- Run package linter / package guard if available in the execution environment.
- Confirm PR #46 remains mergeable after CI/status refresh.
- Do not claim ChatGPT Project runtime activation until Project UI update + Knowledge upload + new-chat activation check.