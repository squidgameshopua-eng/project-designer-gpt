#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "current/package_manifest/package_manifest.json"
REQUIRED_FILES = [
    ROOT / "current/source_files/delegation_access_policy.md",
    ROOT / ".github/workflows/package_guard.yml",
    ROOT / "scripts/validate_package_guard.py",
]
REQUIRED_ACTIVE_SOURCE = "delegation_access_policy.md"


def fail(msg: str) -> int:
    print(f"FAIL: {msg}")
    return 1


def main() -> int:
    for file_path in REQUIRED_FILES:
        if not file_path.exists():
            return fail(f"Missing required file: {file_path.relative_to(ROOT)}")

    if not MANIFEST_PATH.exists():
        return fail("Missing manifest file")

    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        return fail(f"Unable to parse manifest JSON: {exc}")

    if manifest.get("active_source_of_truth") != "current/":
        return fail("active_source_of_truth must be 'current/'")

    active_files = manifest.get("active_source_files")
    if not isinstance(active_files, list):
        return fail("active_source_files must be a list")

    if REQUIRED_ACTIVE_SOURCE not in active_files:
        return fail(
            "delegation_access_policy.md must be listed in active_source_files"
        )

    print("PASS: package guard validation succeeded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
