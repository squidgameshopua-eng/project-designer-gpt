#!/usr/bin/env python3
"""Validate package guard for the Thin Kernel / PB-anchor architecture.

This guard intentionally avoids requiring long exact wording in
current/instructions/Instructions.md. The instruction kernel is allowed to be
small when protected behavior is anchored by PB IDs, manifest owner mapping,
owner protocol files, and executable tests.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT_DIR = ROOT / "current"
SOURCE_DIR = CURRENT_DIR / "source_files"
INSTRUCTION_PATH = CURRENT_DIR / "instructions/Instructions.md"
MANIFEST_PATH = CURRENT_DIR / "package_manifest/package_manifest.json"

INSTRUCTION_LIMIT = 8000
PREFERRED_MAX = 4200
MIN_REASONABLE_KERNEL = 1200

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

REQUIRED_MANIFEST_KEYS = {
    "active_source_of_truth",
    "instruction_file",
    "project_sources_folder",
    "manifest_file",
    "active_source_files",
    "file_roles",
    "protected_behavior_coverage",
    "required_test_suites",
    "release_gates",
    "non_active_folders",
    "chatgpt_project_upload_rule",
}

REQUIRED_RELEASE_GATES = {
    "manifest_schema_pass",
    "package_linter_pass",
    "package_guard_pass",
    "rule_admission_guard_pass",
    "regression_selection_reported",
    "auditor_pass_before_stable",
    "runtime_activation_not_claimed_without_evidence",
}

REQUIRED_TEST_SUITES = {
    "package_linter.py",
    "scripts/validate_package_guard.py",
    "scripts/validate_rule_admission_guard.py",
    "current/source_files/regression_smoke_tests.md",
}

REQUIRED_PB_IDS = ["PB-00", "PB-00A", "PB-00B"] + [f"PB-{n:02d}" for n in range(1, 68)]
KERNEL_CRITICAL_PB_IDS = ["PB-00", "PB-00A", "PB-00B"] + [f"PB-{n:02d}" for n in range(47, 69)]

KERNEL_ANCHORS = [
    "Authority",
    "lower-authority protocol files",
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

FORBIDDEN_INSTRUCTION_PATTERNS = [
    "Final gate: Request Check,architecture,Super-Pipeline,Hidden Requirements Mining,CEGIS,Mutation Testing,Learning Ledger,External UI Handoff",
    "Kernel self-preservation: preserve User-Facing Russian Output,Minimal User Action,TargetPlacement",
    "website/app/interface/tool exact link/screen/panel/field/button,paste/start/submit/wait/post-run/result/evidence",
    "manifest/linter/scripts/.github/workflows/tests/reports/UPLOAD_GUIDE/CODEX/archive/deliveries/ZIPs=repo evidence",
]

OWNER_FILES_BY_PB = {
    "PB-47": ["delivery_protocol.md", "testing_protocol.md", "scripts/build_knowledge_package.py"],
    "PB-48": ["testing_protocol.md", "output_templates.md"],
    "PB-49": ["delegation_access_policy.md", "autonomous_workflow_router.md", "testing_protocol.md"],
    "PB-50": ["delivery_protocol.md", "testing_protocol.md"],
    "PB-51": ["project_learning_ledger.md", "testing_protocol.md"],
    "PB-52": ["delivery_protocol.md", "testing_protocol.md"],
    "PB-53": ["delivery_protocol.md", "testing_protocol.md"],
    "PB-54": ["github_download_link_protocol.md", "delivery_protocol.md", "testing_protocol.md"],
    "PB-55": ["output_templates.md", "testing_protocol.md"],
    "PB-56": ["protected_behavior_registry.md", "testing_protocol.md", "package_linter.py"],
    "PB-57": ["protected_behavior_registry.md", "testing_protocol.md", "package_linter.py"],
    "PB-58": ["protected_behavior_registry.md", "testing_protocol.md", "package_linter.py"],
    "PB-59": ["protected_behavior_registry.md", "testing_protocol.md", "package_linter.py"],
    "PB-60": ["project_design_super_pipeline_protocol.md", "testing_protocol.md"],
    "PB-61": ["project_design_super_pipeline_protocol.md", "testing_protocol.md"],
    "PB-62": ["counterexample_improvement_protocol.md", "testing_protocol.md"],
    "PB-63": ["mutation_testing_protocol.md", "testing_protocol.md"],
    "PB-64": ["project_learning_ledger.md", "testing_protocol.md"],
    "PB-65": ["autonomous_workflow_router.md", "github_download_link_protocol.md", "testing_protocol.md"],
    "PB-66": ["instruction_governance.md", "rule_admission_protocol.md", "patch_lock_protocol.md", "testing_protocol.md"],
    "PB-67": ["autonomous_workflow_router.md", "protected_behavior_registry.md", "testing_protocol.md", "regression_smoke_tests.md"],
    "PB-68": ["no_premature_user_handoff_protocol.md", "autonomous_workflow_router.md", "protected_behavior_registry.md", "testing_protocol.md", "regression_smoke_tests.md"],
}

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


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def warn(message: str) -> None:
    print(f"WARN: {message}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require_path(path: Path) -> int | None:
    if not path.exists():
        return fail(f"missing path: {path.relative_to(ROOT)}")
    return None


def main() -> int:
    for path in [INSTRUCTION_PATH, MANIFEST_PATH, SOURCE_DIR, ROOT / "package_linter.py", ROOT / "scripts/build_knowledge_package.py"]:
        result = require_path(path)
        if result:
            return result

    try:
        manifest = json.loads(read(MANIFEST_PATH))
    except Exception as exc:
        return fail(f"manifest is not valid JSON: {exc}")

    missing_keys = sorted(REQUIRED_MANIFEST_KEYS - set(manifest))
    if missing_keys:
        return fail(f"manifest missing required keys: {missing_keys}")
    if manifest.get("active_source_of_truth") != "current/":
        return fail("active_source_of_truth must be current/")
    if manifest.get("instruction_file") != "current/instructions/Instructions.md":
        return fail("instruction_file must point to current/instructions/Instructions.md")
    if str(manifest.get("project_sources_folder", "")).rstrip("/") != "current/source_files":
        return fail("project_sources_folder must be current/source_files/")

    active_files = manifest.get("active_source_files")
    if not isinstance(active_files, list) or not all(isinstance(x, str) for x in active_files):
        return fail("active_source_files must be a list of filenames")
    if active_files != sorted(active_files):
        return fail("active_source_files must be sorted")
    missing_active = sorted(REQUIRED_SOURCE_FILES - set(active_files))
    if missing_active:
        return fail(f"manifest missing active source files: {missing_active}")
    for filename in active_files:
        if "/" in filename or "\\" in filename or filename.startswith("."):
            return fail(f"active_source_files must contain safe filenames only: {filename}")
        if not (SOURCE_DIR / filename).exists():
            return fail(f"manifest-listed source file missing: {filename}")

    file_roles = manifest.get("file_roles")
    if not isinstance(file_roles, dict):
        return fail("file_roles must be an object")
    for filename in active_files:
        role = file_roles.get(filename)
        if not isinstance(role, str) or len(role.strip()) < 12:
            return fail(f"file_roles missing meaningful role for {filename}")

    coverage = manifest.get("protected_behavior_coverage")
    if not isinstance(coverage, dict):
        return fail("protected_behavior_coverage must be an object")
    for pb_id in KERNEL_CRITICAL_PB_IDS:
        owners = coverage.get(pb_id)
        if not isinstance(owners, list) or not owners:
            return fail(f"manifest missing protected_behavior_coverage for {pb_id}")
    for pb_id, owner_files in OWNER_FILES_BY_PB.items():
        owners = set(coverage.get(pb_id, []))
        missing_owners = [owner for owner in owner_files if owner not in owners]
        if missing_owners:
            return fail(f"manifest coverage for {pb_id} missing owners: {missing_owners}")

    tests = set(manifest.get("required_test_suites", []))
    missing_tests = sorted(REQUIRED_TEST_SUITES - tests)
    if missing_tests:
        return fail(f"manifest missing required test suites: {missing_tests}")
    for suite in tests:
        if not (ROOT / suite).exists():
            return fail(f"required test suite path missing: {suite}")

    gates = set(manifest.get("release_gates", []))
    missing_gates = sorted(REQUIRED_RELEASE_GATES - gates)
    if missing_gates:
        return fail(f"manifest missing release gates: {missing_gates}")

    upload_rule = manifest.get("chatgpt_project_upload_rule", {}).get("project_sources", "")
    for marker in FORBIDDEN_UPLOAD_MARKERS:
        if marker not in upload_rule:
            return fail(f"upload rule must forbid repo-only marker as active Knowledge: {marker}")

    instruction = read(INSTRUCTION_PATH)
    instruction_len = len(instruction)
    if instruction_len > INSTRUCTION_LIMIT:
        return fail(f"Instructions exceed {INSTRUCTION_LIMIT} chars: {instruction_len}")
    if instruction_len > PREFERRED_MAX:
        warn(f"Instructions have {instruction_len} chars; preferred PB-anchor kernel max is {PREFERRED_MAX}.")
    if instruction_len < MIN_REASONABLE_KERNEL:
        return fail(f"Instructions too short to carry non-delegable invariants: {instruction_len}")
    for phrase in KERNEL_ANCHORS:
        if phrase not in instruction:
            return fail(f"PB-anchor kernel missing anchor: {phrase}")
    for pattern in FORBIDDEN_INSTRUCTION_PATTERNS:
        if pattern in instruction:
            return fail(f"Instructions contain obsolete long-form guard wording: {pattern[:80]}...")
    if "PB-00..68" not in instruction:
        return fail("Final gate must anchor the complete PB-00..68 registry range")
    if "Project/GPT > lower-authority protocol files" not in instruction:
        return fail("Authority line must keep lower-authority file boundary")

    registry = read(SOURCE_DIR / "protected_behavior_registry.md")
    for pb_id in REQUIRED_PB_IDS:
        if pb_id not in registry:
            return fail(f"protected_behavior_registry.md missing {pb_id}")
    pb68_protocol = read(SOURCE_DIR / "no_premature_user_handoff_protocol.md")
    if "PB-68" not in pb68_protocol or "No premature user handoff" not in pb68_protocol:
        return fail("no_premature_user_handoff_protocol.md must own PB-68")
    for phrase in [
        "Deletion rule",
        "Right-sized rule",
        "Line-value test",
        "Owner map",
        "Self-Preserving Thin Kernel",
    ]:
        if phrase not in registry:
            return fail(f"registry missing guard phrase: {phrase}")

    testing = read(SOURCE_DIR / "testing_protocol.md")
    for phrase in [
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
    ]:
        if phrase not in testing:
            return fail(f"testing_protocol.md missing test phrase: {phrase}")

    build_script = read(ROOT / "scripts/build_knowledge_package.py")
    for phrase in ["Instructions.md", "Knowledge/", "active_source_files", "name == \"Instructions.md\" or name.startswith(\"Knowledge/\")"]:
        if phrase not in build_script:
            return fail(f"build_knowledge_package.py missing package-scope guard phrase: {phrase}")
    for marker in FORBIDDEN_UPLOAD_MARKERS:
        if marker not in build_script:
            return fail(f"build_knowledge_package.py missing forbidden upload marker: {marker}")

    print("PASS: PB-anchor package guard validation succeeded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
