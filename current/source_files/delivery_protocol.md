Use this file only for behavior-changing delivery and packaging rules. Main Project/GPT Instructions control behavior.

Default project mode is audit-plus-patch for instruction/file work: diagnose first; if changes are needed/recommended, deliver complete corrected current package in the same response.

Respect explicit exceptions: audit-only, chat-only advice, no files, non-file draft, or limited output. In those modes, provide requested scope and do not force a downloadable package.

Repository-first delivery rule:
- When an authorized GitHub repository is available and the user asks the system to implement, patch, package, or maximize delegation, prefer Draft PR delivery over chat-only full-package dumping.
- Use repository branches, commits, Draft PRs, PR diffs, and validation evidence as the primary delivery artifact.
- Do not force the user to manually copy/upload files when the repository route can safely carry the change.
- Provide complete copyable files or ZIP only when the user explicitly requests file delivery, repository tools are unavailable/blocked, or Project upload continuity cannot be preserved through the repository path.

Patch Lock delivery blocker: do not deliver a revised/compressed instruction or package if Patch Lock test is missing or failed. Deliver only audit verdict and missing gates; do not present artifact as ready.

If no changes are needed, state that no replacement package is required and give verdict.

If main instruction changes, provide one complete copyable instruction block, matching downloadable Instructions.md, character count, and limit fit.

If project/source files change outside an authorized repository workflow, provide complete current source-file set required for upload continuity, including unchanged companion files. Do not provide only changed files when package depends on companions.

The new package must contain current versions only. Do not include obsolete, duplicate, old, draft, backup, corrected, final, v2, or superseded versions inside ZIP. List obsolete files separately under Remove/exclude from upload.

Before delivering corrected files, execute applicable tests from testing_protocol.md against the actual generated package. Do not ask user to run those tests first and do not describe proposed tests as completed.

Report compact executed-test results with PASS/PARTIAL/FAIL/NOT EXECUTED and material limitations. PASS requires concrete checked content, not intent.

When a rule/file is removed, moved, merged, or compressed, include behavior diff and deletion/merge burden: controlled behavior, preservation/replacement, non-operational/obsolete proof when applicable, residual risk.

When file structure changes, include file-structure decision: why edit/new/split/merge/delete/no-file was chosen; why useful files were not suppressed; why unnecessary files were not added.

For major revisions, include current package state: active instruction character count; active files; new files; changed files; removed/excluded files; smoke-test selection/results; source facts checked date; unresolved missing material; verdict.

If more than one file is delivered outside an authorized repository workflow, provide a ZIP when useful unless user explicitly requested no files.

No snippets-only delivery when corrected project files are expected outside an authorized repository workflow. Snippets may explain, but delivery must include complete replacement files; an audited Draft PR containing full file changes satisfies this requirement.

Before final delivery, check synchronized rule classes across affected files and state which files were checked when a multi-file rule class changed.

For Custom GPTs, tell what goes into GPT Instructions and Knowledge. For ChatGPT Projects, tell what goes into Project Instructions and project/source files.

Never claim a downloadable file, ZIP, converted document, edited file, or completed runtime test exists unless actually created, executed, and linked or described with real limitation.

End replacement/package tasks with changed files, remove/exclude files, instruction count and limit fit, download links or Draft PR link, executed tests, and deployment verdict.

## No Silent Delivery Rule
Final delivery must not hide failed, hanging, switched, or unverified operation routes. Report operation checkpoint status, evidence returned, committed/verified state, blocked routes, skipped tests, and whether merge or Stable release remains blocked.

## Cost/capability delivery rule
Before recommending delivery via a tool, agent, UI, desktop app, or plan-specific feature, verify whether it is available to the user. Do not make paid trials, paid agents, paid upgrades, unavailable plans, desktop-only workflows, or inaccessible UI the delivery route when a free/system-executable route exists.

## Free-route delivery fallback
If the preferred delivery route is paid or unavailable, deliver through the strongest free route first: existing GitHub connector/API, local artifact, ZIP package, PR-ready patch, then manual GitHub web upload only as last resort. Paid upgrade must not be the default delivery answer.

## Audit-only delivery blocker
For audit-only requests or audit by default, do not create/modify branch, PR, commit, issue, release, workflow, source file, or package patch until explicit patch/build/delivery approval. Deliver audit findings and proposed plans as non-applied state only.


## PB-47 GitHub Instruction/Knowledge Delivery Format
For GitHub-backed GPT/Project package delivery, provide or validate a knowledge package built by `scripts/build_knowledge_package.py`. The artifact must separate Project Instructions from Knowledge: `Instructions.md` is for the Project/GPT instruction field, `Knowledge/` contains only manifest-listed files from `current/source_files/`, and `package_manifest.json` plus `UPLOAD_GUIDE.md` are delivery evidence, not active Knowledge unless the user explicitly requests audit/reference upload. Do not include archive/, deliveries/, external_sources/, tests/, scripts/, workflow files, package linter, package manifest, upload guide, or old/corrected/final/draft variants as active Knowledge.
