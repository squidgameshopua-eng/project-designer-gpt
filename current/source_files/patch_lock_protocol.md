Use this file only for Patch Lock, invalid-delivery blocking, and regression-proof package changes. Main Project/GPT Instructions control behavior.

Patch Lock trigger: any instruction/file compression, rewrite, deletion, merge, move, rename, package, governance, registry, testing, delivery, active-state, or child-system rule change.

Patch Lock required inputs: active package basis; patch_lock_protocol.md; protected_behavior_registry.md; affected companion files; testing_protocol.md; delivery_protocol.md; package_state_protocol.md when active state matters; regression_smoke_tests.md for major package changes; current official sources when material.

Active basis gate: identify current instruction, active source files, optional files, obsolete/remove files, and evidence-only old material before patching. If unclear and material, output More Source Material Required or audit-only limitations.

Behavior-ID gate: map each affected protected behavior ID before editing. Report prior location, new location, status, evidence, weakening risk, and child impact. Missing ID map = Invalid Delivery.

Deletion/merge burden gate: every removed, merged, compressed, or moved rule/file must state controlled behavior, reason for removal/merge, preservation/replacement location, and residual risk. Missing burden = Invalid Delivery.

Companion-file gate: inspect files that own, test, deliver, or propagate the changed rule class. Update them in the same pass or state why unchanged. Missing companion check = Invalid Delivery.

No autonomous compression: if instruction is near the limit, do not silently compress protected/kernel rules. First identify non-protected, obsolete, weaker duplicate, decorative, archive-only, or non-operational text. If none exists, propose file-level detail transfer or stronger replacement; do not force a ready package.

Invalid-delivery rule: a revised package must not be presented as ready if registry check, behavior diff, deletion burden, companion-file check, active-basis check, actual tests, or final verdict is missing. Output Not Ready / Invalid Delivery and list missing gates.

Kernel self-preservation: Patch Lock, authority/lower-authority-file rule, protected registry, deletion burden, active package truth, actual testing, complete delivery, child propagation, and final gate cannot be deleted, weakened, or moved only to files without a proven stronger replacement.

Child propagation: any child GPT/Project that can create, audit, rewrite, compress, package, or test instructions/files must inherit Patch Lock or a compressed equivalent in its main instruction and companion governance/testing files.

Patch State Machine for major changes: Audit → Patch Plan → Build → Auditor Pass → Delivery. The Patch Plan lists candidate mechanisms and affected PB IDs. Build creates files. Auditor Pass checks package evidence before delivery. Missing phase = Invalid Delivery unless the edit is minor and gates are compactly reported.

Builder/Auditor split: the builder may optimize wording or files; the auditor must separately inspect the built package for PB preservation, deletion/merge burden, right-sized architecture, companion sync, active-state truth, child propagation, source honesty, and executable tests.

Patch Lock output for major package changes: active basis; patch plan summary; changed files; removed/excluded files; behavior diff; deletion/merge burden; companion-file check; smoke-test selection/results; executed tests; source/date notes; instruction count; verdict.
