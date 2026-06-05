# Proposed PB-48 User-Facing Russian Output Gate

Evidence layer: GitHub branch `pb48-russian-output-gate`.

Purpose: prevent future drift where the system replies to the Russian-speaking user with English headings, verdicts, next steps, or status reports.

Required patch target:
- `current/instructions/Instructions.md`
- `current/source_files/protected_behavior_registry.md`
- `current/source_files/testing_protocol.md`
- `current/source_files/output_templates.md`
- `scripts/validate_package_guard.py`

Required behavior:

```text
PB-48 User-Facing Russian Output Gate: all user-facing answers to this user must be in Russian. Technical identifiers, filenames, code, exact gate names, GitHub branch names, PR titles, and quoted source text may remain in English when needed, but conclusions, explanations, next steps, status reports, and verdicts must be in Russian.
```

Instruction-level wording:

```text
User-facing outputs in Russian; technical IDs/quotes may stay EN; child EN.
```

Testing requirement:

```text
PB-48 User-Facing Russian Output Gate tests:
- Russian user-facing output test: FAIL if conclusions, next steps, status reports, or verdicts to this user are primarily in English when the user communicates in Russian.
- Technical identifier allowance test: PASS allows English for code, filenames, exact gate names, branch names, PR titles, exact source quotes, and command output when needed, if the user-facing explanation is Russian.
- Audit/report language test: FAIL if an audit report intended for the user uses English headings/verdicts without Russian explanation or translation.
```

Validator requirement:

```text
scripts/validate_package_guard.py must require PB-48 and the phrases:
- User-Facing Russian Output Gate
- User-facing outputs in Russian
- User-facing Russian
- Russian user-facing output test
```

Candidate only. This file is not an active Knowledge/source file and does not by itself change runtime behavior. It exists to preserve the proposed patch after the write route could not safely update all protected files in one pass.