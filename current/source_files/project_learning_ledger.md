Use this file only as the Learning Ledger for recurring failure classes and anti-regression mechanisms. Main Project/GPT Instructions control behavior.

Purpose: ledger for recurring failure classes and anti-regression mechanisms.

## Entry format
- Ledger ID:
- Date/evidence layer:
- Observed failure:
- Failure class:
- Root cause:
- Why prior mechanism failed:
- New prevention mechanism:
- Owner files / PB IDs:
- Regression test:
- Status: open / active / superseded / retired

## Ledger rules
Add or update an entry when a user report, audit, test, validator, PR review, runtime behavior, or repository evidence shows a recurring/systemic failure class. Entries must name an enforceable prevention mechanism and at least one regression test or counterexample. Do not use the ledger to claim runtime activation; it records package design evidence only unless Project UI/runtime evidence is separately provided.

## Initial entries

### LL-001 Prompt-over-architecture
- Ledger ID: LL-001
- Date/evidence layer: 2026-06-06 / GitHub Candidate package design.
- Observed failure: project-design work can jump to prompt text or final instructions before defining architecture, hidden requirements, risks, sources, tools, tests, delivery layer, and evidence verdict.
- Failure class: Prompt-over-architecture.
- Root cause: architecture-first and final-gate requirements existed but did not force a scaled end-to-end search, attack, repair, testing, and ledger loop for non-trivial Project/GPT/repo/governance work.
- Why prior mechanism failed: existing Architecture First, Combination Search, Action Discovery, Patch Lock, and Final Gate rules were distributed across files and did not explicitly require hidden requirements mining, CEGIS, mutation testing, Pareto ranking, and learning-ledger closure.
- New prevention mechanism: Project Design Super-Pipeline with Hidden Requirements Mining, Counterexample-Guided Improvement, Mutation/Regression Testing, Pareto Ranking, Evidence-Based Delivery, and Learning Ledger gates.
- Owner files / PB IDs: project_design_super_pipeline_protocol.md; counterexample_improvement_protocol.md; mutation_testing_protocol.md; project_operating_protocol.md; testing_protocol.md; protected_behavior_registry.md; PB-60, PB-61, PB-62, PB-63, PB-64.
- Regression test: Super-Pipeline trigger test plus Prompt-over-architecture counterexample: non-trivial GPT/Project package request must not deliver final instructions until architecture, hidden requirements, risk/source classification, files/tools, tests, delivery destination, and evidence verdict are present.
- Status: active
