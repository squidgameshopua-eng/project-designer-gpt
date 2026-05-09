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
