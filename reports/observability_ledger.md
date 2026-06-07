# Observability Ledger

Destination: reports/. Repo-only evidence ledger. Do not upload as active ChatGPT Project Knowledge.

Purpose: record observed behavior, evidence layer, runtime boundaries, rollback decisions, and anti-regression actions after releases or audits.

| Date | Release/PR | Observed behavior | Evidence layer | Runtime / GitHub / UI / local / user statement | Affected PB-ID | Action taken | Regression test added | Rollback needed |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## Entry template

- Date:
- Release/PR:
- Observed behavior:
- Evidence layer:
- Runtime, GitHub, UI, local, or user statement:
- Failure/success class:
- Affected PB-ID:
- Was Project runtime activation directly verified?
- Action taken:
- Regression test added or updated:
- Rollback needed:
- Remaining risk:

## Rules

- Do not infer production telemetry from local tests, PR status, external evals, or release reports.
- Runtime behavior requires runtime evidence: new Project chat, activation handshake, UI evidence, logs/traces if integrated, or explicit user-provided runtime evidence.
- GitHub current/ and Candidate PR evidence do not equal ChatGPT Project runtime active state.
- Rollback needed must name the target layer: GitHub Stable, Candidate PR, Project UI, local package, or runtime instruction/source state.
