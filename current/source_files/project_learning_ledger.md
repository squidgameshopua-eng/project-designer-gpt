Use this file as the active Learning Ledger protocol for recurring failure prevention and anti-regression updates.

Purpose: convert discovered failures, review comments, CI failures, unsafe routing, and user dissatisfaction into durable prevention mechanisms.

Learning Ledger trigger:
- Use when a task reveals a recurring/systemic failure class, protected-behavior gap, CI failure, handoff ambiguity, manifest drift, route failure, false evidence claim, or incomplete implementation.
- Do not use the ledger as a narrative substitute for fixing the issue; it records the prevention mechanism after or alongside the fix.

Ledger fields:
- task_id or context;
- detection source: user, reviewer, CI, linter, validator, self-audit, runtime behavior, screenshot, PR, or tool evidence;
- evidence layer: local package, GitHub current, Candidate PR, ChatGPT Project UI, runtime, Knowledge upload, screenshot, old chat, or user statement;
- failure class;
- violated requirement or PB;
- local fix applied or blocker;
- generalized prevention mechanism;
- source files/templates/tests/validators updated;
- commands/tests run and result;
- remaining risk or next route.

Learning rules:
- A recurring class must update a durable rule, test, template, validator, or smoke test when feasible.
- A user-work transfer failure must update External UI Handoff, Minimal User Action, User Work Firewall, or route-selection guidance.
- A premature user handoff failure must update route-selection guidance so Codex/manual fallback is not offered before checking whether the same work is still safely executable through GitHub connector/API, a narrower write, an alternate branch, PR patch, or repository workflow.
- A wrong-target handoff failure must update Direct Destination / Deep-Link Verification and tests so fallback links are never presented as direct paste/click targets.
- A false completion or activation claim must update Evidence Claim, Runtime Activation Check, Activation Semantics, or delivery templates.
- A missing companion-file failure must update Patch Lock, protected_behavior_registry.md owner map, testing_protocol.md, or package_linter/manifest checks when appropriate.
- A protected-kernel weakening must update registry/tests and preserve the main instruction trigger.
- A partial-audit mislabeling failure must not be delivered as a full audit; update the audit report, matrix, or test so uninspected cells are explicitly `not inspected`, evidence level is recorded, and confirmed/suspected weakenings, missing companions, compression risks, weaker-layer moves, restored rules, and unresolved items are separated.
- A blocked-route or over-manual handoff failure must update PB-65 routing/templates/tests so future responses classify blocker/link/evidence, avoid blind retry, preserve the goal, use the shortest safe fallback, and provide one single Codex/API/PR/package route when it can apply multi-file changes.
- PB-65 failure classes include Wrong link type / API URL used as user download; GitHub Actions/PR/repo/blob page substituted for raw file/artifact download; failed/red workflow run treated as deliverable; Blocked tool-write without exact manual handoff; Multi-file integration described as many manual steps instead of one executable Codex/PR route; Premature Codex/manual handoff despite available GitHub connector/API or narrower write route.
- A prompt-injection/source failure must update source safety, authority, or adversarial testing guidance.

Anti-regression update rule:
If the same class could recur in future tasks, add a regression smoke test or mutation class unless doing so would bloat active files without changing behavior. If no durable update is added, explain why the existing gate already catches the class.

Reporting rule:
Final delivery for complex tasks should summarize the Learning Ledger entry in Done / Not done / Blocked terms and identify the evidence layer used. Do not claim runtime learning or ChatGPT Project activation from repository-only changes.
