Use this file only for output structures and reports. Main Project/GPT Instructions control behavior.

Default audit/patch answer:
Request Check:
- actuality:
- correctness:
- realism:
- usefulness/harm:
- gaps:

Architecture:
- purpose:
- user:
- inputs/outputs:
- scope:
- files/sources/tools:
- safety:
- tests:
- verdict:

Patch report:
- Active basis:
- Changed files:
- New files:
- Removed/excluded files:
- PB map:
- Deletion/merge burden:
- Companion-file check:
- Tests executed:
- NOT EXECUTED tests:
- Delivery verdict:

Protected behavior diff table:
| PB ID | Behavior | Prior location | New location | Status | Evidence | Risk | Child impact |

File structure decision:
| File | Decision | Reason | Alternatives rejected | Owner role | Active/evidence status |

Test scorecard:
| Gate/test | Target | Evidence checked | Status | Limitation |

Current package state:
- Instruction count:
- Limit:
- Active files:
- New files:
- Changed files:
- Remove/exclude from upload:
- Optional/evidence-only files:
- Source facts checked:
- Runtime/UI verification:
- Verdict:

Upload instructions:
- Project Instructions: paste complete Instructions.md content.
- Project/source files: upload only listed active .md files.
- Remove/exclude: list old/obsolete files.
- Do not upload: reports, tests, scripts, manifests, linter, archive, delivery ZIPs unless explicitly intended as non-active reference.

Runtime Activation Check template:
- ChatGPT runtime active basis:
- Project Instructions active/not verified:
- Project Knowledge/source files visible/not visible:
- GitHub Stable current/ verified/not verified:
- Candidate PR verified/not verified:
- Old chats evidence-only:
- Repo-only controls not active Knowledge:
- Tests available:
- Tests executed / NOT EXECUTED:
- Verdict: Active / Partial / Not Verified.

Artifact Destination Matrix:
| Artifact | Class | Exact destination | Forbidden destination | Active/evidence status | User action |

GitHub/Codex handoff:
- Exact repo:
- Branch/PR/task:
- File paths:
- Paste/click field:
- Expected result:
- Forbidden side effects:
- Direct/fallback link:
- Evidence to return:

Blocked route report:
- Route/action attempted:
- Target:
- Intended result:
- Blocker class:
- Evidence checked:
- Evidence layer:
- What was not changed:
- Retry policy:
- Shortest safe fallback:
- Completion boundary:

Learning Ledger entry:
- Date/source:
- Failure class:
- Detection source:
- Evidence layer:
- Violated PB/requirement:
- Local fix/blocker:
- Generalized prevention:
- Files/tests/templates/validators updated:
- Commands/tests run:
- Remaining risk:

## Secrets/settings audit template
Scope:
- Target repo/project/account setting:
- Evidence layer:
- Tool/UI availability:

Report:
- Secrets/credentials values: not requested, not displayed, not copied.
- Existence/status only: exists / absent / inaccessible / not verified.
- Security/admin/billing/branch-protection state: exact value not disclosed unless user explicitly supplied it and safe to repeat.
- Limitation:
- Safe next route:

## PB-48 User-facing Russian output template
User-facing language: Russian
Technical identifiers left in English when useful:
- filenames:
- branch/PR IDs:
- exact gate names:
- code/commands:
Verdict in Russian:

## PB-49 Minimal User Action / Action Compression template
Goal:
Safe system-executable route available: YES/NO
Routes compared:
- connector/API:
- Codex task:
- Draft PR:
- generated artifact/ZIP:
- manual UI:
Chosen route:
User actions required per route:
Final user action count:
Why not fewer:

## PB-50 Target Placement and Result Lock template
Exact place:
Target object:
Expected result:
Forbidden side effects:
Parallel artifact risk:
If target inaccessible:
- blocker:
- evidence:
- allowed fallback:

## PB-51 Problem-Class Generalization template
Detected problem/failure pattern:
Detection source:
Evidence layer:
Failure class:
Why local-only fix is insufficient/sufficient:
Generalized prevention mechanism:
Local fix, if still relevant:
Files/tests/templates/validators affected:

## PB-52 End-to-End Handoff template
Entry point/link:
Screen/panel/menu/tab:
Exact paste/click location:
Text/action to paste/click:
Submit/start action:
Wait for:
Post-run publish/apply action to look for:
Expected observable result:
Forbidden side effects:
Evidence the user should return:
Completion may be claimed only after:

## PB-53 Approval-to-Execution Handoff template
Action requiring approval:
Risk/irreversibility:
User approval status:
Safe tool route available:
Tool execution result:
Verification evidence:
Manual fallback reason, if any:

## PB-54 Direct Destination template
Target action/page/file/task:
Deepest link:
Link label: direct / fallback / not verified
Evidence for link target:
Fallback navigation if direct link not verified:
Forbidden generic destination:

## PB-55 Copy-Ready User Action Blocks template
Use each actionable text in a separate fenced block.

Label:
```text
copy-ready block
```

Multiple options:
Option A:
```text
...
```
Option B:
```text
...
```

PB-56 Artifact Destination Matrix template:
| Artifact | Destination class | Exact destination/path | Forbidden destination | Active/evidence status | Upload/apply rule |
|---|---|---|---|---|---|

PB-57 GitHub file-path mapping template:
| Repo path | ChatGPT Project upload path | Upload? | Reason | Forbidden use |
|---|---|---:|---|---|
| current/instructions/Instructions.md | Project Instructions field | YES paste | active instruction | do not upload as Knowledge |
| current/source_files/*.md | Knowledge/*.md | YES upload | active source files | do not rename to draft/final/old |
| current/package_manifest/package_manifest.json | repo control/evidence | NO active upload | manifest only | not Project Knowledge |
| package_linter.py / scripts / workflows / tests / reports / archive / deliveries / ZIPs | repo control/evidence/archive | NO active upload | tooling/evidence | not Project Knowledge |

PB-58 Codex direct handoff/copy-ready task template:
Exact repo:
Exact branch/PR:
Exact files:
Paste into:
Expected result:
Forbidden side effects:
Direct/fallback link:

```text
Codex task:
...
```

PB-59 Runtime activation handshake template:
```text
Runtime Activation Check:
1. Confirm current Project Instructions basis.
2. List visible Project Knowledge/source files.
3. State whether GitHub Stable current/ was verified.
4. State whether Candidate PR/local package/old chat is only evidence.
5. Confirm repo-only controls are not active Knowledge.
6. List tests available and tests NOT EXECUTED.
7. Verdict: Active / Partial / Not Verified.
```

PB-65 Blocked-route report template:
- Route/action:
- Target:
- Intended result:
- Blocker class:
- Evidence checked:
- Evidence layer:
- What was not changed:
- Retry policy:
- Shortest safe fallback:
- Completion boundary:
- Link type classification:
- Artifact current/source layer:
- Evidence to return:
- Forbidden side effects:

PB-65 GitHub artifact/download handoff template:
- Requested artifact:
- Source layer: PR head / merge commit / main / release tag / local package / unknown
- Link type: browser-usable UI / browser-download GitHub / Release asset / Actions artifact browser / API-auth-only / temporary signed / raw / fallback navigation / GPT-hosted
- Direct link:
- Fallback link:
- Exact artifact name:
- Exact button/icon:
- Expected result:
- Evidence to return:
- Do not:

PB-65 Single Task route template:
- Multi-file goal:
- Single Codex/API/PR/package route available: YES/NO and why:
- Exact repo/branch:
- Paths to change:
- Copy-ready single task / direct route:
- Tests to run:
- Expected result:
- Forbidden side effects:
- Evidence to return:
- User actions avoided:
- Remaining user-only action, if any:

Rule Admission Report Template:
Proposed rule:
Existing coverage:
Classification:
Owner file:
Companion files:
Affected PB-ID:
Instruction impact:
Test impact:
Linter/manifest impact:
Release-state impact:
Decision: Accept to Kernel / Accept to Protocol / Accept to Test / Accept to Linter-Manifest / Accept to Template / Reject duplicate / Reject unsafe or unclear
Verdict:
