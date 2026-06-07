Use this file only for Patch Lock, invalid-delivery blocking, and regression-proof package changes. Main Project/GPT Instructions control behavior.

Patch Lock trigger: any Project/GPT instruction, source file, package manifest, testing protocol, delivery protocol, registry, template, source policy, or child-system change must run Patch Lock before patching unless user explicitly requested audit-only/no patch.

Patch Lock minimum gates:
1. Basis: identify active/current/candidate/obsolete inputs and evidence layer.
2. Scope: exact files/instructions/rules affected.
3. PB map: protected_behavior_registry.md IDs preserved/replaced/weakened/removed/unverified.
4. Deletion burden: every removed/compressed/merged rule has equal-or-stronger replacement or justified obsolete status.
5. Companion files: check instruction_governance.md, testing_protocol.md, delivery_protocol.md, output_templates.md, package_state_protocol.md, regression_smoke_tests.md, source_safety_policy.md, project_operating_protocol.md, child packages when relevant.
6. Source/tool safety: no invented source/test/file/permission; current facts verified when material.
7. File structure decision: edit/new/split/merge/delete/no-file compared.
8. Test plan: testing_protocol.md + regression_smoke_tests.md applicable tests selected.
9. Delivery plan: complete replacement package or explicit audit-only report.
10. Verdict: PASS/PARTIAL/FAIL/NOT EXECUTED with evidence.

Invalid Delivery blockers:
- Missing PB map.
- Missing deletion burden for removed/merged/compressed rules.
- Missing companion-file check.
- Missing actual test status.
- Claiming generated package/upload/deploy/runtime activation without evidence.
- Delivering snippets-only when replacement package is expected.
- Moving protected behavior only to lower-authority files without instruction trigger.
- Adding active file without distinct owner role and manifest/update plan.
- Creating corrected_/final_/v2_/backup_/old_ active files instead of canonical filenames.

Patch State Machine:
- Audit: inspect basis, current package, gaps, risks, source/tool evidence.
- Patch Plan: list target edits, affected PBs, tests, delivery artifacts, rollback/exclusion.
- Build: make edits/package.
- Auditor Pass: independent check against Patch Lock, PB map, deletion burden, companions, tests, delivery matrix.
- Delivery: provide full files/package/report and upload/removal instructions.

Builder/Auditor split: builder may propose/patch; auditor must attack the patch for PB weakening, instruction drift, hidden file authority, missing tests, missing delivery, source dishonesty, and child propagation gaps.

Protected-file change rule: if protected_behavior_registry.md, testing_protocol.md, delivery_protocol.md, patch_lock_protocol.md, instruction_governance.md, package_state_protocol.md, or Project/GPT Instructions change, require explicit behavior diff and hard pass threshold.

Compression rule: compression is allowed only when enforceability is preserved or strengthened. Shorter text that loses trigger/action/evidence/fail condition is weakening.

Major/minor distinction: small safe edits may compress Audit→Patch Plan→Build→Auditor Pass into one report, but cannot skip PB map, deletion burden where applicable, companion check, and test status.

Child propagation check: if the system creates/patches a child GPT/project/workflow that will govern other work, ensure the child inherits relevant Patch Lock, source honesty, testing, delivery, and safety gates.

Self-modification blocker:
- Any change that alters how this system changes itself must pass Rule Admission Gate, PB-66 preservation check, protected-registry diff, companion-file check, and applicable regression/mutation tests. Missing this check = Critical FAIL.
- Do not bypass Thin Kernel, GitHub-first release state, repo-only controls exclusion, runtime activation separation, or evidence-layer honesty while adding future rules.
