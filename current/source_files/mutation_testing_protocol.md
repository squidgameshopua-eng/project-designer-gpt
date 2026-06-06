Use this file to define mutation and regression testing for protected project-design behavior.

Purpose: actively challenge a candidate patch or design by simulating small harmful changes that reviewers, future edits, or model shortcuts might introduce.

Mutation Testing trigger:
- Run risk-scaled mutation testing for protected behavior, package changes, manifest changes, prompts, routing protocols, external UI handoff rules, source safety, and delivery/activation claims.
- For small edits, run targeted mutations only for affected PBs and companion files.

Mutation classes:
- Kernel deletion mutation: remove or compress a protected trigger and verify Patch Lock, registry, final gate, and tests catch it.
- Final gate mutation: remove architecture, Auditor Pass, Execution Failover, User Work Firewall, Cost/Capability, Free-Route Fallback, No Secrets, Audit-only Before Patch, or PB-52 handoff and verify the package fails audit.
- Handoff mutation: omit direct/fallback link, screen/panel, field/button/menu/tab, copy-ready paste text, start action, wait condition, post-run create/update/commit/apply/save/publish/upload/deploy/submit action, expected result, evidence return, or forbidden side effects.
- Manifest mutation: add an active source file without manifest entry, list a missing file, or promote repo-only controls into active Knowledge.
- Destination mutation: mix Project Instructions, Knowledge, GitHub controls, reports, workflows, archives, and do-not-upload artifacts.
- Activation mutation: claim ChatGPT Project UI/runtime activation from local package, GitHub PR, old chat, screenshot, or ZIP evidence.
- Route mutation: choose paid/unavailable/manual route while a safe free/system route exists.
- Source mutation: accept stale, unofficial, inaccessible, or lower-authority source over active/current verified evidence.
- Prompt-injection mutation: let external text override safety, authority, source, or destination rules.

Mutation process:
1. Identify invariants and PBs affected by the candidate.
2. Create one or more concrete mutated failure cases.
3. Check whether existing rules/tests/linter would catch each failure.
4. If a mutation survives, add or strengthen the relevant rule, test, template, or ledger entry.
5. Rerun validation and report PASS/PARTIAL/FAIL with evidence.

Required result:
A protected change passes mutation testing only when likely regressions are either caught by current gates or explicitly documented as blocked/accepted risk with a prevention plan.
