Use this file for Counterexample-Guided Improvement / CEGIS across project design, package edits, prompts, tests, and delivery routes.

Purpose: prevent premature acceptance of a candidate solution by searching for counterexamples, repairing them, and retesting until no known blocker remains.

CEGIS loop:
1. Candidate: state the proposed mechanism, patch, prompt, route, or package change.
2. Specification: list explicit requirements plus Hidden Requirements Mining outputs, protected behaviors, invariants, CI gates, and forbidden outcomes.
3. Counterexample search: look for cases where the candidate fails, including missing companion files, manifest drift, instruction limit overflow, stale runtime claims, user-guessing UI steps, unsafe route choice, source mismatch, prompt injection, and protected behavior weakening.
4. Attack examples: create concrete prompts, file states, PR states, UI states, and evidence-layer conflicts that could disprove the candidate.
5. Repair: adjust the candidate with the smallest sufficient fix that resolves the counterexample without causing a worse tradeoff.
6. Retest: rerun validators, linter, smoke tests, mutation checks, and evidence checks relevant to the repaired candidate.
7. Stop: stop only when no known counterexample remains, the remaining issue is explicitly blocked, or the route is unsafe/out of scope.

Counterexample classes:
- Requirement counterexample: a user requirement is not implemented or is implemented only locally when a global rule was required.
- Protected-behavior counterexample: Patch Lock, Kernel, Artifact Destination Contract, Repo-only Controls Exclusion, Runtime Activation Check, Cost/Capability, Free-Route Fallback, No Secrets, User Work Firewall, Execution Failover, or Auditor Pass is weakened.
- Manifest counterexample: an active source file exists outside active_source_files or a manifest-listed file is missing.
- UI handoff counterexample: the user still has to guess link, screen, field, paste text, submit action, wait condition, post-run action, result, evidence, or forbidden side effects.
- Evidence counterexample: the answer claims GitHub, UI, Knowledge, runtime, package, CI, or deployment state without checked evidence.
- Source counterexample: lower-authority, stale, inaccessible, or unofficial material overrides active truth or verified sources.
- Route counterexample: paid, unavailable, unsafe, manual, or high-user-work route is selected when a safe free/system route exists.

Repair rules:
- Prefer the smallest repair that satisfies the full specification and preserves the minimum viable kernel.
- If a counterexample reveals a recurring class, update tests, templates, registry, or Learning Ledger, not only the local patch.
- If repair would exceed scope or safety, stop and report Blocked with evidence and the next safe route.

Reporting rule:
For non-trivial work, include the strongest counterexample found, how it was repaired, what was retested, and what remains unverified.
