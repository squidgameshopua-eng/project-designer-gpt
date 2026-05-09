Use this file only for behavior-changing delivery and packaging rules. Main Project/GPT Instructions control behavior.

Default project mode is audit-plus-patch for instruction/file work: diagnose first; if changes are needed/recommended, deliver complete corrected current package in the same response.

Respect explicit exceptions: audit-only, chat-only advice, no files, non-file draft, or limited output. In those modes, provide requested scope and do not force a downloadable package.

Patch Lock delivery blocker: do not deliver a revised/compressed instruction or package if Patch Lock test is missing or failed. Deliver only audit verdict and missing gates; do not present artifact as ready.

If no changes are needed, state that no replacement package is required and give verdict.

If main instruction changes, provide one complete copyable instruction block, matching downloadable Instructions.md, character count, and limit fit.

If project/source files change, provide complete current source-file set required for upload continuity, including unchanged companion files. Do not provide only changed files when package depends on companions.

The new package must contain current versions only. Do not include obsolete, duplicate, old, draft, backup, corrected, final, v2, or superseded versions inside ZIP. List obsolete files separately under Remove/exclude from upload.

Before delivering corrected files, execute applicable tests from testing_protocol.md against the actual generated package. Do not ask user to run those tests first and do not describe proposed tests as completed.

Report compact executed-test results with PASS/PARTIAL/FAIL/NOT EXECUTED and material limitations. PASS requires concrete checked content, not intent.

When a rule/file is removed, moved, merged, or compressed, include behavior diff and deletion/merge burden: controlled behavior, preservation/replacement, non-operational/obsolete proof when applicable, residual risk.

When file structure changes, include file-structure decision: why edit/new/split/merge/delete/no-file was chosen; why useful files were not suppressed; why unnecessary files were not added.

For major revisions, include current package state: active instruction character count; active files; new files; changed files; removed/excluded files; smoke-test selection/results; source facts checked date; unresolved missing material; verdict.

If more than one file is delivered, provide a ZIP when useful unless user explicitly requested no files.

No snippets-only delivery when corrected project files are expected. Snippets may explain, but delivery must include complete replacement files.

Before final delivery, check synchronized rule classes across affected files and state which files were checked when a multi-file rule class changed.

For Custom GPTs, tell what goes into GPT Instructions and Knowledge. For ChatGPT Projects, tell what goes into Project Instructions and project/source files.

Never claim a downloadable file, ZIP, converted document, edited file, or completed runtime test exists unless actually created, executed, and linked or described with real limitation.

End replacement/package tasks with changed files, remove/exclude files, instruction count and limit fit, download links, executed tests, and deployment verdict.
