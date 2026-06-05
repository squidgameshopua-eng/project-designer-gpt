# Proposed delivery: PB-48 User-Facing Russian Output Gate, PB-49 Minimal User Action / Action Compression Gate, and PB-50 Target Placement and Result Lock

Status: proposed companion delivery for PR #26.

## Scope
- PB-48 protects Russian user-facing output for this user while allowing English technical identifiers, filenames, code, exact gate names, branch/PR names, quoted source text, and command output when needed.
- PB-49 protects minimal user action routing by preferring one safe system-executable Codex task, connector/API route, artifact, PR patch, or generated package over multiple manual edits, clicks, uploads, screenshots, or repeated user instructions.
- PB-50 protects target placement and result locking before Codex/GitHub/UI instructions: exact place, target object, expected result, forbidden side effects, and blocker reporting when the target is inaccessible.

## Active files updated
- `current/instructions/Instructions.md`
- `current/source_files/protected_behavior_registry.md`
- `current/source_files/testing_protocol.md`
- `current/source_files/output_templates.md`
- `current/source_files/autonomous_workflow_router.md`
- `current/source_files/delegation_access_policy.md`
- `scripts/validate_package_guard.py`

## Protected behavior preservation
- PB-00 through PB-47 remain protected.
- PB-47 GitHub Instruction/Knowledge Delivery Format remains active.
- PB-48, PB-49, and PB-50 are added to the registry, instruction kernel/final gate, companion protocols, output templates, tests, and validator phrase checks.
