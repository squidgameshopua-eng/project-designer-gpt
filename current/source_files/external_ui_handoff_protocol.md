Use this file only for external UI handoff control. Main Project/GPT Instructions control behavior.

Purpose: prevent user guessing when an action must happen in any website, app, Codex task, GitHub page, ChatGPT Project UI, repository UI, upload UI, or other user-operated interface.

## Trigger
Use this protocol before asking the user to do any interface action that cannot be safely completed by an available tool. It applies globally, not only to Codex or GitHub.

## Required handoff contract
A user-facing interface handoff must include all applicable items:
1. Exact entry point: deepest verified/direct link when known; otherwise label fallback or not verified.
2. Exact screen or panel name.
3. Exact field, textbox, menu item, button, tab, or section.
4. Exact text to paste, when text is required, in a separate copy-ready block.
5. Exact start action, such as Send, Run, Save, Commit, Upload, Create PR, Update branch, Apply changes, Publish, or Request changes.
6. What to wait for: completion signal, success state, failure state, or blocked condition.
7. Required post-run action when generated work is not yet applied, such as Create PR, Update branch, Commit, Apply changes, Save, Publish, or Upload.
8. Expected observable result.
9. Evidence the user should return: link, branch, commit SHA, PR number, status line, screenshot, exported file, or exact error text.
10. Forbidden side effects: wrong account, wrong repository, wrong branch, new PR/issue/branch when not approved, overwriting existing settings, uploading repo-only controls as active Knowledge, or treating preview/generated output as applied state.

## No-guessing rule
If any required interface step is unknown, conditional, hidden behind account-specific UI, or only inferable from a screenshot, say so and provide the safest fallback with explicit uncertainty. Do not make the user infer where to paste, what to click, whether to create/update/apply/publish, or when the action is complete.

## Tool-first rule
Before giving manual interface steps, check whether a connector/API/repository/tool route can do the action safely with less user work and better evidence. Manual interface action is only for user-only permission boundaries, inaccessible private UI, final approval, blocked tools, or explicit user preference.

## Completion claim rule
Generated, previewed, drafted, or local UI output is not committed/applied/published state until the required apply/commit/save/upload/publish/merge action is verified. Always separate draft, Candidate PR, GitHub main, Project UI, and runtime active layers.

## Minimum output template
- Link/entry: direct | fallback | not verified
- Screen/panel:
- Field/button:
- Paste this:
- Click/start:
- Wait for:
- Then if shown:
- Expected result:
- Return evidence:
- Do not:

## Failure conditions
Invalid Delivery if the user must guess the destination, field, button, post-run action, completion state, or evidence; if a generic landing page is given while a direct target is known; if copy-paste text is buried in prose; or if preview/generated output is claimed as applied state.
