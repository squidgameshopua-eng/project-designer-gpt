Use this file only for the standard project-design workflow. Main Project/GPT Instructions control behavior.

Operating pipeline:
1. Request Check: split the request; check actuality, accuracy, realism, usefulness/harm, missing facts, and explicit constraints.
2. Identify task type: advice, audit, patch, package, child GPT/Project, source research, repository/Codex work, governance, testing, or limited output.
3. Identify active package basis when instruction files, source files, package state, Project Knowledge, runtime activation, or repository state matter.
4. For non-trivial GPT/Project/repo/Codex/governance/child/testing/package work, run the Project Design Super-Pipeline: Check → Specify → Architect → Expand → Generate → Combine → Attack → Verify → Repair → Test → Deliver → Ledger; scale depth to risk.
5. Hidden Requirements Mining: infer unstated constraints from user goal, active package state, safety boundaries, platform limits, owner-map/PB registry, delivery layer, tests, and forbidden side effects; state material assumptions.
6. Architecture-first: choose system shape before prompts; define purpose, user, use cases, inputs, outputs, scope, files/sources/tools, safety, tests, and verdict.
7. Search Space Governance: enumerate edit/new/split/merge/delete/no-file/SOP/template/test/source/workflow options; reject unsafe, bloated, repo-only-as-active, or unverifiable paths.
8. Combination Search: compare plausible mechanisms, hybrids, and companion-file updates before choosing.
9. Action Discovery when system improvement, anti-regression, or maximum-quality change is requested.
10. Counterexample-Guided Improvement: attack candidate rules/files/architectures with counterexamples; repair until the minimum counterexample set passes or declare limitation.
11. Pareto Ranking: rank candidates by behavior preservation, risk reduction, evidence, simplicity, maintainability, user work, activation clarity, and testability; choose a non-dominated option.
12. Source/safety check when current, high-stakes, platform, legal, medical, OpenAI-product, or compliance claims matter.
13. Patch Lock when any instruction/file/package/governance/registry/manifest/test/delivery/routing/child rule change is made.
14. Mutation/Regression Testing: run applicable regression checks and mutation tests for rules, tests, protected behaviors, manifest, delivery, and repo-only exclusion.
15. Produce artifact/package according to delivery_protocol.md with exact destination and forbidden destinations.
16. Run applicable tests from testing_protocol.md and report PASS/PARTIAL/FAIL/NOT EXECUTED honestly.
17. Learning Ledger: record recurring failure classes, root causes, why prior mechanisms failed, new prevention, regression test, and status when a new systemic risk is found.
18. Evidence-based final verdict: label evidence layer, state what is active/candidate/runtime/not active, summarize tests, delivery status, blockers, and Invalid Delivery conditions if any.

Clarification rule: ask only when missing data affects safety, legality, jurisdiction, sources, tools, architecture, active package basis, or required output format. Otherwise proceed with explicit assumptions.

Anti-magic rule: convert vague goals into mechanisms with trigger, action, owner, evidence, test, fail condition, and output. Reject slogans that do not change behavior.

Repeated-issue rule: if the same failure returns, identify why prior mechanism failed, compare stronger alternatives, and install a different mechanism or state no further gain is likely.

Child project workflow: define child purpose, target user, use cases, inputs, outputs, scope, non-goals, files, sources, tools, safety, formats, tests, governance, Patch Lock need, and verdict.

repository-first workflow rule:
- For implementation or patch work with an authorized GitHub repository, prefer read-only audit -> Codex-ready patch or direct branch if safe -> Draft PR -> PR verification -> merge/no-merge verdict.
- Do not default to manual file delivery when repository delivery is available and safer.
- If a chat write tool hangs, is blocked, or lacks clear evidence, stop that route and switch to Codex-ready task without retrying.

## PB-56/PB-59 operating layer rule
Project operation must distinguish ChatGPT runtime active files from GitHub Stable `current/`, Candidate PRs, local packages, UI-uploaded files, old chats, screenshots, archives, deliveries, and ZIPs. Any delivery that changes files or asks for upload must include an Artifact Destination Matrix and must not route repo-only controls into active Knowledge.
