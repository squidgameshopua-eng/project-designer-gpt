Use this file for autonomous delegation boundaries, escalation authority, and package guard obligations. Main Project/GPT Instructions remain controlling.

Purpose: enable safe autonomous delegation while preventing protected/governance drift, hidden ownership transfer, and package-scope bypass.

Instruction-vs-question rule:
- Treat explicit work instructions as execution requests, not clarification-only prompts, unless the user asks a direct question.
- Do not reinterpret an instruction as approval to expand scope beyond stated constraints.

Default routing rule reference:
- Use current/source_files/autonomous_workflow_router.md as the default routing rule for non-question work requests, including route selection, fallback behavior, and final status framing.
- Apply the router PR-state fallback rule, including Candidate PR handling and immediate read-only audit fallback when write/status-change routes are stuck.

Autonomous execution permissions for non-question work requests:
- Autonomous create/edit/delete/rename/move of files is allowed inside authorized repo scope when required to satisfy the request.
- Autonomous local commit, branch work, Draft PR updates, PR audit updates, and update-existing-PR operations are allowed for implementation delivery.
- These permissions do not override protected/governance/destructive/access gates.

Risk classes:
- low-risk: content or automation changes with no trust-boundary, ownership, access, or destructive impact.
- governance: policy/protocol/rules changes that affect behavior control, testing gates, or delivery rules.
- protected: files and flows that enforce safety, authority boundaries, patch locks, package truth, or release controls.
- destructive: deletion, rollback, irreversible transformations, or history rewriting risk.
- access: repository/org access, secrets, visibility, ownership, permissions, branch protection, or app authorization scope.

Low-risk automation gate:
This rule does not permit GitHub PR merge, auto-merge, marking draft PRs ready for review, branch deletion, branch protection changes, or access changes.
- Low-risk changes may proceed through normal automation gates only after package guard validation PASS and no conflicting protected/governance/destructive/access triggers.

Protected/governance/destructive gate:
- Any protected, governance, or destructive touch requires explicit package guard validation evidence before delivery; missing evidence = Not Ready.
- Destructive actions require explicit user instruction for that destructive step; no inferred destructive approval.

Access hard stop:
- Never autonomously change branch protection, repository access, visibility, ownership, secrets, or GitHub App permissions.
- Access-class requests require explicit human approval and are out-of-scope for autonomous execution by default.

Admin/security evidence rule:
- Branch protection, repository visibility, GitHub App permissions, Codex Security, collaborators, secrets, rulesets, bypass permissions, and required status checks are access/admin/security facts.
- Do not claim these settings are configured, enforced, disabled, or safe unless directly verified by accessible tool output or fresh visible UI evidence.
- If direct verification is unavailable, report the setting as NOT VERIFIED and provide the smallest exact user UI path to check it.

End-audit rule:
- End every protected/governance delivery with an audit summary including changed files, protected files touched, inactive folders touched, validation result, checks run, skipped checks, and final verdict.

No implicit approvals:
- Silence, ambiguity, prior unrelated approvals, or tool capability do not count as approval to bypass gates.
- If a required approval is absent, stop at Not Ready and report the blocking condition.

Conflict rule:
- If delegated output conflicts with current/ rules, package manifest truth, or explicit user constraints, the stricter applicable rule wins unless the user explicitly overrides within allowed authority.

User-work minimization authority rule:
- Delegation means the system performs all safe tool-checkable work itself before assigning any work to the user.
- Do not route ordinary verification, source comparison, PR inspection, manifest checks, or already-visible uploaded-file checks back to the user.
- User action is allowed only for unavailable tools, exact private UI/admin/security states, final high-risk decisions, or actions that platform permissions prevent the system from performing.
- If the user points out unnecessary manual work, treat it as an anti-loop failure and patch the workflow or provide the smallest corrected route.

