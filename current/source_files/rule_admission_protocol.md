# Rule Admission Protocol

Purpose: prevent governance drift, instruction bloat, protected-behavior erosion, and unsafe self-modification while allowing future development of this system.

Authority: this protocol is active Project Knowledge only when listed in current/package_manifest/package_manifest.json. It does not override Project Instructions, safety, user constraints, or higher-authority rules.

Core invariant:
- No new rule may be added directly to Project Instructions, source files, manifest, linter, tests, templates, delivery process, GitHub/Codex workflow, or package structure until it is classified, placed, tested, and checked against protected behaviors.
- Future development of this system must preserve the Thin Kernel plus Rule Admission Gate plus GitHub-first release process.
- Direct instruction expansion without classification is Invalid Delivery.

Rule Admission Gate:
1. Capture the proposed rule exactly.
2. State the problem it solves and the failure mode it prevents.
3. Check whether an existing instruction, source file, PB-ID, test, linter check, manifest entry, template, or delivery rule already covers it.
4. Classify the rule: Kernel, Router, Protocol, Registry/PB-ID, Test, Linter/manifest, Template, Domain preference, Evidence/report/archive, or Reject/duplicate.
5. Assign an owner file or repo-only control.
6. Identify companion files that must change together.
7. Identify affected PB-ID and whether a new PB-ID is required.
8. Identify required tests and whether package_linter/manifest checks must change.
9. Decide whether Project Instructions must change. If yes, the change must be Kernel-critical and must replace or compress weaker text without PB loss.
10. Run Patch Lock, protected-registry diff, companion-file check, and relevant tests before delivery.
11. Report release state: Experimental, Candidate, Audited Candidate, Stable, Runtime Active, or Evidence-only.

Preferred placement:
- Put only Kernel-critical triggers in Project Instructions.
- Put procedures in protocol files.
- Put behavioral traps in regression_smoke_tests.md.
- Put pass/fail criteria in testing_protocol.md.
- Put protected invariants in protected_behavior_registry.md.
- Put mechanical checks in package_manifest.json, package_linter.py, scripts, or CI.
- Put output shape in output_templates.md.
- Put historical evidence in reports/archive, not active Knowledge.

Hard blockers:
- Adding or changing a rule without Rule Admission Gate.
- Directly appending new governance text to Project Instructions without Kernel classification.
- Weakening Thin Kernel, Patch Lock, PB registry, Builder/Auditor split, GitHub-first release state, repo-only controls exclusion, runtime activation separation, or evidence-layer honesty.
- Moving repo-only controls into active Project Knowledge.
- Adding files without distinct owner role.
- Adding duplicate protocols instead of updating the existing owner file.
- Treating Candidate PR, local package, ZIP, old chat, screenshot, or report as Stable/runtime active.
- Claiming GitHub, Project UI, Codex, CI, linter, tests, upload, or runtime activation without direct evidence.

Instruction impact rule:
- If a proposed rule needs Project Instructions, first attempt to express it as a short router/kernel trigger.
- Do not add long procedures, examples, templates, or file-specific details to Project Instructions.
- If Project Instructions are near limit, the patch must reduce or replace weaker text rather than add net bloat.
- Any instruction change must include deletion burden and PB preservation evidence.

Self-development rule:
- Because this system will continue developing itself, every future system-development change must preserve this protocol or explicitly strengthen it.
- A change that disables, bypasses, hides, or narrows Rule Admission Gate is Critical FAIL unless the user explicitly requests decommissioning and a safer replacement is provided.

Verdict rule:
- If classification, owner file, companion files, affected PB-ID, tests, linter/manifest impact, or release state are unclear, the rule is Not Ready.
