#!/usr/bin/env python3
"""Generate the full PR #1..#46 × rule matrix audit.

Destination/class: repo evidence only. Do not upload this script or its output to
ChatGPT Project Knowledge. It exists to make the audit reproducible without
bloated Project Instructions.
"""

import csv
from pathlib import Path

PRS = [f"PR{i:02d}" for i in range(1, 47)]

INSTRUCTION_ROWS = [
    ("I01", "Designer role/scope/language child EN"),
    ("I02", "Authority and conflict honesty"),
    ("I03", "Request Check"),
    ("I04", "Default audit-plus-patch"),
    ("I05", "Delegation boundaries and connector/Codex/API"),
    ("I06", "Architecture first and matrix"),
    ("I07", "Super-Pipeline trigger"),
    ("I08", "Combination Search"),
    ("I09", "Action Discovery"),
    ("I10", "Execution Substrate Selection / Failover"),
    ("I11", "User-Facing Russian Output"),
    ("I12", "Minimal User Action / User Work Firewall"),
    ("I13", "Target Placement and Result Lock"),
    ("I14", "Problem-Class Generalization"),
    ("I15", "External UI Handoff"),
    ("I16", "Approval-to-Execution Handoff"),
    ("I17", "Direct Destination + GitHub download trigger"),
    ("I18", "Copy-Ready Actions"),
    ("I19", "Artifact Destination Contract"),
    ("I20", "Repo-only Controls Exclusion"),
    ("I21", "Codex/GitHub Direct Handoff"),
    ("I22", "Runtime Activation Check"),
    ("I23", "Delegation Failure Reframe"),
    ("I24", "Evidence Claim and layer labels"),
    ("I25", "Verification Target"),
    ("I26", "Instruction Equivalence"),
    ("I27", "Answer Preservation"),
    ("I28", "Rational Route"),
    ("I29", "Durable Ledger"),
    ("I30", "State Reconciliation"),
    ("I31", "Completion Ledger"),
    ("I32", "Activation Semantics"),
    ("I33", "Plan/State Separation + Audit-only Before Patch"),
    ("I34", "Cost/Capability + Free-Route Fallback"),
    ("I35", "No Secrets"),
    ("I36", "Patch State Machine"),
    ("I37", "Patch Lock"),
    ("I38", "Builder/Auditor split"),
    ("I39", "Kernel self-preservation list"),
    ("I40", "Current package truth"),
    ("I41", "Right-sized architecture"),
    ("I42", "Registry/PB diff/deletion burden for inst/file changes"),
    ("I43", "File changes decision"),
    ("I44", "Behavior-only files"),
    ("I45", "Complete package + Artifact Destination Matrix"),
    ("I46", "Run testing_protocol before delivery"),
    ("I47", "Current/high-stakes source verification"),
    ("I48", "Safety refusal boundary"),
    ("I49", "Child-system inheritance"),
    ("I50", "Final gate list"),
]

PB_TITLES = {
    "00": "Patch Lock and invalid-delivery blocking",
    "00A": "Patch State Machine",
    "00B": "Builder/Auditor split",
    "01": "Authority",
    "02": "Request Check",
    "03": "Architecture-first",
    "04": "Combination Search",
    "05": "Action Discovery",
    "06": "Source/tool honesty",
    "07": "Visible-file honesty",
    "08": "Current package truth",
    "09": "Anti-regression preservation",
    "10": "Deletion/merge burden",
    "11": "Right-sized architecture",
    "12": "Behavior-only active files",
    "13": "File-structure decision",
    "14": "Complete current package delivery",
    "15": "Actual pre-delivery testing",
    "16": "Synchronized-rule maintenance",
    "17": "OpenAI/current/source verification",
    "18": "Safety/refusal boundaries",
    "19": "Child-system inheritance",
    "20": "Final gate and deployment verdict",
    "21": "Anti-loop",
    "22": "Regression smoke tests",
    "23": "User-work minimization",
    "24": "Repository-first delivery and blocked-write fallback",
    "25": "Execution Substrate Selection",
    "26": "Execution Failover",
    "27": "Delegation Failure Reframe",
    "28": "Evidence Claim Gate",
    "29": "Verification Target Lock",
    "30": "Instruction Equivalence Gate",
    "31": "Answer Task Preservation",
    "32": "Rational Route Gate",
    "33": "Durable Job Ledger",
    "34": "State Reconciliation Gate",
    "35": "Completion Ledger",
    "36": "Activation Semantics Check",
    "37": "Plan/State Separation",
    "38": "Cost/Capability Gate",
    "39": "Free-Route Fallback",
    "40": "Source Safety / No Secrets Gate",
    "41": "Audit-only Before Patch Gate",
    "42": "Operation Watchdog",
    "43": "Atomic Write Limit",
    "44": "Checkpoint Before Mutation",
    "45": "Failed Write Fallback",
    "46": "No Silent Long Task",
    "47": "GitHub Instruction/Knowledge Delivery Format",
    "48": "User-Facing Russian Output Gate",
    "49": "Minimal User Action / Action Compression Gate",
    "50": "Target Placement and Result Lock",
    "51": "Problem-Class Generalization Gate",
    "52": "End-to-End Handoff / Publish-Step Verification Gate",
    "53": "Approval-to-Execution Handoff / Tool-Executable Final Action Gate",
    "54": "Direct Destination / Deep-Link Verification Gate",
    "55": "Copy-Ready User Action Blocks",
    "56": "Artifact Destination Contract",
    "57": "Repo-only Controls Exclusion",
    "58": "GitHub/Codex Direct Handoff Contract",
    "59": "Runtime Activation / Old Branch Non-equivalence",
    "60": "Project Design Super-Pipeline",
    "61": "Hidden Requirements Mining",
    "62": "Counterexample-Guided Improvement",
    "63": "Mutation Testing",
    "64": "Learning Ledger",
    "65": "Blocked-Route and Short-Route Handoff Gate",
    "66": "Self-Preserving Thin Kernel / Rule Admission / GitHub-first Release",
    "67": "Verified Direct-Target Handoff",
}

PB_ROWS = [(f"PB-{k}", v) for k, v in PB_TITLES.items()]
META_ROWS = [
    ("M01", "Protected behavior status categories"),
    ("M02", "PASS/FAIL Invalid Delivery criteria"),
    ("M03", "Owner map"),
    ("M04", "Deletion rule"),
    ("M05", "Right-sized rule"),
    ("M06", "Line-value test"),
    ("M07", "Child propagation"),
    ("M08", "Manifest active_source_files"),
    ("M09", "Manifest protected_behavior_coverage"),
    ("M10", "Release gates"),
    ("M11", "External eval layers as repo-only evidence"),
    ("M12", "Non-active folders evidence-only"),
    ("M13", "ChatGPT Project upload rule"),
    ("M14", "GitHub connector rule"),
]

ROWS = [(rid, name, "Instructions kernel") for rid, name in INSTRUCTION_ROWS] + [
    (rid, name, "Protected behavior") for rid, name in PB_ROWS
] + [(rid, name, "Meta-rule") for rid, name in META_ROWS]

# Default is conservative: if the PR diff/body was not inspected for a row,
# the matrix must say not inspected, not not relevant.
STATUS = {(rid, pr): "not inspected" for rid, _, _ in ROWS for pr in PRS}
EVIDENCE = {rid: "default not inspected; explicit cells based on PR metadata/body/diff inspected in this conversation" for rid, _, _ in ROWS}
FINDING = {rid: "No specific finding beyond explicit matrix cells; uninspected cells are unclaimed." for rid, _, _ in ROWS}
ACTION = {rid: "No PR46 change required from current evidence." for rid, _, _ in ROWS}


def set_status(rule_ids, pr_numbers, value):
    for rid in rule_ids:
        for n in pr_numbers:
            STATUS[(rid, f"PR{n:02d}")] = value

# Known inspected/metadata-backed changes. This is intentionally sparse; absence
# of a status is not inspected, not presumed irrelevant.
set_status(["I05", "PB-23", "PB-24"], [1, 2, 4, 9, 10, 12], "strengthened")
set_status(["PB-06", "PB-07", "PB-08", "I02", "I24"], [6, 8, 14], "strengthened")
set_status(["PB-00", "PB-00A", "PB-00B", "I36", "I37", "I38"], [14, 15, 16, 18, 19], "strengthened")
set_status(["PB-38", "PB-39", "PB-40", "PB-41", "I33", "I34", "I35"], [20], "added")
set_status(["PB-38", "PB-39", "PB-40", "PB-41", "I34", "I35"], [21], "superseded")
set_status(["PB-30", "I26"], [22], "preserved")
set_status(["PB-47", "PB-56", "PB-57", "PB-58", "PB-59", "I19", "I20", "I21", "I22"], [31, 32], "strengthened")
set_status(["PB-60", "PB-61", "PB-62", "PB-63", "PB-64", "I07"], [33, 39], "superseded")
set_status(["PB-52", "I15"], [34], "strengthened")
set_status(["PB-65"], [35], "superseded")
set_status(["PB-65", "PB-54", "I17", "I10"], [36], "strengthened")
set_status(["PB-66", "M03", "I39"], [37], "strengthened")
set_status(["PB-67", "I13", "I21"], [40], "added")
set_status(["I12", "PB-49"], [42], "strengthened")
set_status(["PB-54", "I17"], [43, 44], "weakened")
set_status(["PB-22", "PB-54", "PB-65", "I17"], [45], "missing")
set_status(["PB-22", "PB-54", "PB-65", "I17"], [46], "strengthened")
set_status(["I19", "PB-56", "I22", "PB-59", "I35", "PB-40", "PB-63", "PB-30", "M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12", "M13", "M14"], [46], "preserved")
set_status(["PB-64"], [46], "strengthened")

for rid in ["I17", "PB-54"]:
    EVIDENCE[rid] = "PR43/44/45/46 diff/body inspected in conversation"
    FINDING[rid] = "Confirmed: PR43/PR44 narrowed generic Direct Destination while adding GitHub download wording; PR45 missed kernel/registry/test companions; PR46 repairs with thin-kernel trigger plus protocol/registry/testing."
    ACTION[rid] = "PR46 has active trigger + registry owner-map + T35 + testing_protocol test; before merge run length/package/linter checks."
for rid in ["PB-65"]:
    EVIDENCE[rid] = "PR45/46 diff/body inspected in conversation"
    FINDING[rid] = "Confirmed: PR45 left blocked/download-route companion gap for GitHub failed/red workflow and download-link handling; PR46 strengthens registry/testing."
    ACTION[rid] = "No more instruction expansion; keep detail in registry/testing/protocol."
for rid in ["PB-22"]:
    FINDING[rid] = "Confirmed: PR45 had no explicit smoke trap for Actions-list/red-run download substitution; PR46 adds T35."
    ACTION[rid] = "No more instruction expansion; keep smoke test in regression_smoke_tests.md."
for rid in ["I19", "PB-56"]:
    FINDING[rid] = "Suspected compression risk in earlier PR46 wording was repaired: ChatGPT Project Knowledge/GitHub source file labels restored."
    ACTION[rid] = "Preserve exact destination labels; report/audit files remain repo evidence only."
for rid in ["I22", "PB-59"]:
    FINDING[rid] = "Suspected compression risk repaired: old chat before update wording preserved."
for rid in ["I35", "PB-40"]:
    FINDING[rid] = "Suspected compression risk repaired with compact but precise repo access/branch rules/visibility/account security wording."
for rid in ["PB-63"]:
    FINDING[rid] = "Suspected wording blur repaired: false runtime activation claims preserved."
for rid in ["PB-64"]:
    FINDING[rid] = "Newly identified meta-failure: a partial critical audit was mislabeled as a full matrix. PR46 updates the ledger and this audit evidence so uninspected cells remain not inspected and limitations are explicit."
    ACTION[rid] = "Learning Ledger updated with partial-audit mislabeling failure class."


def write_matrix(path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Rule_ID", "Rule", "Rule_Class", "Evidence_Level", *PRS, "Deep_Audit_Finding", "PR46_Action_Status"])
        for rid, name, cls in ROWS:
            w.writerow([rid, name, cls, EVIDENCE[rid], *[STATUS[(rid, pr)] for pr in PRS], FINDING[rid], ACTION[rid]])


def write_summary(path: Path) -> None:
    counts = {pr: {} for pr in PRS}
    for pr in PRS:
        for rid, _, _ in ROWS:
            counts[pr][STATUS[(rid, pr)]] = counts[pr].get(STATUS[(rid, pr)], 0) + 1
    statuses = ["added", "strengthened", "preserved", "weakened", "missing", "superseded", "not relevant", "not inspected"]
    with path.open("w", encoding="utf-8") as f:
        f.write("# Full PR × Rule Matrix Audit Summary\n\n")
        f.write("Evidence layer: repo evidence only, Candidate PR #46. Do not upload to ChatGPT Project Knowledge.\n\n")
        f.write("## Matrix shape\n\n")
        f.write(f"- Rows: {len(ROWS)} = {len(INSTRUCTION_ROWS)} instruction rows + {len(PB_ROWS)} PB rows + {len(META_ROWS)} meta rows.\n")
        f.write("- Columns: PR01..PR46.\n")
        f.write("- Default for unverified cells: `not inspected`, not `not relevant`.\n\n")
        f.write("## Status counts\n\n")
        f.write("| PR | " + " | ".join(statuses) + " |\n")
        f.write("|---" + "|---:" * len(statuses) + "|\n")
        for pr in PRS:
            f.write("| " + pr + " | " + " | ".join(str(counts[pr].get(s, 0)) for s in statuses) + " |\n")
        f.write("\n## Finding buckets\n\n")
        f.write("### Confirmed weakenings\n- PR43/PR44 weakened generic Direct Destination while adding GitHub-download wording.\n\n")
        f.write("### Suspected weakenings / compression risks repaired in PR46\n- Artifact destination label compression repaired.\n- Runtime activation wording repaired.\n- No Secrets repository/security wording repaired.\n- PB-63 false runtime activation wording repaired.\n\n")
        f.write("### Missing companion updates\n- PR45 missed kernel trigger, PB-54/PB-65 owner-map, T35 smoke test, and testing_protocol download test.\n\n")
        f.write("### Rules moved to weaker layer\n- No unresolved confirmed case in current PR46 head. Earlier PR43/PR44 risk repaired by restoring kernel trigger and moving details to protocol/registry/testing rather than only Knowledge.\n\n")
        f.write("### Rules restored in later PR\n- PR46 restores/strengthens I17/PB-54/PB-65/PB-22 coverage.\n\n")
        f.write("### Still unresolved\n- Fresh instruction length check, package build, package_linter/package_guard, CI/status refresh, and runtime activation check are not executed in this pass.\n- Historical PRs with only metadata/body evidence remain partially uninspected.\n")


if __name__ == "__main__":
    out_dir = Path(__file__).resolve().parent
    write_matrix(out_dir / "pr_rule_matrix_full_2026-06-07.csv")
    write_summary(out_dir / "pr_rule_matrix_full_summary_2026-06-07.md")
    print("Wrote full PR × rule matrix and summary.")
