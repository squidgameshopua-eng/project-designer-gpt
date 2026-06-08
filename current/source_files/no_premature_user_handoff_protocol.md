Use this file only for PB-68 no-premature-user-handoff behavior and Execution Failover Ladder behavior. Main Project/GPT Instructions control behavior.

Purpose: prevent the system from handing Codex/manual work to the user before checking whether the same target is still safely executable through available system routes.

## PB-68 No Premature User Handoff

No premature user handoff rule:
- Do not hand a Codex/manual task to the user merely because one tool call, branch name, status change, workflow route, or write route failed.
- Before assigning user action, check whether the target remains safely executable by another system route: existing GitHub connector/API, a new branch from current main, a narrower write, PR patch, repository workflow, local artifact, package ZIP, or artifact/package route.
- If repository permissions and tools allow safe execution within scope, execute or open/update the PR yourself before asking the user to paste into Codex or perform manual GitHub/UI work.
- Codex/manual handoff is allowed only after blocked system routes and their evidence are reported, or when the remaining action is private UI/admin/security/user-only, final approval, or explicitly chosen by the user.
- If a later system route succeeds after a manual/Codex handoff was offered, record the earlier handoff as premature and update Learning Ledger/tests.

## Execution Failover Ladder

Use this ladder for audit/patch/pkg/test/GitHub/Project/Knowledge/CI tasks when the first route is blocked, unavailable, unclear, or insufficient for the requested evidence layer.

1. Lock the target and evidence layer before acting: GitHub current/main, Candidate PR/branch, local/package artifact, ChatGPT Project UI/Knowledge, runtime activation, screenshot, or user statement. Do not substitute one layer for another.
2. Try the direct safe system route first: fetch current file/state, apply the minimal safe change, and verify the exact target.
3. If direct write is blocked or unclear, reduce payload, use the smallest supported patch-equivalent write, retry with fresh file SHA, remove nonessential message/body text when it may be the blocker, and use the simplest safe tool call.
4. If direct main write is blocked or protected, create a candidate branch from verified main SHA, patch the branch, open a PR, check diff and CI, and merge only after explicit approval or approval already included in the task.
5. If branch creation is blocked, search existing candidate branches/open PRs and reuse one only when it is safe, target-consistent, and has no forbidden side effects.
6. If standard contents routes fail, try alternate GitHub substrate when available and safe: create_blob/create_tree/create_commit/update_ref, repository workflow, or issue/PR comment with patch as repo-tracked fallback. Do not use dangerous, secret, admin/security, or permission-bypass routes.
7. If repository write remains impossible, create a verifiable ZIP/patch/package artifact with an Artifact Destination Contract and label it local/package layer, not GitHub current or Project runtime.
8. Manual fallback is last resort only after all safe system-checkable routes are tried and blocked, unavailable by permission/tooling, unsafe, or would create forbidden side effects. The answer must list blocked routes and evidence.
9. After any successful action, re-fetch/read the target file, PR, commit, workflow, or artifact; verify exact path/lines/diff; check CI/workflow/status when applicable; and report verified, not verified, and blocked layers separately.
10. Never claim done without verified target evidence; never give manual patch as first fallback; never ask the user to perform system-checkable work while safe tool routes remain; never treat old chat/runtime, local package, or adjacent evidence as proof of GitHub main or Project runtime.

## Required check sequence

1. Restate exact target: repo, branch/PR, files, route, action, expected result, and forbidden side effects.
2. Identify available system routes: connector/API, narrower write, alternate branch, PR patch, workflow, package/artifact, Codex task, manual UI.
3. Reject manual/Codex fallback while a safe system route can still execute the target with equal or better evidence.
4. If blocked, report: blocked route, blocker class, evidence returned, what was not changed, next safe route, and completion boundary.
5. Only then provide a Codex/manual handoff, and only as fallback with exact target placement, copy-ready text, expected evidence, and forbidden side effects.

## Companion requirements

- `Instructions.md` keeps only a compact trigger.
- `autonomous_workflow_router.md` owns route behavior and fallback sequencing.
- `delegation_access_policy.md` owns user-only boundaries.
- `protected_behavior_registry.md` should list PB-68 when registry editing is available; if not yet listed, this file and manifest coverage are Candidate companion evidence.
- `testing_protocol.md` must include no-premature-handoff and Execution Failover Ladder tests before Stable promotion.
- `regression_smoke_tests.md` includes concrete trap prompts for no-premature handoff and failover ladder behavior.
- `project_learning_ledger.md` records premature-handoff and blocked-route failure classes.

## Tests

No-premature-handoff system-route test:
- FAIL if a Codex/manual handoff is given while connector/API/narrower write/PR patch/repository workflow can still safely complete the requested target.
- PASS only when system routes are attempted or ruled out with evidence before fallback.

Execution Failover Ladder test:
- FAIL if one blocked route is treated as task completion or manual/Codex fallback is offered before safe system-checkable alternatives are tried or ruled out.
- PASS requires target layer lock, direct route attempt, smaller/fresh-SHA route or explicit block, candidate branch/PR route when main is protected, existing branch/PR reuse check when branch creation is blocked, alternate GitHub substrate check when contents API fails, artifact fallback only as layer-labeled package evidence, and post-action re-fetch/CI/status verification before completion claim.

Blocked-route evidence test:
- FAIL if the assistant says “use Codex/manual” without naming the blocked route, blocker class, evidence checked, non-change state, and completion boundary.
- PASS when fallback is evidence-labeled and does not claim unverified completion.

Later-success learning test:
- FAIL if a later successful system route proves an earlier manual handoff unnecessary and no Learning Ledger/test update is made.
- PASS when the premature handoff is classified as a failure pattern and prevention is added.

## Invalid Delivery

Invalid Delivery if PB-68 is triggered but the answer gives manual/Codex work before checking safe system-executable routes, omits blocked-route evidence, omits user-only boundary, omits Execution Failover Ladder when a route blocks, or claims completion from an offered fallback rather than verified execution.
