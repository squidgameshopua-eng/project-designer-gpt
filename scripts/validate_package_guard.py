#!/usr/bin/env python3
"""Behavioral guard for the PB-anchor Thin Kernel architecture.

This guard validates behavior anchors rather than obsolete long exact wording in
Project Instructions. It fails when the compact kernel loses authority, PB range,
manifest/test anchors, active-file scope, or Knowledge upload boundaries.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "current"
SOURCE = CURRENT / "source_files"
INSTRUCTIONS = CURRENT / "instructions/Instructions.md"
MANIFEST = CURRENT / "package_manifest/package_manifest.json"

REQUIRED_SOURCE_FILES = {
    "architecture_domain_rules.md",
    "autonomous_workflow_router.md",
    "counterexample_improvement_protocol.md",
    "delegation_access_policy.md",
    "delivery_protocol.md",
    "github_download_link_protocol.md",
    "gpt_action_discovery_protocol.md",
    "instruction_governance.md",
    "mutation_testing_protocol.md",
    "no_premature_user_handoff_protocol.md",
    "openai_gpt_project_sources.md",
    "output_templates.md",
    "package_state_protocol.md",
    "patch_lock_protocol.md",
    "project_design_super_pipeline_protocol.md",
    "project_learning_ledger.md",
    "project_operating_protocol.md",
    "protected_behavior_registry.md",
    "regression_smoke_tests.md",
    "rule_admission_protocol.md",
    "source_safety_policy.md",
    "testing_protocol.md",
}

PB_COVERAGE_REQUIRED = ["PB-00", "PB-00A", "PB-00B"] + [f"PB-{n:02d}" for n in range(47, 69)]
REGISTRY_REQUIRED = ["PB-00", "PB-00A", "PB-00B"] + [f"PB-{n:02d}" for n in range(1, 68)]

INSTRUCTION_ANCHORS = [
    "Authority",
    "Project/GPT > lower-authority protocol files",
    "not hidden instructions",
    "Request Check",
    "audit-plus-patch",
    "PB-00..68",
    "protected_behavior_registry.md",
    "package_manifest.json",
    "testing_protocol.md",
    "regression_smoke_tests.md",
    "Artifact Destination",
    "Repo-only",
    "runtime",
    "evidence",
    "Patch Lock",
    "Final gate",
    "NOT EXECUTED",
    "verdict",
]

OBSOLETE_BLOAT = [
    "Final gate: Request Check,architecture,Super-Pipeline,Hidden Requirements Mining,CEGIS,Mutation Testing,Learning Ledger,External UI Handoff",
    "website/app/interface/tool exact link/screen/panel/field/button,paste/start/submit/wait/post-run/result/evidence",
    "manifest/linter/scripts/.github/workflows/tests/reports/UPLOAD_GUIDE/CODEX/archive/deliveries/ZIPs=repo evidence",
]

FORBIDDEN_UPLOAD_MARKERS = [
    "package_manifest.json",
    "package_linter.py",
    "scripts/",
    ".github/workflows/",
    "tests/",
    "reports/",
    "evals/",
    "UPLOAD_GUIDE.md",
    "CODEX_TASK",
    "archive/",
    "deliveries/",
    "external_sources/",
]

TEST_ANCHORS = [
    "Evidence-grade test",
    "Patch Lock test",
    "Protected-registry regression test",
    "Deletion-burden test",
    "Right-sized architecture test",
    "Instruction-limit test",
    "Artifact Destination Matrix test",
    "Repo-only Controls Exclusion test",
    "Runtime Activation / old-branch non-equivalence test",
    "Super-Pipeline trigger test",
    "Mutation Testing test",
    "Rule Admission test",
]


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    for path in [INSTRUCTIONS, MANIFEST, SOURCE, ROOT / "package_linter.py", ROOT / "scripts/build_knowledge_package.py"]:
        if not path.exists():
            return fail(f"missing path: {path.relative_to(ROOT)}")

    data = json.loads(read(MANIFEST))
    if data.get("active_source_of_truth") != "current/":
        return fail("manifest active_source_of_truth must be current/")
    if data.get("instruction_file") != "current/instructions/Instructions.md":
        return fail("manifest instruction_file must point to current Instructions.md")
    if str(data.get("project_sources_folder", "")).rstrip("/") != "current/source_files":
        return fail("manifest project_sources_folder must be current/source_files/")

    active = data.get("active_source_files")
    if not isinstance(active, list) or active != sorted(active):
        return fail("active_source_files must be a sorted list")
    missing = sorted(REQUIRED_SOURCE_FILES - set(active))
    if missing:
        return fail(f"manifest missing active source files: {missing}")
    for filename in active:
        if "/" in filename or "\\" in filename or not (SOURCE / filename).exists():
            return fail(f"invalid or missing active source file: {filename}")

    roles = data.get("file_roles", {})
    if not isinstance(roles, dict):
        return fail("file_roles must be an object")
    for filename in active:
        if not isinstance(roles.get(filename), str) or len(roles[filename].strip()) < 12:
            return fail(f"missing meaningful file role for {filename}")

    coverage = data.get("protected_behavior_coverage", {})
    if not isinstance(coverage, dict):
        return fail("protected_behavior_coverage must be an object")
    for pb_id in PB_COVERAGE_REQUIRED:
        if not coverage.get(pb_id):
            return fail(f"manifest missing PB coverage: {pb_id}")
    if "no_premature_user_handoff_protocol.md" not in coverage.get("PB-68", []):
        return fail("PB-68 coverage must include no_premature_user_handoff_protocol.md")
    if "instruction_governance.md" not in coverage.get("PB-66", []):
        return fail("PB-66 coverage must include instruction_governance.md")

    tests = set(data.get("required_test_suites", []))
    for suite in ["package_linter.py", "scripts/validate_package_guard.py", "scripts/validate_rule_admission_guard.py", "current/source_files/regression_smoke_tests.md"]:
        if suite not in tests or not (ROOT / suite).exists():
            return fail(f"missing required test suite: {suite}")

    release_gates = set(data.get("release_gates", []))
    for gate in ["package_linter_pass", "package_guard_pass", "rule_admission_guard_pass", "auditor_pass_before_stable", "runtime_activation_not_claimed_without_evidence"]:
        if gate not in release_gates:
            return fail(f"manifest missing release gate: {gate}")

    upload_rule = data.get("chatgpt_project_upload_rule", {}).get("project_sources", "")
    for marker in FORBIDDEN_UPLOAD_MARKERS:
        if marker not in upload_rule:
            return fail(f"upload rule must forbid repo-only marker: {marker}")

    instruction = read(INSTRUCTIONS)
    if len(instruction) > 8000:
        return fail("Instructions exceed 8000 characters")
    if len(instruction) < 1200:
        return fail("Instructions too short to hold non-delegable kernel contracts")
    for phrase in INSTRUCTION_ANCHORS:
        if phrase not in instruction:
            return fail(f"instruction missing PB-anchor phrase: {phrase}")
    for phrase in OBSOLETE_BLOAT:
        if phrase in instruction:
            return fail(f"obsolete long-form instruction wording survived: {phrase[:80]}...")

    registry = read(SOURCE / "protected_behavior_registry.md")
    for pb_id in REGISTRY_REQUIRED:
        if pb_id not in registry:
            return fail(f"registry missing {pb_id}")
    if "PB-68" not in read(SOURCE / "no_premature_user_handoff_protocol.md"):
        return fail("PB-68 must be owned by no_premature_user_handoff_protocol.md")
    for phrase in ["Deletion rule", "Right-sized rule", "Line-value test", "Owner map", "Self-Preserving Thin Kernel"]:
        if phrase not in registry:
            return fail(f"registry missing guard phrase: {phrase}")

    testing = read(SOURCE / "testing_protocol.md")
    for phrase in TEST_ANCHORS:
        if phrase not in testing:
            return fail(f"testing_protocol.md missing test anchor: {phrase}")

    build_script = read(ROOT / "scripts/build_knowledge_package.py")
    for phrase in ["Instructions.md", "Knowledge/", "active_source_files", "external_sources/", 'name == "Instructions.md" or name.startswith("Knowledge/")']:
        if phrase not in build_script:
            return fail(f"build_knowledge_package.py missing guard phrase: {phrase}")

    print("PASS: PB-anchor package guard validation succeeded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
