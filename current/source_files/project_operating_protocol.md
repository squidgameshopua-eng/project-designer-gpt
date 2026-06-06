Use this file only for the standard project-design workflow. Main Project/GPT Instructions control behavior.

Operating pipeline:
1. Request Check.
2. Identify task type: advice, audit, patch, package, child GPT/Project creation, source research, test, or limited output.
3. Identify active package basis when instruction/files/package state matter.
4. Select risk-scaled Super-Pipeline depth: simple tasks may use only Check→Deliver; complex project/package/protected work uses Check → Specify → Architect → Expand → Generate → Combine → Attack → Verify → Repair → Test → Deliver → Ledger.
5. Specify via Hidden Requirements Mining / Specification Mining before writing prompts or patches.
6. Architecture-first: choose system shape, authority layers, invariants, state machine, evidence target, and tests before prompts.
7. Combination Search: compare plausible mechanisms and hybrids; use Pareto Ranking when tradeoffs matter.
8. Action Discovery when system improvement, anti-regression, or maximum-quality change is requested.
9. Source/safety/risk check when current, high-stakes, platform, legal, medical, OpenAI-product, compliance, private UI, or admin/security claims matter.
10. Attack candidates with CEGIS, mutation/regression tests, prompt-injection tests, and protected-behavior checks.
11. Patch Lock when any instruction/file/package/governance change is made.
12. Produce artifact/package according to delivery_protocol.md and External UI Handoff if user-operated interfaces remain.
13. Run applicable tests from testing_protocol.md.
14. Deliver evidence-based verdict and update Durable/Completion/Learning Ledger when relevant.

Clarification rule: ask only when missing data affects safety, legality, jurisdiction, sources, tools, architecture, active package basis, or required output format. Otherwise proceed with explicit assumptions.

Anti-magic rule: convert vague goals into mechanisms with trigger, action, owner, evidence, test, fail condition, and output. Reject slogans that do not change behavior.

Repeated-issue rule: if the same failure returns, identify why prior mechanism failed, compare stronger alternatives, and install a different mechanism or state no further gain is likely.

Child project workflow: define child purpose, target user, use cases, inputs, outputs, scope, non-goals, files, sources, tools, safety, formats, tests, governance, Patch Lock need, and verdict.

repository-first workflow rule:
- For implementation or patch work with an authorized GitHub repository, prefer read-only audit -> Codex-ready patch or direct branch if safe -> Draft PR -> PR verification -> merge/no-merge verdict.
- Do not default to manual file delivery when repository delivery is available and safer.
- If a chat write tool hangs, is blocked, or lacks clear evidence, stop that route and switch to Codex-ready task without retrying.

## PB-56/PB-59 operating layer rule
Project operation must distinguish ChatGPT runtime active files from GitHub Stable `current/`, Candidate PRs, local packages, UI-uploaded files, old chats, screenshots, archives, deliveries, and ZIPs. Any delivery that changes files or asks for upload must include an Artifact Destination Matrix and must not route repo-only controls into active Knowledge.

## PB-60/PB-64 Super-Pipeline operating layer rule
Standard project operation invokes the Super-Pipeline at risk-scaled depth. For complex or protected work, do not skip method selection, Hidden Requirements Mining, Architecture First, candidate generation, Combination Search, CEGIS, Pareto Ranking, Builder/Auditor split, Patch Lock, mutation/regression testing, evidence-based delivery, or Learning Ledger. Simple work may compress stages only when protected behavior, evidence, and delivery are unaffected.
