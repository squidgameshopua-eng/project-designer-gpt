#!/usr/bin/env python3
"""Build a GitHub-origin Knowledge ZIP from active current/source_files only."""
from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "current/package_manifest/package_manifest.json"
SOURCE_DIR = ROOT / "current/source_files"
DEFAULT_OUTPUT = ROOT / "knowledge_source_files.zip"
PACKAGE_FOLDER = "knowledge_source_files"
FORBIDDEN_NAMES = {"README.md", "Instructions.md", "package_manifest.json", "manifest.json"}
FORBIDDEN_PREFIXES = (
    "current/",
    "scripts/",
    "tests/",
    ".github/",
    "archive/",
    "deliveries/",
    "external_sources/",
)


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def load_active_files() -> list[str]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    active_files = manifest.get("active_source_files")
    if not isinstance(active_files, list) or not all(isinstance(item, str) and item for item in active_files):
        raise ValueError("manifest active_source_files must be a non-empty list of filenames")
    return active_files


def validate_member_name(name: str, *, folder: bool) -> None:
    if Path(name).name != name or "/" in name or "\\" in name or ".." in Path(name).parts:
        raise ValueError(f"active source entry must be a filename only: {name}")
    if name in FORBIDDEN_NAMES:
        raise ValueError(f"forbidden file name in Knowledge package: {name}")
    arcname = f"{PACKAGE_FOLDER}/{name}" if folder else name
    if any(arcname.startswith(prefix) for prefix in FORBIDDEN_PREFIXES):
        raise ValueError(f"forbidden path in Knowledge package: {arcname}")


def build_zip(output: Path, *, root_files: bool) -> list[str]:
    active_files = load_active_files()
    output.parent.mkdir(parents=True, exist_ok=True)
    members: list[str] = []
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name in active_files:
            validate_member_name(name, folder=not root_files)
            source = (SOURCE_DIR / name).resolve()
            source.relative_to(SOURCE_DIR.resolve())
            if not source.is_file():
                raise FileNotFoundError(f"active source file missing: current/source_files/{name}")
            arcname = name if root_files else f"{PACKAGE_FOLDER}/{name}"
            zf.write(source, arcname)
            members.append(arcname)
    return members


def verify_zip(output: Path, expected_members: list[str]) -> None:
    with zipfile.ZipFile(output, "r") as zf:
        actual = sorted(zf.namelist())
    expected = sorted(expected_members)
    if actual != expected:
        raise ValueError(f"ZIP members differ from expected active source files: {actual} != {expected}")
    for member in actual:
        if member.endswith("/"):
            raise ValueError(f"ZIP must not contain directory entries: {member}")
        if any(member.startswith(prefix) for prefix in FORBIDDEN_PREFIXES):
            raise ValueError(f"ZIP contains forbidden path: {member}")
        if Path(member).name in FORBIDDEN_NAMES:
            raise ValueError(f"ZIP contains forbidden file: {member}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Package only active current/source_files Knowledge files.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output ZIP path.")
    parser.add_argument("--root-files", action="store_true", help="Place Knowledge files at ZIP root instead of knowledge_source_files/.")
    args = parser.parse_args(argv)
    try:
        members = build_zip(args.output, root_files=args.root_files)
        verify_zip(args.output, members)
    except Exception as exc:
        return fail(str(exc))
    print(f"PASS: built {args.output} with {len(members)} active current/source_files Knowledge files")
    for member in sorted(members):
        print(f"- {member}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
