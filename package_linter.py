#!/usr/bin/env python3
"""Mechanical package linter for the PB-anchor Thin Kernel architecture.

The linter validates the active current/ package, manifest ownership,
repo-only upload boundaries, and compact Project Instructions anchors without
requiring obsolete long-form wording in Instructions.md.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

DEFAULT_INSTRUCTION_LIMIT = 8000
PREFERRED_INSTRUCTION_LIMIT = 4200
DEFAULT_MANIFEST = Path("current/package_manifest/package_manifest.json")
CURRENT_DIR = Path("current")
SOURCE_DIR = CURRENT_DIR / "source_files"
INSTRUCTION_FILE = CURRENT_DIR / "instructions/Instructions.md"

REQUIRED_ACTIVE_SOURCE_FILES = {
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
    "package_name",
    "status",
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
    "github_connector_rule",
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

REQUIRED_TEST_SUITE_PATHS = {
    "package_linter.py",
    "scripts/validate_package_guard.py",
    "scripts/validate_rule_admission_guard.py",
    "current/source_files/regression_smoke_tests.md",
}

KERNEL_CRITICAL_PB_IDS = ["PB-00", "PB-00A", "PB-00B"] + [f"PB-{n:02d}" for n in range(1, 69)]
MANIFEST_REQUIRED_COVERAGE = ["PB-00", "PB-00A", "PB-00B"] + [f"PB-{n:02d}" for n in range(47, 69)]

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
    "Artifact",
    "Repo-only",
    "runtime",
    "evidence",
    "Patch Lock",
    "Final gate",
    "NOT EXECUTED",
    "verdict",
]

OBSOLETE_LONG_FORM_INSTRUCTION_PATTERNS = [
    "Final gate: Request Check,architecture,Super-Pipeline,Hidden Requirements Mining,CEGIS,Mutation Testing,Learning Ledger,External UI Handoff",
    "Kernel self-preservation: preserve User-Facing Russian Output,Minimal User Action,Target Placement and Result Lock,Problem-Class Generalization,End-to-End Handoff",
    "website/app/interface/tool exact link/screen/panel/field/button,paste/start/submit/wait/post-run/result/evidence",
    "manifest/linter/scripts/.github/workflows/tests/reports/UPLOAD_GUIDE/CODEX/archive/deliveries/ZIPs=repo evidence",
]

REQUIRED_SOURCE_TERMS = {
    "protected_behavior_registry.md": ["Deletion rule", "Right-sized rule", "Line-value test", "Owner map", "PB-66", "PB-67"],
    "testing_protocol.md": ["Evidence-grade test", "Patch Lock test", "Protected-registry regression test", "Deletion-burden test", "Right-sized architecture test", "Instruction-limit test", "Rule Admission test"],
    "instruction_governance.md": ["Thin Kernel", "Project Instructions", "lower-authority", "Rule Admission Gate"],
    "rule_admission_protocol.md": ["Rule Admission", "Kernel-critical", "owner file"],
    "no_premature_user_handoff_protocol.md": ["PB-68", "No premature user handoff", "system routes"],
    "delivery_protocol.md": ["Artifact Destination Contract", "ChatGPT upload package = `Instructions.md` plus `Knowledge/*.md` only"],
    "output_templates.md": ["Artifact Destination Matrix", "copy-ready"],
    "package_state_protocol.md": ["GitHub Stable basis", "Candidate PR basis", "ChatGPT runtime active basis"],
    "regression_smoke_tests.md": ["T13", "T14", "T15", "T16", "Fail"],
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

BANNED_ACTIVE_NAME_RE = re.compile(r"(^|[_\-.])(corrected|final|draft|v\d+|backup|old|superseded)([_\-.]|$)", re.I)
EXPECTED_CURRENT_SUBDIRS = {"instructions", "source_files", "package_manifest"}


@dataclass
class Finding:
    severity: str
    check: str
    path: str
    message: str


def posix(path: Path) -> str:
    return path.as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def add(findings: list[Finding], severity: str, check: str, path: Path | str, message: str) -> None:
    findings.append(Finding(severity, check, str(path), message))


def ensure_path(repo: Path, rel: str | Path, findings: list[Finding]) -> bool:
    path = repo / rel
    if path.exists():
        add(findings, "INFO", "exists", rel, "Exists.")
        return True
    add(findings, "ERROR", "exists", rel, "Missing.")
    return False


def load_manifest(repo: Path, findings: list[Finding]) -> dict[str, Any] | None:
    path = repo / DEFAULT_MANIFEST
    if not path.exists():
        add(findings, "ERROR", "manifest", DEFAULT_MANIFEST, "Manifest missing.")
        return None
    try:
        manifest = json.loads(read_text(path))
    except Exception as exc:
        add(findings, "ERROR", "manifest", DEFAULT_MANIFEST, f"Manifest invalid JSON: {exc}")
        return None
    add(findings, "INFO", "manifest", DEFAULT_MANIFEST, "Manifest valid JSON.")
    return manifest


def check_manifest(repo: Path, manifest: dict[str, Any], findings: list[Finding]) -> None:
    missing = sorted(REQUIRED_MANIFEST_KEYS - set(manifest))
    if missing:
        add(findings, "ERROR", "manifest_schema", DEFAULT_MANIFEST, f"Missing manifest keys: {missing}")

    if manifest.get("active_source_of_truth") != "current/":
        add(findings, "ERROR", "active_source_of_truth", DEFAULT_MANIFEST, "active_source_of_truth must be current/.")
    if manifest.get("instruction_file") != "current/instructions/Instructions.md":
        add(findings, "ERROR", "instruction_file", DEFAULT_MANIFEST, "instruction_file must be current/instructions/Instructions.md.")
    if str(manifest.get("project_sources_folder", "")).rstrip("/") != "current/source_files":
        add(findings, "ERROR", "project_sources_folder", DEFAULT_MANIFEST, "project_sources_folder must be current/source_files/.")

    active_files = manifest.get("active_source_files", [])
    if not isinstance(active_files, list) or not all(isinstance(x, str) for x in active_files):
        add(findings, "ERROR", "active_source_files", DEFAULT_MANIFEST, "active_source_files must be a list of filenames.")
        active_files = []
    if active_files != sorted(active_files):
        add(findings, "ERROR", "active_source_files", DEFAULT_MANIFEST, "active_source_files must be sorted.")
    missing_sources = sorted(REQUIRED_ACTIVE_SOURCE_FILES - set(active_files))
    extra_sources = sorted(set(active_files) - REQUIRED_ACTIVE_SOURCE_FILES)
    if missing_sources:
        add(findings, "ERROR", "active_source_files", DEFAULT_MANIFEST, f"Missing active source files: {missing_sources}")
    if extra_sources:
        add(findings, "WARNING", "active_source_files", DEFAULT_MANIFEST, f"Extra non-standard active source files: {extra_sources}")

    roles = manifest.get("file_roles", {})
    if not isinstance(roles, dict):
        add(findings, "ERROR", "file_roles", DEFAULT_MANIFEST, "file_roles must be an object.")
        roles = {}
    for filename in active_files:
        role = roles.get(filename)
        if not isinstance(role, str) or len(role.strip()) < 12:
            add(findings, "ERROR", "file_roles", DEFAULT_MANIFEST, f"Missing meaningful role for {filename}.")

    coverage = manifest.get("protected_behavior_coverage", {})
    if not isinstance(coverage, dict):
        add(findings, "ERROR", "pb_coverage", DEFAULT_MANIFEST, "protected_behavior_coverage must be an object.")
        coverage = {}
    for pb_id in MANIFEST_REQUIRED_COVERAGE:
        owners = coverage.get(pb_id)
        if not isinstance(owners, list) or not owners:
            add(findings, "ERROR", "pb_coverage", DEFAULT_MANIFEST, f"Missing coverage for {pb_id}.")
    if "no_premature_user_handoff_protocol.md" not in coverage.get("PB-68", []):
        add(findings, "ERROR", "pb_coverage", DEFAULT_MANIFEST, "PB-68 coverage must include no_premature_user_handoff_protocol.md.")

    tests = set(manifest.get("required_test_suites", [])) if isinstance(manifest.get("required_test_suites"), list) else set()
    for suite in REQUIRED_TEST_SUITE_PATHS:
        if suite not in tests:
            add(findings, "ERROR", "required_test_suites", DEFAULT_MANIFEST, f"Missing required test suite: {suite}")
        elif not (repo / suite).exists():
            add(findings, "ERROR", "required_test_suites", suite, "Required test path missing.")

    gates = set(manifest.get("release_gates", [])) if isinstance(manifest.get("release_gates"), list) else set()
    for gate in REQUIRED_RELEASE_GATES:
        if gate not in gates:
            add(findings, "ERROR", "release_gates", DEFAULT_MANIFEST, f"Missing release gate: {gate}")

    upload_rule = manifest.get("chatgpt_project_upload_rule", {}).get("project_sources", "") if isinstance(manifest.get("chatgpt_project_upload_rule"), dict) else ""
    for marker in FORBIDDEN_UPLOAD_MARKERS:
        if marker not in upload_rule:
            add(findings, "ERROR", "upload_rule", DEFAULT_MANIFEST, f"Upload rule must forbid {marker} as active Knowledge.")


def check_tree(repo: Path, manifest: dict[str, Any], findings: list[Finding]) -> None:
    for rel in ["current", "current/instructions", "current/source_files", "current/package_manifest", "scripts/validate_package_guard.py", "scripts/build_knowledge_package.py", "package_linter.py"]:
        ensure_path(repo, rel, findings)
    current = repo / CURRENT_DIR
    if current.exists():
        subdirs = {p.name for p in current.iterdir() if p.is_dir()}
        if subdirs != EXPECTED_CURRENT_SUBDIRS:
            add(findings, "ERROR", "current_subdirs", CURRENT_DIR, f"Expected {sorted(EXPECTED_CURRENT_SUBDIRS)}, found {sorted(subdirs)}")
        for p in current.rglob("*"):
            rel = p.relative_to(repo)
            if p.is_file() and p.name.startswith("."):
                add(findings, "ERROR", "hidden_current_file", rel, "Hidden/dotfile under current/ is not allowed.")
    active_files = manifest.get("active_source_files", []) if isinstance(manifest.get("active_source_files"), list) else []
    source_dir = repo / SOURCE_DIR
    actual = {p.name for p in source_dir.iterdir() if p.is_file()} if source_dir.exists() else set()
    expected = set(active_files)
    for name in sorted(expected - actual):
        add(findings, "ERROR", "source_files_missing", SOURCE_DIR / name, "Manifest-listed file missing.")
    for name in sorted(actual - expected):
        add(findings, "ERROR", "source_files_extra", SOURCE_DIR / name, "File present but absent from manifest.")
    for name in sorted(actual | expected):
        if BANNED_ACTIVE_NAME_RE.search(name):
            add(findings, "ERROR", "banned_active_filename", SOURCE_DIR / name, "Active source filename uses old/final/draft/version marker.")
        if name in expected and not name.endswith(".md"):
            add(findings, "ERROR", "source_extension", SOURCE_DIR / name, "Active source file must be .md.")


def check_instruction(repo: Path, findings: list[Finding]) -> None:
    path = repo / INSTRUCTION_FILE
    if not path.exists():
        return
    text = read_text(path)
    chars = len(text)
    if chars > DEFAULT_INSTRUCTION_LIMIT:
        add(findings, "ERROR", "instruction_limit", INSTRUCTION_FILE, f"Instruction has {chars} chars > {DEFAULT_INSTRUCTION_LIMIT}.")
    elif chars > PREFERRED_INSTRUCTION_LIMIT:
        add(findings, "WARNING", "instruction_preferred_size", INSTRUCTION_FILE, f"Instruction has {chars} chars; preferred PB-anchor max is {PREFERRED_INSTRUCTION_LIMIT}.")
    else:
        add(findings, "INFO", "instruction_limit", INSTRUCTION_FILE, f"Instruction has {chars}/{DEFAULT_INSTRUCTION_LIMIT} chars.")
    for phrase in INSTRUCTION_ANCHORS:
        if phrase not in text:
            add(findings, "ERROR", "instruction_anchor", INSTRUCTION_FILE, f"Missing PB-anchor kernel phrase: {phrase}")
    for pattern in OBSOLETE_LONG_FORM_INSTRUCTION_PATTERNS:
        if pattern in text:
            add(findings, "ERROR", "instruction_bloat", INSTRUCTION_FILE, f"Obsolete long-form wording survived: {pattern[:80]}...")


def check_source_content(repo: Path, findings: list[Finding]) -> None:
    for filename, terms in REQUIRED_SOURCE_TERMS.items():
        path = repo / SOURCE_DIR / filename
        if not path.exists():
            add(findings, "ERROR", "source_required_content", path, "Required source file missing.")
            continue
        text = read_text(path)
        for term in terms:
            if term not in text:
                add(findings, "ERROR", "source_required_content", path, f"Missing expected term: {term}")
    registry = read_text(repo / SOURCE_DIR / "protected_behavior_registry.md")
    for pb_id in ["PB-00", "PB-00A", "PB-00B"] + [f"PB-{n:02d}" for n in range(1, 68)]:
        if pb_id not in registry:
            add(findings, "ERROR", "registry_pb", SOURCE_DIR / "protected_behavior_registry.md", f"Missing {pb_id}.")
    if "PB-68" not in registry and not (repo / SOURCE_DIR / "no_premature_user_handoff_protocol.md").exists():
        add(findings, "ERROR", "registry_pb68", SOURCE_DIR / "protected_behavior_registry.md", "PB-68 must be in registry or owned by no_premature_user_handoff_protocol.md.")


def check_build_scope(repo: Path, findings: list[Finding]) -> None:
    build = read_text(repo / "scripts/build_knowledge_package.py")
    for phrase in ["Instructions.md", "Knowledge/", "active_source_files", 'name == "Instructions.md" or name.startswith("Knowledge/")']:
        if phrase not in build:
            add(findings, "ERROR", "build_scope", "scripts/build_knowledge_package.py", f"Missing build scope phrase: {phrase}")
    for marker in FORBIDDEN_UPLOAD_MARKERS:
        if marker not in build:
            add(findings, "ERROR", "build_scope", "scripts/build_knowledge_package.py", f"Missing forbidden upload marker: {marker}")


def summarize(findings: list[Finding]) -> dict[str, int]:
    return {level: sum(1 for f in findings if f.severity == level) for level in ["ERROR", "WARNING", "INFO"]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    findings: list[Finding] = []
    manifest = load_manifest(repo, findings)
    if manifest is not None:
        check_manifest(repo, manifest, findings)
        check_tree(repo, manifest, findings)
    check_instruction(repo, findings)
    check_source_content(repo, findings)
    check_build_scope(repo, findings)

    summary = summarize(findings)
    if args.json:
        print(json.dumps({"summary": summary, "findings": [asdict(f) for f in findings]}, ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f"{f.severity}: [{f.check}] {f.path}: {f.message}")
        print(f"SUMMARY: {summary}")
    return 1 if summary["ERROR"] else 0


if __name__ == "__main__":
    sys.exit(main())
