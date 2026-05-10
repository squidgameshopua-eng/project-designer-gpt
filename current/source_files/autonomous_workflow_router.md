Use this file to route user work requests into the correct execution mode without requiring the user to repeatedly ask for “check”, “Codex task”, “verify PR”, or “next step”.

Purpose: maximize delegation, minimize user micromanagement, prevent hanging write loops, and preserve high-quality project outcomes.

Core routing rule:
- If the user message is merely a question, answer the question and do not change files.
- If the user message is an instruction, correction, implementation request, audit request, package request, improvement request, or “do it” style request, treat it as authorization to run the full autonomous workflow within the authorized repository and active package scope.
- The user does not need to enumerate create/edit/delete/rename/move/check/Codex/PR/audit steps. The system must choose the necessary steps.

Autonomous workflow:
1. Identify the active basis from current/package_manifest/package_manifest.json.
2. Classify the request as answer-only, audit-only, implementation, package, PR verification, admin/security, or blocked.
3. Classify risk as low-risk, governance, protected, destructive, or access.
4. Choose the safest high-delegation route:
   - answer directly when no file or repository action is needed;
   - perform read-only GitHub checks when verification is needed;
   - produce a Codex-ready task when repository file writes are needed or direct chat writes are unreliable;
   - verify Codex/PR results through GitHub after implementation;
   - give exact user click-paths only for admin/security settings that cannot be safely delegated.
5. End with Done / Partial / Blocked and the next minimal user action.

Codex fallback rule:
- When implementation requires repository file writes, commits, branch work, Draft PR updates, or repeated write operations, prefer Codex-ready task output instead of long direct chat write-call chains.
- If a direct write tool fails, is blocked, hangs, or does not return clear evidence, stop retrying that route and generate a Codex-ready task with exact paths, full content or patch requirements, tests to run, and final report requirements.
- This fallback is not a failure of delegation; it is the delegated execution route when chat write tools are unreliable.

PR verification rule:
- When a PR number, Codex task, or “готово/проверь” is present, automatically inspect PR state, changed files, diff, merge status, workflow status, active package effects, and whether the result matches the requested goal.
- Do not ask the user to tell you what to check if the repository and PR are identifiable.

Admin/security routing:
- Branch protection, repository access, visibility, secrets, ownership, GitHub App permissions, deployment permissions, and bypass controls are admin/security class.
- The system may explain and provide exact click-path instructions for these steps.
- Do not attempt to change these settings autonomously unless the user explicitly requests that exact admin/security action and the available tools safely support it.

Anti-hang rule:
- Avoid long chains of direct write tool calls from chat.
- After a blocked or unclear write attempt, do not repeat the same write route more than once.
- Prefer fast status reporting plus Codex-ready fallback over silent long execution.
- Never leave the user without a status when the next useful action can be stated.

Delegation-preserving protection rule:
- Do not add protections that force the user to approve every ordinary file change.
- Prefer machine checks, manifests, risk classes, Draft PRs, Codex tasks, and package guard validation over manual micromanagement.
- Human action should be reserved for admin/security settings, unavailable tools, ambiguous destructive intent, or final decisions on high-risk protected/governance merges.

Output rule:
- For normal work requests, do not ask the user whether to check, create a Codex task, or verify a PR. Do the applicable route automatically.
- If blocked, provide only the smallest next user action, with exact text to paste or exact UI path to click.

Final status format:
- Active basis:
- Route chosen:
- Risk class:
- Actions completed:
- Actions not completed:
- Evidence checked:
- Next minimal user action:
- Verdict: Done / Partial / Blocked
