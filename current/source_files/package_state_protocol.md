Use this file only for active package state, continuity, obsolete-file handling, and branch drift control. Main Project/GPT Instructions control behavior.

Active package basis: current Project/GPT Instructions plus active upload/source files from the latest delivered package. Old chats, ZIPs, manifests, changelogs, screenshots, and superseded files are evidence only unless explicitly reactivated by the user.

Repository current precedence: when the authorized GitHub repository is accessible, use repository `current/` as the default source of truth for package audits and source-state comparisons. Check repository `current/` before drawing conclusions from local runtime files, chat uploads, File Library results, screenshots, old chats, or archive material. Treat those non-repository layers as mirrors/evidence unless repository access is unavailable or the user explicitly overrides the source.

Before patching, identify: active instruction source; active file list; changed files; unchanged companion files; obsolete/remove files; optional/non-active evidence; missing material. If active basis is unclear and blocks reliable patching, output More Source Material Required or audit-only limitations.

Do not merge old branches into governance by default. Treat them as evidence candidates. Reactivate old content only after checking conflicts, protected behavior impact, current source status, and package continuity.

Package state labels: active; changed; unchanged companion; new active; optional; evidence-only; obsolete/remove-exclude; missing/unavailable; generated this turn.

Current package report for major revisions: instruction character count; instruction limit used; active files; changed files; new files; removed/excluded files; smoke-test file/status; source facts checked date; screenshot/UI evidence; unresolved limitations; verdict.

Canonical names: active files use durable snake_case.md or Instructions.md. Do not use corrected_, final_, draft_, v2_, backup_, old_, or superseded suffixes/prefixes for active upload files.

Obsolete handling: exclude obsolete/duplicate/old files from ZIP and list them under Remove/exclude from upload. Do not silently keep older files that compete with current rules.

Continuity rule: when a package depends on companion files, include complete current set, not only changed files. Unchanged companion files prevent accidental deletion during upload replacement.

File-count rule: stay within known plan limits. For Plus Projects, official OpenAI source currently lists 25 files per project and 10 files per upload batch; if UI evidence conflicts, separate official source from UI evidence.

Drift rule: if active file names differ from internal references, fix names/references in same pass or mark Not Ready. If old references remain intentionally, explain their non-active evidence status.

Child propagation: child systems that create packages must include active-state truth, canonical names, obsolete exclusion, complete-package continuity, Patch State Machine, Builder/Auditor split, and regression smoke-test equivalents.

## Operation State
Track operation state separately:
- planned
- attempted
- evidence returned
- committed
- compared
- failed
- switched route
- user-only blocked
- verified

## PB-56/PB-57/PB-59 layered artifact state rule
Keep these layers separate in every package/state claim:
- ChatGPT runtime active basis: saved Project Instructions plus visible Project source/Knowledge files in the current/new runtime chat.
- GitHub Stable basis: repository `current/` plus `current/package_manifest/package_manifest.json` on main/current stable branch.
- Candidate PR basis: unmerged PR branch/diff and its validation evidence; not Stable until merged/promoted.
- Local package basis: generated local files/ZIPs; evidence only until uploaded/committed/promoted.
- Evidence-only basis: old branches, old chats, old ZIPs, screenshots, reports, archives, deliveries, and user statements until verified in the target layer.
Repo-only controls (`package_manifest.json`, `package_linter.py`, scripts, workflows, reports, guides, Codex tasks, archives, deliveries, ZIPs) are not ChatGPT runtime active Knowledge unless the user explicitly requests non-active audit/reference upload.

GitHub-first self-system release rule:
For system-development changes, GitHub current/ is the Stable source of truth when verified. Candidate PRs, local packages, old chats, screenshots, reports, and ZIPs are not Stable until promoted through manifest/linter/test/audit/release verification. Runtime active state requires Project UI update plus new-chat activation check. Rule Admission Gate and PB-66 must be preserved before any self-system release is promoted.
