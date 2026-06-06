Use this file only for mutation testing of package behavior. Main Project/GPT Instructions control behavior.

Purpose: mutation testing for instructions, source files, tests, and package governance.

## Trigger
Run mutation testing for major package changes and any material change to triggers, protected behaviors, governance, testing, delivery, source/safety policy, manifest, active-source scope, or child-system inheritance. Use compact mutation testing for smaller edits that touch those areas.

## Mutation testing loop
1. Select targets: changed rules/files/tests plus affected companion files and PB owner-map entries.
2. Create mutants: intentionally remove, weaken, invert, relocate, or blur critical behavior.
3. Predict detection: name the test, guard, registry check, linter, or counterexample expected to catch each mutant.
4. Run/check detection with available tools or textual verification.
5. Classify result.
6. Repair surviving material mutants by strengthening rules/tests/owners or report a blocked/limited verdict.
7. Report mutation score qualitatively when exact automation is unavailable.

## Required mutation classes
- Trigger deletion or narrowing.
- Final-gate omission.
- Hidden-requirement omission.
- Evidence-layer conflation.
- Repo-only controls included as active Knowledge.
- Patch Lock bypass.
- PB owner-map removal or weakening.
- Test expectation missing or too vague.
- Source/safety check bypass.
- Child-system inheritance omission.
- Delivery destination matrix omission.
- Learning Ledger omission for recurring failure classes.

## Mutation result categories
- KILLED: an available test/check/rule detects the mutant.
- SURVIVED: the mutant is not detected and could change behavior.
- EQUIVALENT: the mutant does not materially change behavior.
- NOT RUN: required tool/material unavailable; must be labeled.
- BLOCKED: safety, permission, source, or environment prevents execution.

## Pass condition
PASS requires all material mutants killed or equivalent, and no surviving mutant that weakens safety, protected behavior, active-source scope, delivery evidence, or tests. PARTIAL requires documented NOT RUN/BLOCKED mutants and limited delivery language.

## Fail / Invalid Delivery
Invalid Delivery if mutation testing was triggered but omitted, required mutation classes are absent without rationale, surviving material mutants are ignored, repo-only/activation/evidence mutants survive, or final delivery claims full PASS with NOT RUN material mutants.

## Report template
- Target:
- Mutant:
- Expected detector:
- Result: KILLED / SURVIVED / EQUIVALENT / NOT RUN / BLOCKED
- Evidence:
- Repair if survived:
- Residual risk:
