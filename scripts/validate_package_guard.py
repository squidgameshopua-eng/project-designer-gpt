#!/usr/bin/env python3
"""Minimal deterministic guard for PB-anchor Thin Kernel packages.

This script guards the new architecture by checking the compact instruction
anchors, manifest/source scope, registry/test presence, and upload boundaries.
It intentionally does not require obsolete long exact instruction phrases.
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


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    required_paths = [
        INSTRUCTIONS,
        MANIFEST,
        SOURCE / "protected_behavior_registry.md",
        SOURCE / "testing_protocol.md",
        SOURCE / "regression_smoke_tests.md",
        SOURCE / "no_premature_user_handoff_protocol.md",
        ROOT / "package_linter.py",
        ROOT / "scripts/build_knowledge_package.py",
    ]
    for path in required_paths:
        if not path.exists():
            return fail(f"missing path: {path.relative_to(ROOT)}")

    manifest = json.loads(read(MANIFEST))
    if manifest.get("active_source_of_truth") != "current/":
        return fail("manifest active_source_of_truth must be current/")
    if manifest.get("instruction_file") != "current/instructions/Instructions.md":
        return fail("manifest instruction_file must target current/instructions/Instructions.md")
    if str(manifest.get("project_sources_folder", "")).rstrip("/") != "current/source_files":
        return fail("manifest project_sources_folder must target current/source_files/")

    active = manifest.get("active_source_files")
    if not isinstance(active, list) or active != sorted(active):
        return fail("active_source_files must be a sorted list")
    for filename in active:
        if not isinstance(filename, str) or "/" in filename or "\\" in filename or not (SOURCE / filename).exists():
            return fail(f"invalid active source file: {filename}")

    coverage = manifest.get("protected_behavior_coverage", {})
    for pb_id in ["PB-00", "PB-00A", "PB-00B"] + [f"PB-{n:02d}" for n in range(47, 69)]:
        if not coverage.get(pb_id):
            return fail(f"manifest missing coverage for {pb_id}")
    if "no_premature_user_handoff_protocol.md" not in coverage.get("PB-68", []):
        return fail("PB-68 must be mapped to no_premature_user_handoff_protocol.md")

    upload_rule = manifest.get("chatgpt_project_upload_rule", {}).get("project_sources", "")
    for marker in ["package_manifest.json", "package_linter.py", "scripts/", ".github/workflows/", "tests/", "reports/", "evals/", "archive/", "deliveries/", "external_sources/"]:
        if marker not in upload_rule:
            return fail(f"upload rule must forbid {marker} as active Knowledge")

    instruction = read(INSTRUCTIONS)
    if not (1200 <= len(instruction) <= 8000):
        return fail(f"instruction length outside valid range: {len(instruction)}")
    for anchor in ["Authority", "lower-authority protocol files", "not hidden instructions", "Request Check", "audit-plus-patch", "PB-00..68", "protected_behavior_registry.md", "package_manifest.json", "testing_protocol.md", "regression_smoke_tests.md", "Artifact Destination", "Repo-only", "runtime", "evidence", "Patch Lock", "Final gate", "NOT EXECUTED", "verdict"]:
        if anchor not in instruction:
            return fail(f"instruction missing anchor: {anchor}")

    registry = read(SOURCE / "protected_behavior_registry.md")
    for anchor in ["PB-00", "PB-00A", "PB-00B", "PB-47", "PB-66", "PB-67", "Deletion rule", "Right-sized rule", "Line-value test", "Owner map"]:
        if anchor not in registry:
            return fail(f"registry missing anchor: {anchor}")
    if "PB-68" not in read(SOURCE / "no_premature_user_handoff_protocol.md"):
        return fail("PB-68 protocol anchor missing")

    testing = read(SOURCE / "testing_protocol.md")
    for anchor in ["Evidence-grade test", "Patch Lock test", "Instruction-limit test", "Artifact Destination Matrix test", "Rule Admission test"]:
        if anchor not in testing:
            return fail(f"testing_protocol.md missing anchor: {anchor}")

    build_script = read(ROOT / "scripts/build_knowledge_package.py")
    for anchor in ["Instructions.md", "Knowledge/", "active_source_files", "external_sources/"]:
        if anchor not in build_script:
            return fail(f"build script missing anchor: {anchor}")

    print("PASS: PB-anchor package guard validation succeeded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
