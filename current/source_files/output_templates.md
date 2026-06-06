Use this file only for output structures and reports. Main Project/GPT Instructions control behavior.

Request Check template:
| Запрос | Проверка |
|---|---|
| <split request> | Актуальность / корректность / реалистичность / польза-вред / фактические пробелы |

Patch Lock / State Machine report template:
| Gate | Evidence checked | Status | Limitation |
|---|---|---|---|
| Active package basis | <instruction/files/source> | PASS/PARTIAL/FAIL/NOT EXECUTED | <limit> |
| patch_lock_protocol.md checked | <yes/no> | <status> | <limit> |
| protected_behavior_registry.md checked | <yes/no> | <status> | <limit> |
| Behavior IDs mapped | <PB list> | <status> | <limit> |
| Deletion/merge burden | <items> | <status> | <limit> |
| Companion files checked | <files> | <status> | <limit> |
| Actual tests executed | <tests> | <status> | <limit> |
| Verdict | <Ready/Not Ready/Invalid Delivery> | <status> | <limit> |

Behavior diff template:
| PB ID | Behavior class | Prior location | New location | Status | Evidence | Weakening risk | Child impact |
|---|---|---|---|---|---|---|---|

Deletion/merge burden template:
| Removed/merged item | Controlled behavior | Reason | Preservation/replacement | Residual risk | Verdict |
|---|---|---|---|---|---|

File-structure decision template:
| File/action | Decision | Operational role | Why not merge/delete/no-file | Tests/owner |
|---|---|---|---|---|

Package state template:
Instruction count: <n>/<limit>
Active files: <list>
New files: <list>
Changed files: <list>
Unchanged companion files: <list>
Remove/exclude from upload: <list>
Official/source facts checked: <date + sources>
Screenshot/UI evidence: <if used>
Missing material: <list/none>
Verdict: <Ready/Ready With Minor Risks/Not Ready/Split Required/More Source Material Required/Unsafe/Invalid Delivery>

Executed tests template:
| Test | Target | Evidence checked | Status | Limitation |
|---|---|---|---|---|

Final delivery checklist template:
Changed files: <list>
Remove/exclude files: <list>
Instruction count and limit fit: <n>/<limit>
Downloads: <links>
Executed tests: <compact table>
Deployment verdict: <verdict>

Operation Checkpoint template:
| Operation | State | Route | Expected evidence | Evidence returned | Next action/blocker |
|---|---|---|---|---|---|

Cost/capability route template:
Route considered: <tool/UI/agent>
Availability checked: <plan/permission/device/UI/tool>
Paid/unavailable risk: <none/paid trial/paid agent/unavailable/desktop-only/inaccessible>
Free route chosen first: <connector/API/local artifact/ZIP/PR-ready patch/manual web upload>
Verdict: <Allowed/Use fallback/Blocked>

Secrets/settings audit template:
| Item | Status | Evidence layer | Limitation |
|---|---|---|---|
| <setting/secret category> | <exists/absent/inaccessible/not verified> | <tool/file/UI/user evidence> | <no value disclosed> |


PB-47 GitHub Instruction/Knowledge delivery template:
Instruction file: current/instructions/Instructions.md -> Instructions.md
Instruction count: <n>/8000
Knowledge files: <manifest-listed current/source_files files>
Excluded from Knowledge: archive/, deliveries/, external_sources/, tests/, scripts/, .github/, non-active files
Artifact: <knowledge_source_files.zip path/link>
Build evidence: <scripts/build_knowledge_package.py result>
Upload guidance: paste Instructions.md into Project Instructions; upload only Knowledge/*.md as Project Sources/Knowledge; keep UPLOAD_GUIDE.md/package_manifest.json repo-only unless explicitly non-active audit/reference.
Verdict: <Ready/Not Ready>

PB-48 User-facing Russian output template:
- User-facing language: Russian
- English allowed only for: technical identifiers, filenames, code, exact gate names, branch/PR names, quoted source text, command output
- Conclusions: Russian
- Next steps: Russian
- Status reports: Russian
- Verdicts: Russian
- If technical output is in English, add Russian explanation

PB-49 Minimal User Action / Action Compression template:
- Goal:
- Available routes:
- User actions required per route:
- Evidence quality per route:
- Risk / reversibility:
- Selected route:
- Why this route has the fewest user actions without lowering quality:
- Rejected higher-user-work routes:
- User-only action, if unavoidable:

PB-50 Target Placement and Result Lock template:
- Exact place to paste/click:
- Target object:
- Target branch/PR/task/file:
- Expected result:
- Forbidden side effects:
- If target inaccessible:
- New artifact allowed: YES/NO and why:

PB-51 Problem-Class Generalization template:
- Detected problem:
- Detection source / evidence layer:
- Problem class:
- Local fix needed: YES/NO and why:
- Immediate correction, if relevant:
- Generalized prevention mechanism:
- Files/gates/tests/templates/validator to update:
- Future regression test:
- What not to repeat:

PB-52 End-to-End Handoff template:
- Entry point / link:
- Exact place to paste/click:
- Target object:
- Start/submit action:
- Post-run publish/apply action to look for, including what to click/wait for and create/update/save/upload/deploy if applicable:
- Expected result:
- Evidence to return:
- Forbidden side effects:
- Completion may be claimed only after:

PB-53 Approval-to-Execution Handoff template:
- Action requiring approval:
- Approval evidence:
- Safe tool route available: YES/NO and why:
- Execution route selected:
- Tool evidence verified:
- Result reported:
- Manual UI fallback used: YES/NO and reason:

PB-54 Direct Destination template:
- Intended target/action:
- Link provided:
- Link label: direct / fallback / not verified
- Verification or inference evidence:
- If fallback, minimal navigation from landing point:
- Why this is not merely a product homepage or generic parent page:

PB-55 Copy-Ready User Action Blocks template:
- Action label:
- Copy-ready block:
- Where to paste/send:
- When to use:
- If multiple options, provide each option in a separate copy-ready block:

## PB-56 Artifact Destination Matrix template
| Artifact | Class | Exact destination path/location | Forbidden destinations | Active/evidence status |
|---|---|---|---|---|
| `Instructions.md` | Project Instructions | Paste into ChatGPT Project Instructions | Project Knowledge, GitHub-only control folders | Runtime active only after UI save + activation check |
| `Knowledge/<file>.md` | ChatGPT Project Knowledge | Upload to Project Sources/Knowledge | GitHub control-only folders unless source file remains in repo | Runtime active only after UI upload + activation check |
| `current/package_manifest/package_manifest.json` | GitHub repo control | GitHub repo path `current/package_manifest/package_manifest.json` | Active ChatGPT Project Knowledge | Repo evidence/control |

## PB-57 GitHub file-path mapping template
Target repo: `<owner>/<repo>`
Target branch/PR: `<branch or PR>`
| Source artifact | GitHub destination path | Operation | Forbidden side effects |
|---|---|---|---|
| `<local path>` | `<repo path>` | add/update/delete | Do not change secrets, visibility, branch protection, or unrelated files |

## PB-58 Codex direct handoff/copy-ready task template
Direct/fallback link label: `<direct|fallback|not verified>` — `<URL or entry name>`
Exact paste/click field: `<Codex task prompt box / PR comment / file editor>`
Expected result: `<branch/commit/PR/files/tests>`
Forbidden side effects: no merge without validation; no secrets/access/visibility/branch-protection changes; no repo-only controls in active Knowledge.

```text
Codex task for <owner>/<repo> on <branch/PR>:
<copy-ready exact task, file paths, validation commands, expected result, forbidden side effects>
```

## PB-59 Runtime activation handshake template
Layer basis checked: GitHub main/current `<commit/branch>`, Candidate PR `<id>`, local package `<path>`, Project UI uploaded files `<evidence>`, runtime chat `<new chat URL/time>`, user screenshot statements `<scope>`.
Activation question for new Project chat:
```text
State the active Project Instructions version and list the visible Project Knowledge/source files you can use. Do not rely on old chats. Then answer: where should package_manifest.json be uploaded?
```
Expected: repo-only/control; not active Knowledge.
