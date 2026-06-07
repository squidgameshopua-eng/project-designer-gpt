#!/usr/bin/env python3
"""
package_linter.py — mechanical package checker for project-designer-gpt.

Purpose:
- Verify that GitHub current/ package matches current/package_manifest/package_manifest.json.
- Catch hidden/extra files such as .gitkeep in active folders.
- Catch missing active files, stale filenames, instruction-limit failures, and lost kernel terms.
- Validate release-control manifest metadata, repo-only eval/report separation, and Knowledge upload scope.

Usage from repository root:
    python package_linter.py
    python package_linter.py --repo .
    python package_linter.py --json

Exit code:
    0 = PASS, no errors
    1 = FAIL, one or more errors
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

DEFAULT_INSTRUCTION_LIMIT = 8000
DEFAULT_MANIFEST = Path("current/package_manifest/package_manifest.json")

REQUIRED_ACTIVE_SOURCE_FILES = {
    "architecture_domain_rules.md",
    "autonomous_workflow_router.md",
    "counterexample_improvement_protocol.md",
    "delegation_access_policy.md",
    "delivery_protocol.md",
    "gpt_action_discovery_protocol.md",
    "instruction_governance.md",
    "mutation_testing_protocol.md",
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

REQUIRED_MANIFEST_KEYS = [
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
    "external_eval_layers",
    "non_active_folders",
    "chatgpt_project_upload_rule",
    "github_connector_rule",
]

REQUIRED_RELEASE_GATES = {
    "manifest_schema_pass",
    "package_linter_pass",
    "package_guard_pass",
    "rule_admission_guard_pass",
    "regression_selection_reported",
    "external_eval_status_recorded",
    "auditor_pass_before_stable",
    "runtime_activation_not_claimed_without_evidence",
}

REQUIRED_EXTERNAL_EVAL_LAYERS = {
    "promptfoo",
    "inspect_ai",
    "garak_or_harmbench",
    "langfuse_style_ledger",
}

REQUIRED_TEST_SUITE_PATHS = {
    "package_linter.py",
    "scripts/validate_package_guard.py",
    "scripts/validate_rule_admission_guard.py",
    "current/source_files/regression_smoke_tests.md",
}

REQUIRED_INSTRUCTION_TERMS = [
    "Request Check",
    "audit-plus-patch",
    "Architecture first",
    "Combination Search",
    "Action Discovery",
    "Patch State Machine",
    "Patch Lock",
    "Builder/Auditor",
    "Kernel self-preservation",
    "Current package truth",
    "Right-sized architecture",
    "Behavior-only files",
    "protected_behavior_registry.md",
    "testing_protocol.md",
    "Child-system inheritance",
    "Final gate",
    "Artifact Destination Contract",
    "Repo-only Controls Exclusion",
    "Codex/GitHub Direct Handoff",
    "Runtime Activation Check",
]

REQUIRED_SOURCE_TERMS = {
    "autonomous_workflow_router.md": [
        "Execution substrate selection rule",
        "Verification fallback",
        "User-work minimization rule",
    ],
    "delegation_access_policy.md": [
        "User-work minimization authority rule",
        "Evidence claim gate",
        "Rational route gate",
    ],
    "patch_lock_protocol.md": ["Patch Lock", "Invalid Delivery", "Builder/Auditor", "Patch State Machine"],
    "protected_behavior_registry.md": ["PB-00", "PB-00A", "PB-00B", "PB-22", "PB-56", "PB-57", "PB-58", "PB-59", "Artifact Destination Contract", "Repo-only Controls Exclusion", "GitHub/Codex Direct Handoff Contract", "Runtime Activation / Old Branch Non-equivalence", "protected behavior"],
    "testing_protocol.md": ["Patch Lock test", "Patch State Machine test", "Builder/Auditor test", "Hard pass threshold", "Artifact Destination Matrix test", "Repo-only Controls Exclusion test", "Direct Codex/GitHub Handoff test", "Runtime Activation / old-branch non-equivalence test"],
    "delivery_protocol.md": ["Patch Lock delivery blocker", "complete current", "No snippets-only", "Artifact Destination Contract delivery blocker", "ChatGPT upload package = `Instructions.md` plus `Knowledge/*.md` only"],
    "package_state_protocol.md": ["Active package basis", "evidence only", "canonical", "ChatGPT runtime active basis", "GitHub Stable basis", "Candidate PR basis", "Local package basis"],
    "regression_smoke_tests.md": ["T01", "T04", "T12", "T13", "T14", "T15", "T16", "T28", "T29", "T30", "T31", "T32", "Fail"],
    "project_design_super_pipeline_protocol.md": ["Super-Pipeline", "Hidden Requirements Mining", "CEGIS", "Mutation Testing", "Learning Ledger", "Pareto Ranking"],
    "counterexample_improvement_protocol.md": ["Counterexample-Guided Improvement", "CEGIS", "counterexample"],
    "mutation_testing_protocol.md": ["Mutation Testing", "mutation", "protected behavior"],
    "project_learning_ledger.md": ["Learning Ledger", "failure class", "evidence layer"],
    "rule_admission_protocol.md": ["Rule Admission", "Thin Kernel", "owner file"],
}

BANNED_ACTIVE_NAME_RE = re.compile(
    r"(^|[_\-.])(corrected|final|draft|v\d+|backup|old|superseded)([_\-.]|$)",
    re.IGNORECASE,
)

EXPECTED_CURRENT_SUBDIRS = {"instructions", "source_files", "package_manifest"}


@dataclass
class Finding:
    severity: str  # ERROR, WARNING, INFO
    check: str
    path: str
    message: str


def posix(path: Path) -> str:
    return path.as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def add(findings: list[Finding], severity: str, check: str, path: Path | str, message: str) -> None:
    findings.append(Finding(severity, check, str(path), message))


def load_manifest(repo: Path, findings: list[Finding]) -> dict[str, Any] | None:
    manifest_path = repo / DEFAULT_MANIFEST
    if not manifest_path.exists():
        add(findings, "ERROR", "manifest_exists", DEFAULT_MANIFEST, "Manifest file is missing.")
        return None
    try:
        data = json.loads(read_text(manifest_path))
    except Exception as exc:
        add(findings, "ERROR", "manifest_json", DEFAULT_MANIFEST, f"Manifest is not valid JSON: {exc}")
        return None
    add(findings, "INFO", "manifest_json", DEFAULT_MANIFEST, "Manifest exists and is valid JSON.")
    return data


def ensure_string(manifest: dict[str, Any], key: str, findings: list[Finding]) -> str | None:
    val = manifest.get(key)
    if not isinstance(val, str) or not val.strip():
        add(findings, "ERROR", "manifest_schema", DEFAULT_MANIFEST, f"Manifest key {key!r} must be a non-empty string.")
        return None
    return val


def ensure_list_of_strings(manifest: dict[str, Any], key: str, findings: list[Finding]) -> list[str]:
    val = manifest.get(key)
    if not isinstance(val, list) or not all(isinstance(x, str) and x.strip() for x in val):
        add(findings, "ERROR", "manifest_schema", DEFAULT_MANIFEST, f"Manifest key {key!r} must be a list of non-empty strings.")
        return []
    return val


def list_files_direct(folder: Path) -> set[str]:
    if not folder.exists():
        return set()
    return {p.name for p in folder.iterdir() if p.is_file()}


def list_all_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted([p for p in root.rglob("*") if p.is_file()])


def check_manifest_and_structure(repo: Path, manifest: dict[str, Any], findings: list[Finding]) -> dict[str, Path | list[str]]:
    active_root_s = ensure_string(manifest, "active_source_of_truth", findings) or "current/"
    instruction_file_s = ensure_string(manifest, "instruction_file", findings) or "current/instructions/Instructions.md"
    source_folder_s = ensure_string(manifest, "project_sources_folder", findings) or "current/source_files/"
    manifest_file_s = ensure_string(manifest, "manifest_file", findings) or posix(DEFAULT_MANIFEST)
    active_source_files = ensure_list_of_strings(manifest, "active_source_files", findings)

    active_root = repo / active_root_s
    instruction_file = repo / instruction_file_s
    source_folder = repo / source_folder_s
    manifest_file = repo / manifest_file_s

    for check, path in [
        ("active_root_exists", active_root),
        ("instruction_file_exists", instruction_file),
        ("source_folder_exists", source_folder),
        ("manifest_file_exists", manifest_file),
    ]:
        if path.exists():
            add(findings, "INFO", check, path.relative_to(repo), "Exists.")
        else:
            add(findings, "ERROR", check, path.relative_to(repo), "Missing.")

    if active_root_s.rstrip("/") != "current":
        add(findings, "ERROR", "active_source_of_truth", active_root_s, "active_source_of_truth should be current/.")

    if instruction_file_s != "current/instructions/Instructions.md":
        add(findings, "ERROR", "instruction_file_path", instruction_file_s, "instruction_file should be current/instructions/Instructions.md.")

    if source_folder_s.rstrip("/") != "current/source_files":
        add(findings, "ERROR", "source_folder_path", source_folder_s, "project_sources_folder should be current/source_files/.")

    if manifest_file_s != "current/package_manifest/package_manifest.json":
        add(findings, "ERROR", "manifest_file_path", manifest_file_s, "manifest_file should be current/package_manifest/package_manifest.json.")

    if len(active_source_files) != len(set(active_source_files)):
        dupes = sorted({x for x in active_source_files if active_source_files.count(x) > 1})
        add(findings, "ERROR", "active_source_files_duplicates", DEFAULT_MANIFEST, f"Duplicate active_source_files: {dupes}")

    if active_source_files != sorted(active_source_files):
        add(findings, "ERROR", "active_source_files_sorted", DEFAULT_MANIFEST, "active_source_files must be sorted for deterministic packaging.")

    missing_required = sorted(REQUIRED_ACTIVE_SOURCE_FILES - set(active_source_files))
    extra_manifest = sorted(set(active_source_files) - REQUIRED_ACTIVE_SOURCE_FILES)
    if missing_required:
        add(findings, "ERROR", "required_source_files", DEFAULT_MANIFEST, f"Manifest missing required active source files: {missing_required}")
    if extra_manifest:
        add(findings, "WARNING", "manifest_extra_source_files", DEFAULT_MANIFEST, f"Manifest lists non-standard source files: {extra_manifest}")

    return {
        "active_root": active_root,
        "instruction_file": instruction_file,
        "source_folder": source_folder,
        "manifest_file": manifest_file,
        "active_source_files": active_source_files,
    }


def check_manifest_control_metadata(repo: Path, manifest: dict[str, Any], active_source_files: list[str], findings: list[Finding]) -> None:
    for key in REQUIRED_MANIFEST_KEYS:
        if key not in manifest:
            add(findings, "ERROR", "manifest_required_keys", DEFAULT_MANIFEST, f"Missing manifest key: {key}")

    file_roles = manifest.get("file_roles")
    if not isinstance(file_roles, dict):
        add(findings, "ERROR", "manifest_file_roles", DEFAULT_MANIFEST, "file_roles must be an object mapping every active source file to a role.")
    else:
        missing_roles = sorted(set(active_source_files) - set(file_roles))
        extra_roles = sorted(set(file_roles) - set(active_source_files))
        if missing_roles:
            add(findings, "ERROR", "manifest_file_roles", DEFAULT_MANIFEST, f"Missing file_roles for active files: {missing_roles}")
        if extra_roles:
            add(findings, "ERROR", "manifest_file_roles", DEFAULT_MANIFEST, f"file_roles contains non-active files: {extra_roles}")
        for name, role in file_roles.items():
            if not isinstance(role, str) or len(role.strip()) < 12:
                add(findings, "ERROR", "manifest_file_roles", DEFAULT_MANIFEST, f"file_roles[{name!r}] must be a meaningful non-empty role string.")

    coverage = manifest.get("protected_behavior_coverage")
    if not isinstance(coverage, dict):
        add(findings, "ERROR", "manifest_pb_coverage", DEFAULT_MANIFEST, "protected_behavior_coverage must be an object.")
    else:
        required_pb = {"PB-00", "PB-00A", "PB-00B"} | {f"PB-{n:02d}" for n in range(47, 66)}
        missing_pb = sorted(required_pb - set(coverage))
        if missing_pb:
            add(findings, "ERROR", "manifest_pb_coverage", DEFAULT_MANIFEST, f"Missing protected_behavior_coverage IDs: {missing_pb}")
        for pb_id, owners in coverage.items():
            if not re.fullmatch(r"PB-(00A|00B|\d{2})", str(pb_id)):
                add(findings, "ERROR", "manifest_pb_coverage", DEFAULT_MANIFEST, f"Invalid PB ID in protected_behavior_coverage: {pb_id}")
            if not isinstance(owners, list) or not all(isinstance(x, str) and x.strip() for x in owners):
                add(findings, "ERROR", "manifest_pb_coverage", DEFAULT_MANIFEST, f"Coverage for {pb_id} must be a list of owner paths/files.")

    test_suites = manifest.get("required_test_suites")
    if not isinstance(test_suites, list) or not all(isinstance(x, str) and x.strip() for x in test_suites):
        add(findings, "ERROR", "manifest_required_test_suites", DEFAULT_MANIFEST, "required_test_suites must be a list of strings.")
    else:
        missing_required_suites = sorted(REQUIRED_TEST_SUITE_PATHS - set(test_suites))
        if missing_required_suites:
            add(findings, "ERROR", "manifest_required_test_suites", DEFAULT_MANIFEST, f"Missing required test suites: {missing_required_suites}")
        for suite in test_suites:
            if not (repo / suite).exists():
                add(findings, "ERROR", "manifest_required_test_suites", suite, "Required test suite path does not exist.")

    release_gates = manifest.get("release_gates")
    if not isinstance(release_gates, list) or not all(isinstance(x, str) and x.strip() for x in release_gates):
        add(findings, "ERROR", "manifest_release_gates", DEFAULT_MANIFEST, "release_gates must be a list of strings.")
    else:
        missing_gates = sorted(REQUIRED_RELEASE_GATES - set(release_gates))
        if missing_gates:
            add(findings, "ERROR", "manifest_release_gates", DEFAULT_MANIFEST, f"Missing release gates: {missing_gates}")

    external_eval_layers = manifest.get("external_eval_layers")
    if not isinstance(external_eval_layers, dict):
        add(findings, "ERROR", "manifest_external_eval_layers", DEFAULT_MANIFEST, "external_eval_layers must be an object.")
    else:
        missing_layers = sorted(REQUIRED_EXTERNAL_EVAL_LAYERS - set(external_eval_layers))
        if missing_layers:
            add(findings, "ERROR", "manifest_external_eval_layers", DEFAULT_MANIFEST, f"Missing external eval layers: {missing_layers}")

    upload_rule = manifest.get("chatgpt_project_upload_rule", {}).get("project_sources") if isinstance(manifest.get("chatgpt_project_upload_rule"), dict) else ""
    for marker in ("evals/", "reports/", "package_manifest.json", "package_linter.py", "scripts/", ".github/workflows/", "archive/", "deliveries/"):
        if marker not in upload_rule:
            add(findings, "ERROR", "manifest_upload_rule", DEFAULT_MANIFEST, f"chatgpt_project_upload_rule.project_sources must forbid {marker} as active Knowledge.")


def check_current_tree(repo: Path, active_root: Path, findings: list[Finding]) -> None:
    if not active_root.exists():
        return

    actual_subdirs = {p.name for p in active_root.iterdir() if p.is_dir()}
    missing_subdirs = sorted(EXPECTED_CURRENT_SUBDIRS - actual_subdirs)
    extra_subdirs = sorted(actual_subdirs - EXPECTED_CURRENT_SUBDIRS)
    if missing_subdirs:
        add(findings, "ERROR", "current_subdirs", active_root.relative_to(repo), f"Missing current/ subdirectories: {missing_subdirs}")
    if extra_subdirs:
        add(findings, "ERROR", "current_subdirs", active_root.relative_to(repo), f"Unexpected current/ subdirectories: {extra_subdirs}")

    gitkeeps = [p for p in list_all_files(active_root) if p.name == ".gitkeep"]
    if gitkeeps:
        add(findings, "ERROR", "current_gitkeep", active_root.relative_to(repo), "Remove .gitkeep files from active current/: " + ", ".join(posix(p.relative_to(repo)) for p in gitkeeps))
    else:
        add(findings, "INFO", "current_gitkeep", active_root.relative_to(repo), "No .gitkeep files under current/.")

    hidden_files = [p for p in list_all_files(active_root) if p.name.startswith(".")]
    if hidden_files:
        add(findings, "ERROR", "current_hidden_files", active_root.relative_to(repo), "Hidden/dotfiles under current/ are not allowed: " + ", ".join(posix(p.relative_to(repo)) for p in hidden_files))


def check_folder_contents(repo: Path, instruction_file: Path, source_folder: Path, manifest_file: Path, active_source_files: list[str], findings: list[Finding]) -> None:
    instructions_folder = instruction_file.parent
    manifest_folder = manifest_file.parent

    actual_instruction_files = list_files_direct(instructions_folder)
    expected_instruction_files = {instruction_file.name}
    if actual_instruction_files != expected_instruction_files:
        add(findings, "ERROR", "instructions_folder_exact", instructions_folder.relative_to(repo), f"Expected only {sorted(expected_instruction_files)}, found {sorted(actual_instruction_files)}")
    else:
        add(findings, "INFO", "instructions_folder_exact", instructions_folder.relative_to(repo), "Contains only Instructions.md.")

    actual_manifest_files = list_files_direct(manifest_folder)
    expected_manifest_files = {manifest_file.name}
    if actual_manifest_files != expected_manifest_files:
        add(findings, "ERROR", "package_manifest_folder_exact", manifest_folder.relative_to(repo), f"Expected only {sorted(expected_manifest_files)}, found {sorted(actual_manifest_files)}")
    else:
        add(findings, "INFO", "package_manifest_folder_exact", manifest_folder.relative_to(repo), "Contains only package_manifest.json.")

    actual_source_files = list_files_direct(source_folder)
    expected_source_files = set(active_source_files)
    missing = sorted(expected_source_files - actual_source_files)
    extra = sorted(actual_source_files - expected_source_files)
    if missing:
        add(findings, "ERROR", "source_files_missing", source_folder.relative_to(repo), f"Files listed in manifest but absent: {missing}")
    else:
        add(findings, "INFO", "source_files_missing", source_folder.relative_to(repo), "No manifest-listed files are missing.")
    if extra:
        add(findings, "ERROR", "source_files_extra", source_folder.relative_to(repo), f"Files present but absent from manifest: {extra}")
    else:
        add(findings, "INFO", "source_files_extra", source_folder.relative_to(repo), "No extra files in source_files/.")

    for name in sorted(actual_source_files | expected_source_files):
        if BANNED_ACTIVE_NAME_RE.search(name):
            add(findings, "ERROR", "banned_active_filename", source_folder / name, "Active source filename uses banned old/draft/final/versioned naming.")
        if name in expected_source_files and not name.endswith(".md"):
            add(findings, "ERROR", "source_file_extension", source_folder / name, "Active source files should be .md files.")


def check_instruction(repo: Path, instruction_file: Path, limit: int, findings: list[Finding]) -> None:
    if not instruction_file.exists():
        return
    text = read_text(instruction_file)
    char_count = len(text)
    byte_count = len(text.encode("utf-8"))
    if char_count > limit:
        add(findings, "ERROR", "instruction_limit", instruction_file.relative_to(repo), f"Instruction has {char_count} characters > limit {limit}.")
    elif char_count > int(limit * 0.985):
        add(findings, "WARNING", "instruction_limit", instruction_file.relative_to(repo), f"Instruction has {char_count}/{limit} characters; very close to limit.")
    else:
        add(findings, "INFO", "instruction_limit", instruction_file.relative_to(repo), f"Instruction has {char_count}/{limit} characters ({byte_count} UTF-8 bytes).")

    missing_terms = [term for term in REQUIRED_INSTRUCTION_TERMS if term not in text]
    if missing_terms:
        add(findings, "ERROR", "instruction_kernel_terms", instruction_file.relative_to(repo), f"Missing kernel terms: {missing_terms}")
    else:
        add(findings, "INFO", "instruction_kernel_terms", instruction_file.relative_to(repo), "All required kernel terms are present.")

    if "corrected_" in text or "final_" in text or "draft_" in text or "v2_" in text:
        add(findings, "INFO", "instruction_mentions_banned_names", instruction_file.relative_to(repo), "Instruction mentions banned filename patterns; this is acceptable if it is a prohibition rule.")


def check_required_source_content(repo: Path, source_folder: Path, findings: list[Finding]) -> None:
    for filename, terms in REQUIRED_SOURCE_TERMS.items():
        path = source_folder / filename
        if not path.exists():
            add(findings, "ERROR", "source_required_content", path.relative_to(repo), "Required source file missing; content terms not checked.")
            continue
        text = read_text(path)
        missing = [term for term in terms if term not in text]
        if missing:
            add(findings, "ERROR", "source_required_content", path.relative_to(repo), f"Missing expected terms: {missing}")
        else:
            add(findings, "INFO", "source_required_content", path.relative_to(repo), "Expected terms present.")


def check_linter_location(repo: Path, findings: list[Finding]) -> None:
    matches = [p for p in list_all_files(repo) if p.name == "package_linter.py"]
    current_matches = [p for p in matches if "current" in p.relative_to(repo).parts]
    if not matches:
        add(findings, "WARNING", "package_linter_presence", "package_linter.py", "package_linter.py not found in repository root. Add it at repo root, not inside current/source_files/.")
    elif (repo / "package_linter.py") not in matches:
        add(findings, "ERROR", "package_linter_location", "package_linter.py", "package_linter.py exists but not at repository root.")
    else:
        add(findings, "INFO", "package_linter_presence", "package_linter.py", "package_linter.py exists at repository root.")
    if current_matches:
        add(findings, "ERROR", "package_linter_location", "current/", "package_linter.py must not be inside active current/ package.")


def check_non_active_and_root(repo: Path, manifest: dict[str, Any], findings: list[Finding]) -> None:
    non_active = manifest.get("non_active_folders", {})
    if isinstance(non_active, dict):
        for folder_s in non_active:
            folder = repo / folder_s
            if folder.exists():
                add(findings, "INFO", "non_active_folder", folder_s, "Non-active folder exists; treat as evidence only.")
    else:
        add(findings, "WARNING", "non_active_folders", DEFAULT_MANIFEST, "non_active_folders is not a dictionary.")

    active_names = set(manifest.get("active_source_files", [])) | {"Instructions.md", "package_manifest.json"}
    active_like_outside_current: list[str] = []
    for p in list_all_files(repo):
        rel = p.relative_to(repo)
        if rel.parts and rel.parts[0] == "current":
            continue
        if p.name in active_names:
            active_like_outside_current.append(posix(rel))
    if active_like_outside_current:
        add(findings, "WARNING", "active_like_outside_current", ".", "Files with active names exist outside current/; they are evidence only unless explicitly promoted: " + ", ".join(sorted(active_like_outside_current)))


def check_artifact_destination_contract(repo: Path, findings: list[Finding]) -> None:
    instruction_text = read_text(repo / "current/instructions/Instructions.md")
    registry_text = read_text(repo / "current/source_files/protected_behavior_registry.md")
    build_text = read_text(repo / "scripts/build_knowledge_package.py")
    required_instruction = [
        "Artifact Destination Contract",
        "Repo-only Controls Exclusion",
        "Codex/GitHub Direct Handoff",
        "Runtime Activation Check",
        "ChatGPT Project Knowledge",
        "GitHub repo control",
        "do-not-upload",
    ]
    for term in required_instruction:
        if term not in instruction_text:
            add(findings, "ERROR", "artifact_destination_instruction", "current/instructions/Instructions.md", f"Missing destination contract term: {term}")

    for pb_id in ("PB-56", "PB-57", "PB-58", "PB-59"):
        if pb_id not in registry_text:
            add(findings, "ERROR", "artifact_destination_registry", "current/source_files/protected_behavior_registry.md", f"Missing protected behavior ID: {pb_id}")

    forbidden_upload_markers = [
        "package_manifest.json",
        "package_linter.py",
        "scripts/",
        "reports/",
        "evals/",
        ".github/workflows/",
        "UPLOAD_GUIDE.md",
        "CODEX_TASK",
        "archive/",
        "deliveries/",
    ]
    for marker in forbidden_upload_markers:
        if marker not in build_text:
            add(findings, "ERROR", "knowledge_build_scope_guard", "scripts/build_knowledge_package.py", f"Missing forbidden upload marker guard: {marker}")
    if '\n        ("UPLOAD_GUIDE.md"' in build_text or '\n        ("package_manifest.json"' in build_text:
        add(findings, "ERROR", "knowledge_build_scope_guard", "scripts/build_knowledge_package.py", "Upload ZIP entries must not include UPLOAD_GUIDE.md or package_manifest.json.")
    if 'name == "Instructions.md" or name.startswith("Knowledge/")' not in build_text:
        add(findings, "ERROR", "knowledge_build_scope_guard", "scripts/build_knowledge_package.py", "Missing strict Instructions.md/Knowledge/* ZIP scope check.")


def summarize(findings: list[Finding]) -> dict[str, int]:
    return {
        "ERROR": sum(1 for f in findings if f.severity == "ERROR"),
        "WARNING": sum(1 for f in findings if f.severity == "WARNING"),
        "INFO": sum(1 for f in findings if f.severity == "INFO"),
    }


def print_human(findings: list[Finding]) -> None:
    counts = summarize(findings)
    verdict = "PASS" if counts["ERROR"] == 0 else "FAIL"
    print(f"package_linter verdict: {verdict}")
    print(f"Errors: {counts['ERROR']} | Warnings: {counts['WARNING']} | Info: {counts['INFO']}")
    print()
    for sev in ("ERROR", "WARNING", "INFO"):
        group = [f for f in findings if f.severity == sev]
        if not group:
            continue
        print(f"{sev}:")
        for f in group:
            print(f"- [{f.check}] {f.path}: {f.message}")
        print()


def run(repo: Path, instruction_limit: int) -> tuple[list[Finding], int]:
    repo = repo.resolve()
    findings: list[Finding] = []
    if not repo.exists() or not repo.is_dir():
        add(findings, "ERROR", "repo_exists", repo, "Repository path does not exist or is not a directory.")
        return findings, 1

    manifest = load_manifest(repo, findings)
    if manifest is None:
        return findings, 1

    paths = check_manifest_and_structure(repo, manifest, findings)
    active_root = paths["active_root"]  # type: ignore[assignment]
    instruction_file = paths["instruction_file"]  # type: ignore[assignment]
    source_folder = paths["source_folder"]  # type: ignore[assignment]
    manifest_file = paths["manifest_file"]  # type: ignore[assignment]
    active_source_files = paths["active_source_files"]  # type: ignore[assignment]

    assert isinstance(active_root, Path)
    assert isinstance(instruction_file, Path)
    assert isinstance(source_folder, Path)
    assert isinstance(manifest_file, Path)
    assert isinstance(active_source_files, list)

    check_manifest_control_metadata(repo, manifest, active_source_files, findings)
    check_current_tree(repo, active_root, findings)
    check_folder_contents(repo, instruction_file, source_folder, manifest_file, active_source_files, findings)
    check_instruction(repo, instruction_file, instruction_limit, findings)
    check_required_source_content(repo, source_folder, findings)
    check_linter_location(repo, findings)
    check_non_active_and_root(repo, manifest, findings)
    check_artifact_destination_contract(repo, findings)

    exit_code = 1 if summarize(findings)["ERROR"] else 0
    return findings, exit_code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint the project-designer-gpt package structure.")
    parser.add_argument("--repo", default=".", help="Repository root path. Default: current directory.")
    parser.add_argument("--instruction-limit", type=int, default=DEFAULT_INSTRUCTION_LIMIT, help="Project instruction character limit. Default: 8000.")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of human-readable report.")
    args = parser.parse_args(argv)

    findings, exit_code = run(Path(args.repo), args.instruction_limit)
    if args.json:
        print(json.dumps({"summary": summarize(findings), "findings": [asdict(f) for f in findings], "exit_code": exit_code}, ensure_ascii=False, indent=2))
    else:
        print_human(findings)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
