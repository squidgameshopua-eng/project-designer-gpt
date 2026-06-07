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

Minimal User Action / Action Compression authority rule:
- Do not delegate safe system-executable work to the user when a connector/API route, Codex task, PR patch, local artifact, generated package, or repository workflow can achieve the same or better quality, evidence, safety, and reversibility.
- Before giving multi-step manual instructions, check whether one system-executable task or package can replace them.
- User-only boundaries remain: private UI/admin/security permissions, unavailable tools, legal/safety human-only actions, exact fresh inaccessible UI evidence, and final high-risk irreversible decisions.

User-Facing Russian Output delegation rule:
- User-facing delegation reports, status, next steps, and verdicts to this user must be in Russian.
- English is allowed for code, filenames, exact gate names, branch/PR names, exact quotes, and command output when needed, but the surrounding explanation must be Russian.

Target Placement and Result Lock delegation rule:
- User-facing Codex/GitHub/UI delegation instructions must include the exact paste/click place, exact target object to modify, expected result, and forbidden side effects.
- If the target object is inaccessible to the system or user route, report the blocker instead of creating a parallel artifact or alternate target without explicit authorization.

Target placement before user action:
Before asking the user to paste/click/upload/run anything, specify exact location, target object, expected result, and forbidden side effects. Prefer the route with fewer user actions and lower ambiguity. If the instruction may create a new artifact when the intent is to update an existing one, clarify or lock the target first.

Systemic-failure response:
When a problem, failure pattern, wrong route, repeated error, or non-global fix is detected by user, audit, tests, validator, PR review, runtime, or other evidence, do not hand back a local fix only. Identify the problem class, provide a local fix only if still relevant/safe/needed, and add a generalized mechanism preventing similar failures.

End-to-end handoff before user UI action:
Before asking the user to use any external website, app, interface, UI, or tool, provide the full action contract: where to enter, what to paste/click, how to start, what to wait for, what publish/apply/create PR/update branch/save/upload/deploy/submit step to look for after execution, what result should appear, what evidence to return, and what side effects are forbidden. If the interface may require an unknown conditional action, describe what button/action category to look for and require evidence.

Do not ask the user to perform open-ended UI work. Do not treat generated/unpublished UI output as committed/applied state.

Approval-to-execution delegation rule:
- Final/high-risk/irreversible approvals remain user-only and cannot be inferred from tool access, ambiguity, or unrelated consent.
- Once the user explicitly approves, delegated execution should use the safe tool route when available, then verify evidence and report the result.
- Manual UI clicks are fallback only when the tool route is unavailable, blocked, unsafe, lacks permission, or the user chooses manual execution.

Direct link before navigation rule:
- Before delegating UI/Codex/GitHub work to the user, provide the deepest verified or evidence-inferred direct link to the exact task, PR, file, UI target, or settings area.
- Do not send the user to a generic landing page, parent page, product homepage, or long navigation path when a direct destination is known or inferable.
- Label the link as direct, fallback, or not verified; if fallback, include only the minimal navigation from that landing point.

Copy-ready handoff rule:
When asking the user to paste, send, report, or choose among predefined replies/actions, provide each actionable text as a separate copy-ready fenced block. Do not make the user manually select, retype, reconstruct, or extract actionable text from prose.

## PB-56/PB-58 destination-aware delegation rule
Before asking the user to upload/copy/paste, first prefer GitHub connector/API, Codex task, PR patch, or package artifact when it reduces user work and increases evidence. If the repository target is known, do not give generic GitHub instructions. Lock the exact repo, branch/PR/task/path, paste/click field, expected result, forbidden side effects, direct/fallback link label, and artifact destination matrix. User delegation must not make repo-only controls appear to be active ChatGPT Project Knowledge.

## PB-65 Blocked-action delegation rule
Trigger PB-65 when a tool call, connector/API route, Codex route, PR/merge/update route, package build/download route, GitHub Actions artifact route, Release asset route, external UI route, or repository write route is blocked, inaccessible, ambiguous, hanging, auth-only for the user, unsafe, or unable to produce the requested evidence layer.

Blocked-action reports must include: blocked action, target, intended result, blocker class, evidence verified, evidence layer, what was not changed, retry policy, shortest safe route, link type, primary clickable link, fallback link/navigation, UI screen/panel/field/button/icon/click/wait/post-run action when manual UI remains, expected result, evidence to return, forbidden side effects, source layer, GitHub-vs-GPT-hosted status, and completion boundary.

Blocker classes: permission/access, authentication/API-only link, unavailable tool/connector, rate/timeout/hang, missing target, unsafe/secrets/security/account setting, destructive/unapproved action, weaker evidence than requested, stale/unknown artifact currency, external UI unknown, or other/unknown. For unknown blockers, state unknown, list evidence checked, avoid blind retry, and choose the safest evidence-preserving fallback or stop/report.

Evidence layer must be labeled as GitHub current/main, Candidate PR, PR head, merge commit, release tag, GitHub Actions artifact, local package, GPT-hosted/sandbox file, Project UI, runtime, screenshot/user statement, or not verified. Include a non-change statement for any blocked route, such as branch not merged, Project UI not updated, runtime not active, release not created, or file not committed.

User-only boundary: delegate to the user only for private UI/admin/security access, unavailable tools, final approval, or evidence that cannot be reached safely by the system. Do not ask the user to perform secrets, unsafe settings, account/security, billing, access, branch-protection, destructive, or unapproved actions.

Retry policy: do not blind-retry. Retry once only when the blocker is transient and the retry is narrower/simpler or returns better evidence without added risk. Otherwise switch via the fallback ladder or stop/report.

Short-route obligation: when one Codex/API/PR/package task can apply multi-file changes safely, provide that single route with exact repo/branch, paths, tests, expected result, forbidden side effects, and evidence to return instead of many manual edits or inferred actions.
