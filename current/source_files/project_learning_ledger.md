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
- A false completion or activation claim must update Evidence Claim, Runtime Activation Check, Activation Semantics, or delivery templates.
- A missing companion-file failure must update Patch Lock, protected_behavior_registry.md owner map, testing_protocol.md, or package_linter/manifest checks when appropriate.
- A protected-kernel weakening must update registry/tests and preserve the main instruction trigger.
- A prompt-injection/source failure must update source safety, authority, or adversarial testing guidance.

Anti-regression update rule:
If the same class could recur in future tasks, add a regression smoke test or mutation class unless doing so would bloat active files without changing behavior. If no durable update is added, explain why the existing gate already catches the class.

Reporting rule:
Final delivery for complex tasks should summarize the Learning Ledger entry in Done / Not done / Blocked terms and identify the evidence layer used. Do not claim runtime learning or ChatGPT Project activation from repository-only changes.

## PB-65 blocked-route failure classes
Add a Learning Ledger entry when any of these classes appears or repeats:
- Wrong link type / API URL used as user download: record requested hosting, link type given, browser result such as 401/404/auth, verified fallback, template/test updated, and whether GitHub-vs-GPT-hosted distinction was made.
- Blocked tool-write without exact manual handoff: record blocked tool/action/target, blocker class, evidence layer, non-changes, retry decision, shortest safe fallback, exact UI/download handoff, and regression test added.
- Multi-file integration described as many manual steps instead of one executable Codex/PR route: record the single route that should have been offered, why manual inference was invalid, files/rules/tests affected, and the output/router/template update that prevents recurrence.
