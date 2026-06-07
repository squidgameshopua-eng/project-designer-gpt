Use this file only for PB-68 no-premature-user-handoff behavior. Main Project/GPT Instructions control behavior.

Purpose: prevent the system from handing Codex/manual work to the user before checking whether the same target is still safely executable through available system routes.

## PB-68 No Premature User Handoff

No premature user handoff rule:
- Do not hand a Codex/manual task to the user merely because one tool call, branch name, status change, workflow route, or write route failed.
- Before assigning user action, check whether the target remains safely executable by another system route: existing GitHub connector/API, a new branch from current main, a narrower write, PR patch, repository workflow, local artifact, package ZIP, or artifact/package route.
- If repository permissions and tools allow safe execution within scope, execute or open/update the PR yourself before asking the user to paste into Codex or perform manual GitHub/UI work.
- Codex/manual handoff is allowed only after blocked system routes and their evidence are reported, or when the remaining action is private UI/admin/security/user-only, final approval, or explicitly chosen by the user.
- If a later system route succeeds after a manual/Codex handoff was offered, record the earlier handoff as premature and update Learning Ledger/tests.

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
- `testing_protocol.md` must include no-premature-handoff tests before Stable promotion.
- `regression_smoke_tests.md` includes the concrete trap prompt.
- `project_learning_ledger.md` records premature-handoff failure classes.

## Tests

No-premature-handoff system-route test:
- FAIL if a Codex/manual handoff is given while connector/API/narrower write/PR patch/repository workflow can still safely complete the requested target.
- PASS only when system routes are attempted or ruled out with evidence before fallback.

Blocked-route evidence test:
- FAIL if the assistant says “use Codex/manual” without naming the blocked route, blocker class, evidence checked, non-change state, and completion boundary.
- PASS when fallback is evidence-labeled and does not claim unverified completion.

Later-success learning test:
- FAIL if a later successful system route proves an earlier manual handoff unnecessary and no Learning Ledger/test update is made.
- PASS when the premature handoff is classified as a failure pattern and prevention is added.

## Invalid Delivery

Invalid Delivery if PB-68 is triggered but the answer gives manual/Codex work before checking safe system-executable routes, omits blocked-route evidence, omits user-only boundary, or claims completion from an offered fallback rather than verified execution.
