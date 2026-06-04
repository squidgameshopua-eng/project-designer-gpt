# Package integrity smoke checklist

Status: non-active test evidence/checklist. Do not upload as Project Source.

Use this checklist when auditing or patching the active package under `current/`.

## Required mechanical checks

1. Run `python3 package_linter.py` from the repository root.
2. Run `python3 scripts/validate_package_guard.py` from the repository root.
3. Confirm `.github/workflows/package_guard.yml` runs both checks for pull requests that change `current/**`, `package_linter.py`, the guard script, or the workflow.

## Manual review points

- Active package basis is `current/package_manifest/package_manifest.json`.
- Main instruction file is `current/instructions/Instructions.md` and remains within the configured instruction limit.
- Active source files are exactly the filenames listed in `active_source_files` and exist under `current/source_files/`.
- Protected behaviors in `current/source_files/protected_behavior_registry.md` remain preserved or strengthened.
- Routing/delegation behavior remains covered by `autonomous_workflow_router.md`, `delegation_access_policy.md`, `delivery_protocol.md`, `project_operating_protocol.md`, and `testing_protocol.md`.
- Patch Lock, Builder/Auditor split, deletion burden, evidence claims, source safety, and delivery gates are not weakened.
- Non-active folders (`archive/`, `deliveries/`, `external_sources/`, `tests/`) are not treated as active Project Sources.

## Evidence to report in PRs

- Files changed.
- Checks run and whether each passed, failed, or was not executed.
- Protected behaviors touched and preservation evidence.
- Risks, limitations, and anything requiring human/GPT review.
