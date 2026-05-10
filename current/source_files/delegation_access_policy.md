Use this file for autonomous delegation boundaries, escalation authority, and package guard obligations. Main Project/GPT Instructions remain controlling.

Purpose: enable safe autonomous delegation while preventing protected/governance drift, hidden ownership transfer, and package-scope bypass.

Delegation scope:
- Autonomous delegation is allowed only for bounded implementation subtasks that do not alter trust boundaries, ownership, or protected policy intent.
- Delegated work inherits all active package rules from current/, including testing, patch lock, delivery, and source safety requirements.
- Delegation may draft changes, but protected/governance finalization requires explicit guard validation before delivery.

Hard prohibitions:
- Do not delegate branch protection changes, repository ownership/access changes, visibility changes, secrets handling, or GitHub App permission changes.
- Do not delegate merge, auto-merge enablement, or readiness-state escalation when protected/governance files changed.
- Do not treat inactive folders as active authority during delegation.

Protected/governance upgrade guard:
- Any change touching protected/governance scope must run package guard validation and report pass/fail evidence.
- Package guard must verify active package basis is current/, manifest alignment, and protected file touch disclosure.
- Failing guard means Not Ready and blocks protected/governance delivery.

Delegation evidence requirements:
- Report changed files, protected files touched, inactive folders touched, manifest validation result, executed checks, skipped checks, and final verdict.
- Evidence must be generated from visible files and actual command outputs only.

Conflict rule:
- If delegated output conflicts with current/ rules or manifest truth, current/ and manifest win unless user explicitly overrides.
