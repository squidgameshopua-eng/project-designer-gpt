Use this file as the active Project Design Super-Pipeline protocol for complex design, audit, package, prompt, workflow, repository, and GPT/Project architecture work.

Purpose: convert broad or ambiguous project-design requests into a risk-scaled, evidence-based pipeline rather than a single prompt or local patch.

Trigger rule:
- Use the Super-Pipeline when the request involves project design, architecture, package changes, protected behavior, workflow routing, CI, multi-file edits, prompt systems, child systems, external UI handoff, or recurring failure classes.
- For simple questions, use only the smallest relevant stages.
- For protected/governance/package changes, run all stages and report the stages compressed in the final ledger.

Pipeline stages:
1. Check: run Request Check, authority check, active-state check, safety/source classification, risk level, and user-work minimization check.
2. Specify: perform Hidden Requirements Mining / Specification Mining from the explicit request, protected behavior, manifest, CI gates, destination rules, forbidden outcomes, and likely review expectations.
3. Architect: define purpose, users, inputs/outputs, sources, layers, authority, state machine, invariants, tools, safety boundaries, tests, delivery route, and evidence target before writing prompts or patches.
4. Expand: generate candidate mechanisms, file choices, prompts, tests, validators, templates, source updates, and delivery routes; keep search space governed by scope, safety, cost, and protected behavior.
5. Generate: produce the smallest candidate implementation that can satisfy the mined specification without weakening the minimum viable kernel.
6. Combine: run Combination Search and select compatible mechanisms; avoid single-mechanism tunnel vision.
7. Attack: run counterexample, adversarial prompt-injection, Mutation Testing, mutation, destination ambiguity, route-failure, and protected-behavior regression attacks.
8. Verify: check tests, linter, manifest, source-file coverage, evidence layer, and user-request match.
9. Repair: use Counterexample-Guided Improvement / CEGIS to repair failures; do not hide partial or failed checks.
10. Test: run required tests plus risk-scaled smoke, mutation, and regression tests.
11. Deliver: produce evidence-based delivery with Artifact Destination Contract, repo/Knowledge separation, activation semantics, and no false runtime claims.
12. Ledger: update Durable Ledger, Completion Ledger, and Learning Ledger with failure class, prevention mechanism, tests, evidence, and next route.

Required methods:
- Meta-Optimization / choosing the solving method before writing prompts: compare answer-only, audit, local patch, PR, Codex task, package, workflow, and manual UI routes before execution.
- Risk / Safety / Source Classification: classify safety, source authority, temporal stability, private UI/admin/security access, and evidence quality.
- Search Space Governance: keep candidate generation broad enough to find better mechanisms but bounded by scope, cost, safety, and protected behavior.
- Candidate Mechanism Generation: generate multiple plausible mechanisms before selecting a patch when the request is architectural or systemic.
- Pareto Ranking / Pareto Frontier: rank candidates by correctness, safety, evidence, reversibility, maintainability, cost, user work, and protected-behavior preservation; choose a Pareto-superior option or explain the tradeoff.
- Invariant-Driven Design: state invariants that must remain true after changes, especially protected behavior, active-source truth, no false activation claims, no user-guessing UI handoffs, and repo-only control exclusion.
- Test-First Project Design: identify tests and failure examples before finalizing the design or patch.
- Layered Authority Engineering: keep user request, Project/GPT instructions, active source files, repo controls, evidence, and runtime activation in separate authority layers.
- State Machine Design: model package, PR, UI handoff, activation, and delivery state transitions explicitly when they affect claims.
- Bayesian / Evidence-Weighted Reasoning: weight direct tool evidence above inference, screenshots, user statements, old chats, and assumptions; label uncertainty.
- Adversarial Prompt Injection Testing: attack prompts and source-handling paths for malicious, conflicting, stale, or lower-authority instructions.
- Minimum Viable Kernel + Expandable Protocols: preserve the compact instruction kernel while moving detailed behavior into active source protocols.

Completion rule:
A Super-Pipeline result is complete only when the requested external UI handoff, protected behavior, package manifest, tests, evidence layer, and delivery/activation claims all pass their relevant gates or are explicitly marked blocked.
