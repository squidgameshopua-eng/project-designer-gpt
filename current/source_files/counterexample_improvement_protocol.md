Use this file only for counterexample-guided improvement. Main Project/GPT Instructions control behavior.

Purpose: CEGIS protocol for material rules, files, architectures, tests, and packages.

## Trigger
Run CEGIS when a task creates or changes material instructions, protected behavior, governance, source/safety policy, testing, package manifests, delivery rules, child-system behavior, repository/Codex handoffs, or any architecture with non-trivial failure risk.

## CEGIS loop
1. Candidate: state the candidate rule, file, architecture, test, package, or delivery mechanism.
2. Spec: state required behavior, hidden requirements, forbidden side effects, evidence layer, and pass/fail criteria.
3. Generate counterexamples: produce concrete cases that should fail if the candidate is weak.
4. Attack: check the candidate against each counterexample.
5. Repair: revise the candidate, companion files, tests, or delivery evidence to address surviving counterexamples.
6. Re-test: rerun the counterexample set and applicable regression/mutation tests.
7. Verdict: PASS only when all material counterexamples are handled or explicitly demoted with rationale and evidence.

## Counterexample classes
- Omission: required trigger, owner, companion, destination, test, or evidence is missing.
- Ambiguity: wording allows multiple unsafe or weaker interpretations.
- Overbreadth: rule blocks safe work or creates unnecessary user work.
- Underbreadth: rule fails on a material variant of the task.
- Adversarial/misuse: user prompt or route pressure tries to bypass safety, PBs, Patch Lock, or evidence.
- Layer mixing: local package, Candidate PR, GitHub main, Project UI upload, runtime active state, screenshot, and user statement are conflated.
- Source/evidence: current or high-stakes claim is made without required source verification.
- Repo-only leakage: manifest, scripts, workflows, tests, reports, archives, deliveries, ZIPs, or controls are treated as active Project Knowledge.
- Regression: old PB behavior or smoke-test behavior is weakened.
- Child propagation: child GPT/Project/package misses inherited governance, tests, safety, or delivery rules.

## Repair requirements
Repairs must alter enforceable behavior, not just add aspirations. A repair must name the changed rule/file/test, owner map, protected behavior impact, evidence required, and residual risk.

## Minimum counterexample set
For material package changes, include at least one omission, one ambiguity, one layer-mixing, one repo-only leakage, one PB regression, one evidence/source, and one delivery-destination counterexample. Add safety, child-propagation, and repository/Codex counterexamples when relevant.

## Pass condition
PASS requires no surviving material counterexample, updated companions/tests when needed, and an evidence-backed verdict. PARTIAL requires explicitly listed unresolved cases and why delivery remains limited. FAIL blocks final delivery.

## Invalid Delivery conditions
Invalid Delivery if CEGIS was triggered but absent, counterexamples are only generic labels without concrete cases, material surviving counterexamples are ignored, repairs are not re-tested, or final verdict claims PASS without evidence.
