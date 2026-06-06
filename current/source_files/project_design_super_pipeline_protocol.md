Use this file only for the Project Design Super-Pipeline. Main Project/GPT Instructions control behavior.

Purpose: operational protocol for non-trivial GPT/Project design, audit, patch, package, repository, Codex, governance, testing, and child-system work.

## Trigger
Run this protocol when the request materially affects instructions, source files, package state, Project Knowledge, GPT/Project architecture, repo/Codex delivery, governance, tests, child systems, safety/source policy, protected behaviors, or evidence-based delivery. Scale depth to risk; compact mode is allowed only when all mandatory gates are still satisfied.

## Core pipeline
1. Check: split the request; verify active package basis, authority, safety, current/source needs, forbidden side effects, and evidence layer.
2. Specify: define objective, non-goals, stakeholders, input/output contract, hidden requirements, success criteria, invalid-delivery conditions, and tests.
3. Architect: choose system shape before writing prompts/files; compare GPT, Project, Project+GPT, multi-GPT, SOP, matrix, repository, workflow, and no-change routes when relevant.
4. Expand: enumerate candidate actions across edit, add, delete, rename, split, merge, compress, template, test, source, delivery, workflow, and governance mechanisms.
5. Generate: create candidate mechanisms with trigger, action, owner file, evidence, tests, fail condition, and expected behavior.
6. Combine: test useful hybrids and companion-file combinations; preserve PB owner maps and package continuity.
7. Attack: use counterexamples, misuse cases, hidden requirements, mutation ideas, stale-source risks, route failures, and layer-mixing risks against each candidate.
8. Verify: check protected behavior preservation, manifest/package consistency, source/safety basis, repo-only exclusion, artifact destinations, and activation semantics.
9. Repair: patch candidates until attacks are addressed or explicitly mark remaining limits.
10. Test: run applicable package linter/guard/regression/mutation checks; never label unrun checks as PASS.
11. Deliver: provide exact artifacts, destinations, forbidden destinations, evidence layer, tests, and verdict.
12. Ledger: record systemic failures and new anti-regression mechanisms in the Learning Ledger when the task reveals a recurring failure class.

## Hidden Requirements Mining
Before final instructions or package changes, mine hidden requirements from the user's goal, existing package files, PB registry, manifest, delivery protocol, source/safety policy, platform limits, repository branch state, user-language preferences, forbidden side effects, and known failure patterns. Convert hidden requirements into explicit constraints or assumptions.

## Architecture First
Do not write final prompts, package instructions, or repository edits before architecture is selected. Architecture output must include purpose, target user, use cases, inputs, outputs, scope/non-goals, files/tools/sources, safety, tests, delivery layer, and verdict.

## Risk/Safety/Source Classification
Classify risk as low, medium, high, or blocked. Mark whether source verification is required for current facts, platform behavior, OpenAI-product behavior, legal/medical/financial/compliance content, security, privacy, or user-specific claims. Unsafe or unverifiable required claims block delivery or require explicit NOT VERIFIED labeling.

## Search Space Governance
Enumerate plausible mechanisms and reject options that weaken protected behaviors, add bloated files without distinct roles, route repo-only controls into active Knowledge, create unverifiable activation claims, increase user work unnecessarily, or ignore companion-file updates.

## Candidate Mechanism Generation
Each candidate must state trigger, action, owner file, companion files, protected behavior impact, tests, evidence required, delivery destination, and fail condition. Slogans without enforcement are invalid candidates.

## Combination Search
Compare single mechanisms and hybrids. Prefer the smallest non-dominated combination that preserves behavior, covers hidden requirements, improves evidence, and remains maintainable.

## Counterexample-Guided Improvement
Run counterexample_improvement_protocol.md on material rules, files, architectures, tests, and packages. Counterexamples must include at least omission, ambiguity, adversarial/misuse, layer-mixing, source/evidence, and regression cases when applicable.

## Pareto Ranking
Rank candidates by protected-behavior preservation, hidden-requirement coverage, risk reduction, evidence strength, test coverage, simplicity, maintainability, user-work minimization, activation clarity, and compatibility with repo-only exclusion. Select a non-dominated candidate or explain the tradeoff.

## Builder/Auditor Split
Builder proposes changes. Auditor separately verifies PB preservation, deletion burden, companion sync, manifest/linter consistency, right-sized architecture, tests, delivery destination, runtime activation claims, and child propagation before final verdict.

## Patch Lock
Any instruction/file/package/governance/registry/manifest/linter/test/delivery/routing/child-system change must satisfy patch_lock_protocol.md and protected_behavior_registry.md. Missing basis, PB impact, companion check, tests, or verdict is Invalid Delivery.

## Mutation/Regression Testing
Run mutation_testing_protocol.md and applicable regression tests for major changes or any change affecting triggers, protected behavior, delivery, source safety, manifest, or tests. Surviving material mutations require repair or explicit fail verdict.

## Evidence-Based Delivery
Final delivery must identify the evidence layer: local package, GitHub Candidate PR, GitHub main/current, ChatGPT Project UI upload, runtime active behavior, screenshot, user statement, report/evidence, or NOT VERIFIED. Do not claim Project UI/runtime activation from repository changes.

## Learning Ledger
When a recurring failure class or new anti-regression mechanism is identified, update project_learning_ledger.md or report the required ledger entry if editing the file is out of scope.

## Scaling modes
- Lite: low-risk advice or tiny edits; run all gates compactly.
- Standard: normal non-trivial design/audit/patch/package work; run the full pipeline with concise evidence.
- High-risk: governance, safety, source policy, protected behavior, child-system, repository delivery, or repeated failures; require explicit counterexamples, mutation/regression tests, and auditor pass.
- Blocked: required evidence, permission, safety, source, or active package basis is missing; stop or deliver only a limited, labeled result.

## Fail conditions
Invalid Delivery if final output lacks architecture, hidden requirements, risk/source classification, files/tools/destinations, tests, evidence verdict, PB preservation when applicable, Patch Lock when applicable, counterexample repair for material changes, mutation/regression result for governed changes, or Learning Ledger handling for systemic failures.
