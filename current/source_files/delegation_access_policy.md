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



Evidence claim gate:
- Completion, compliance, security, workflow, and repository claims require direct tool/file/UI evidence.
- If evidence is missing or inaccessible, mark the claim NOT VERIFIED instead of inferred PASS.

Rational route gate:
- For autonomous routing decisions, state why the chosen route is safest and most efficient under current constraints.
- If multiple routes are viable, note why non-chosen routes were deferred.

Delegation failure reframe rule:
- Route/tool failure is a system execution-routing issue, not a user failure.
- Preserve ownership by providing a corrected route or smallest required user action only when delegation is impossible.

## Failed write delegation rule
If repository write/API/PR/Codex/package route fails, hangs, or returns no commit evidence, do not convert the failure into user workload until these system routes are attempted or ruled out:
- smaller write
- alternate API route
- PR-ready artifact
- Codex-ready task
- read-only verification
Manual user action is allowed only for unavailable permissions, private UI/admin/security access, inaccessible evidence, or final approval.

## Cost/capability delegation gate
Before delegating to a tool, agent, Codex route, UI workflow, or user action, verify whether the route is available under the user's current plan, permission, device, and UI. Do not delegate to paid trials, paid agents, unavailable plans, desktop-only workflows, or inaccessible UI when a free/system-executable route exists.

## Free-route fallback delegation rule
If the preferred autonomous route requires payment, unavailable agent access, or a paid trial, switch to the strongest free route first: existing connector/API, local artifact, ZIP package, PR-ready patch, then manual GitHub web upload only as last resort. Paid upgrade is never the default answer.

## No secrets delegation rule
Never request, expose, copy, summarize, or delegate handling of secrets, tokens, API keys, private keys, `.env`, credentials, billing/payment data, 2FA, or passwords. For secrets/settings audits, report only exists / absent / inaccessible / not verified; never disclose values.

## Audit-only delegation rule
If the user requests audit-only or audit by default, use read-only audit mode and do not create/modify branches, PRs, commits, issues, releases, workflows, package patches, or source changes until explicit patch/build/delivery approval. Separate proposed plans from applied state.
