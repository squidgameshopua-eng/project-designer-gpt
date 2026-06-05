#!/usr/bin/env python3
"""Build the GitHub Instruction/Knowledge delivery ZIP for project-designer-gpt.

The generated artifact separates the Project/GPT instruction text from Knowledge
source files so a repository-backed package can be uploaded without mixing
archive, test, script, workflow, or reference folders into active Knowledge.
"""
from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT_DIR = ROOT / "current"
MANIFEST_PATH = CURRENT_DIR / "package_manifest" / "package_manifest.json"
SOURCE_DIR = CURRENT_DIR / "source_files"
INSTRUCTION_LIMIT = 8000
FORBIDDEN_NAME_MARKERS = (
    "corrected_",
    "final_",
    "draft_",
    "v2_",
    "backup_",
    "old_",
    "superseded",
)


def fail(message: str) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    return 1


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def validate_manifest(manifest: dict) -> tuple[Path, list[str]]:
    if manifest.get("active_source_of_truth") != "current/":
        raise ValueError("active_source_of_truth must be current/")

    instruction_file = manifest.get("instruction_file")
    if not isinstance(instruction_file, str) or not instruction_file:
        raise ValueError("manifest instruction_file must be a non-empty string")
    instruction_path = (ROOT / instruction_file).resolve()
    if instruction_path != (CURRENT_DIR / "instructions" / "Instructions.md").resolve():
        raise ValueError("instruction_file must be current/instructions/Instructions.md")
    if not instruction_path.exists():
        raise ValueError("instruction file is missing")
    instruction_len = len(instruction_path.read_text(encoding="utf-8"))
    if instruction_len > INSTRUCTION_LIMIT:
        raise ValueError(f"Instructions.md exceeds {INSTRUCTION_LIMIT} characters")

    active_files = manifest.get("active_source_files")
    if not isinstance(active_files, list) or not active_files:
        raise ValueError("active_source_files must be a non-empty list")
    if sorted(active_files) != active_files:
        raise ValueError("active_source_files must be sorted for deterministic delivery")

    validated: list[str] = []
    for item in active_files:
        if not isinstance(item, str) or not item:
            raise ValueError("active_source_files entries must be non-empty strings")
        path = Path(item)
        if path.name != item or path.is_absolute() or ".." in path.parts:
            raise ValueError(f"active source entry must be a filename only: {item}")
        lowered = item.lower()
        if any(marker in lowered for marker in FORBIDDEN_NAME_MARKERS):
            raise ValueError(f"active source entry uses forbidden version marker: {item}")
        source_path = (SOURCE_DIR / item).resolve()
        try:
            source_path.relative_to(SOURCE_DIR.resolve())
        except ValueError as exc:
            raise ValueError(f"active source escapes current/source_files/: {item}") from exc
        if not source_path.exists():
            raise ValueError(f"active source file missing: {item}")
        validated.append(item)
    return instruction_path, validated


def guide_text(manifest: dict, instruction_len: int, active_files: list[str]) -> str:
    files = "\n".join(f"- {name}" for name in active_files)
    return f"""# GitHub Instruction/Knowledge Delivery Package

Repository package: {manifest.get('package_name', 'project-designer-gpt')}
Active source of truth: current/
Instruction count: {instruction_len}/{INSTRUCTION_LIMIT}

## Upload format
1. Paste `Instructions.md` into the Project/GPT Instructions field.
2. Upload every file in `Knowledge/` as Project/GPT Knowledge or project source files.
3. Keep `package_manifest.json` and this `UPLOAD_GUIDE.md` as delivery evidence unless the UI accepts only Knowledge files.

## Knowledge files
{files}

## Excluded from active Knowledge
archive/, deliveries/, external_sources/, tests/, scripts/, .github/, old/corrected/final/draft variants, and any file not listed in `current/package_manifest/package_manifest.json`.

Project/GPT Instructions remain higher authority than Knowledge files. Knowledge files are support material, not hidden instructions.
"""


def add_text(zf: zipfile.ZipFile, arcname: str, text: str) -> None:
    info = zipfile.ZipInfo(arcname)
    info.date_time = (1980, 1, 1, 0, 0, 0)
    info.compress_type = zipfile.ZIP_DEFLATED
    zf.writestr(info, text.encode("utf-8"))


def build(output: Path) -> None:
    manifest = load_manifest()
    instruction_path, active_files = validate_manifest(manifest)
    instruction_text = instruction_path.read_text(encoding="utf-8")
    manifest_text = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)

    entries: list[tuple[str, str]] = [
        ("Instructions.md", instruction_text),
        ("UPLOAD_GUIDE.md", guide_text(manifest, len(instruction_text), active_files)),
        ("package_manifest.json", manifest_text),
    ]
    for file_name in active_files:
        entries.append((f"Knowledge/{file_name}", (SOURCE_DIR / file_name).read_text(encoding="utf-8")))

    with zipfile.ZipFile(output, "w") as zf:
        for arcname, text in sorted(entries, key=lambda item: item[0]):
            add_text(zf, arcname, text)

    with zipfile.ZipFile(output, "r") as zf:
        names = zf.namelist()
    expected = sorted(arcname for arcname, _ in entries)
    if names != expected:
        raise ValueError("ZIP entries are not deterministic or complete")
    print(f"PASS: built {output} with {len(active_files)} Knowledge files and Instructions.md {len(instruction_text)}/{INSTRUCTION_LIMIT} chars")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build GitHub Instruction/Knowledge delivery ZIP.")
    parser.add_argument("--output", required=True, type=Path, help="Output ZIP path")
    args = parser.parse_args()
    try:
        build(args.output)
    except Exception as exc:
        return fail(str(exc))
    return 0


if __name__ == "__main__":
    sys.exit(main())
