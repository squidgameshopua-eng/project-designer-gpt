# Release Report Template

Destination: reports/templates/. Repo-only report template. Do not upload as active ChatGPT Project Knowledge.

## Release identity

- Release ID:
- Date:
- Base commit:
- Candidate branch/PR:
- Author/tool route:
- Intended Stable target:

## Changed files

| Path | Layer | Change type | Active Knowledge? | Reason |
|---|---|---:|---:|---|
|  |  |  |  |  |

## Manifest status

- package_manifest.json checked:
- active_source_files continuity:
- file_roles coverage:
- protected_behavior_coverage:
- required_test_suites:
- release_gates:
- non-active eval/report separation:

## Linter and guard status

- package_linter.py:
- scripts/validate_package_guard.py:
- scripts/validate_rule_admission_guard.py:
- scripts/validate_external_eval_specs.py:
- scripts/build_knowledge_package.py:
- GitHub Actions status:

## Regression tests

- Regression tests selected:
- Regression tests executed:
- NOT EXECUTED tests and reason:
- New/updated tests:

## External evals

- Promptfoo spec status:
- Inspect AI status:
- Garak/HarmBench status:
- External eval result evidence layer:
- External evals do not prove runtime activation:

## Protected behavior preservation

| PB-ID | Prior owner | New owner | Status | Evidence | Risk |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Deletion / merge burden

| Removed/merged item | Controlled behavior | Replacement | Evidence | Verdict |
|---|---|---|---|---|
|  |  |  |  |  |

## Artifact Destination Matrix

| Artifact | Destination | Forbidden destination | Active? | Evidence layer |
|---|---|---|---:|---|
| Instructions.md | Project Instructions | Project Knowledge | yes after UI upload | UI/runtime only |
| Knowledge/*.md | ChatGPT Project Knowledge | Project Instructions | yes after UI upload | UI/runtime only |
| package_manifest.json | GitHub repo control | active Project Knowledge | no | repo evidence |
| package_linter.py | GitHub repo control | active Project Knowledge | no | repo evidence |
| evals/ | external eval evidence | active Project Knowledge | no | repo evidence |
| reports/ | report/evidence | active Project Knowledge | no | repo evidence |

## Runtime activation status

- GitHub Stable/current status:
- Candidate PR/local package status:
- Project UI upload status:
- New Project chat / activation handshake:
- Runtime active claim allowed? yes/no:
- Runtime activation evidence:

## Stable promotion verdict

- Promote to Stable: PASS / FAIL / BLOCKED / NOT EXECUTED
- Reason:
- Remaining blockers:
- Rollback target:

## Known limitations

- Unchecked UI state:
- Unrun external evals:
- Assumptions:
- User-only actions:
