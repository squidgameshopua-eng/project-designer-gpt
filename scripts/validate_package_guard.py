#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT_DIR = ROOT / "current"
SOURCE_DIR = CURRENT_DIR / "source_files"
MANIFEST_PATH = CURRENT_DIR / "package_manifest/package_manifest.json"
REQUIRED_ACTIVE_SOURCES = ["delegation_access_policy.md", "autonomous_workflow_router.md"]
FORBIDDEN_VERSION_MARKERS = (
    "corrected_",
    "final_",
    "draft_",
    "v2_",
    "backup_",
    "old_",
    "superseded",
)
FORBIDDEN_ACTIVE_PATH_SEGMENTS = (
    "archive/",
    "deliveries/",
    "external_sources/",
    "tests/",
    ".github/",
    "scripts/",
)
PROTECTED_FILES = [
    CURRENT_DIR / "instructions/Instructions.md",
    CURRENT_DIR / "package_manifest/package_manifest.json",
    CURRENT_DIR / "source_files/delegation_access_policy.md",
    CURRENT_DIR / "source_files/autonomous_workflow_router.md",
    ROOT / ".github/workflows/package_guard.yml",
    ROOT / "scripts/validate_package_guard.py",
]


def fail(msg: str) -> int:
    print(f"FAIL: {msg}")
    return 1


def assert_exists(path: Path, label: str) -> str | None:
    if not path.exists():
        return f"{label} missing: {path.relative_to(ROOT)}"
    return None


def main() -> int:
    if not MANIFEST_PATH.exists():
        return fail("Missing manifest file")

    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return fail(f"Invalid manifest JSON: {exc}")

    if manifest.get("active_source_of_truth") != "current/":
        return fail("active_source_of_truth must be 'current/'")

    non_active = manifest.get("non_active_folders")
    if not isinstance(non_active, dict):
        return fail("non_active_folders must be an object")
    if "current/" in non_active:
        return fail("inactive folders must not promote current/ as inactive")

    instruction_file = manifest.get("instruction_file")
    if not isinstance(instruction_file, str) or not instruction_file:
        return fail("instruction_file must be a non-empty string")
    instruction_path = ROOT / instruction_file
    if not instruction_path.exists():
        return fail(f"instruction_file does not exist: {instruction_file}")
    instruction_text = instruction_path.read_text(encoding="utf-8")
    instruction_len = len(instruction_text)
    if instruction_len > 8000:
        return fail("current/instructions/Instructions.md exceeds 8000 characters")
    if instruction_len > 7800:
        print("WARN: current/instructions/Instructions.md exceeds 7800 characters")

    active_files = manifest.get("active_source_files")
    if not isinstance(active_files, list) or not active_files:
        return fail("active_source_files must be a non-empty list")

    for required in REQUIRED_ACTIVE_SOURCES:
        if required not in active_files:
            return fail(f"{required} must be listed in active_source_files")

    for item in active_files:
        if not isinstance(item, str) or not item:
            return fail("active_source_files entries must be non-empty strings")
        p = Path(item)
        if p.name != item:
            return fail(f"active_source_files must contain filenames only: {item}")
        if "/" in item or "\\" in item:
            return fail(f"active_source_files must contain filenames only, not paths: {item}")
        for forbidden_segment in FORBIDDEN_ACTIVE_PATH_SEGMENTS:
            if forbidden_segment in item:
                return fail(f"active_source_files entry must not target restricted paths: {item}")
        for marker in FORBIDDEN_VERSION_MARKERS:
            if marker in item.lower():
                return fail(f"active_source_files contains forbidden version marker '{marker}': {item}")
        if p.is_absolute() or ".." in p.parts:
            return fail(f"active source file points outside source folder: {item}")
        resolved = (SOURCE_DIR / item).resolve()
        try:
            resolved.relative_to(SOURCE_DIR.resolve())
        except ValueError:
            return fail(f"active source file escapes current/source_files/: {item}")
        if not resolved.exists():
            return fail(f"active source file missing under current/source_files/: {item}")

    for protected in PROTECTED_FILES:
        err = assert_exists(protected, "Protected file")
        if err:
            return fail(err)

    delegation_policy_text = (SOURCE_DIR / "delegation_access_policy.md").read_text(encoding="utf-8")
    if "Low-risk auto-merge gate" in delegation_policy_text:
        return fail(
            'delegation_access_policy.md contains deprecated phrase "Low-risk auto-merge gate"'
        )
    if "Admin/security evidence rule" not in delegation_policy_text:
        return fail('delegation_access_policy.md missing required section: "Admin/security evidence rule"')

    testing_protocol_text = (SOURCE_DIR / "testing_protocol.md").read_text(encoding="utf-8")
    if "Evidence-grade test" not in testing_protocol_text:
        return fail('testing_protocol.md missing required section: "Evidence-grade test"')

    old_delivery_phrase = "provide complete revised current files and ZIP unless user requested audit-only/no-files/chat-only"
    if old_delivery_phrase in testing_protocol_text:
        return fail("testing_protocol.md contains deprecated Delivery test phrase requiring only manual files/ZIP delivery")
    if "audited Draft PR for authorized repository workflows" not in testing_protocol_text:
        return fail('testing_protocol.md missing required phrase: "audited Draft PR for authorized repository workflows"')


    registry_text = (SOURCE_DIR / "protected_behavior_registry.md").read_text(encoding="utf-8")
    required_pb_ids = ["PB-00", "PB-00A", "PB-00B"] + [f"PB-{n:02d}" for n in range(1, 38)]
    for pb_id in required_pb_ids:
        if pb_id not in registry_text:
            return fail(f"protected_behavior_registry.md missing required ID: {pb_id}")

    required_registry_phrases = [
        "User-work minimization",
        "Repository-first delivery",
    ]
    for phrase in required_registry_phrases:
        if phrase not in registry_text:
            return fail(f'protected_behavior_registry.md missing required phrase: "{phrase}"')

    required_kernel_phrases = [
        "Patch Lock",
        "Patch State Machine",
        "Builder/Auditor split",
        "Current package truth",
        "Right-sized architecture",
        "Child-system inheritance",
        "Final gate",
    ]
    for phrase in required_kernel_phrases:
        if phrase not in instruction_text:
            return fail(f'current/instructions/Instructions.md missing required phrase: "{phrase}"')

    router_text = (SOURCE_DIR / "autonomous_workflow_router.md").read_text(encoding="utf-8").lower()
    if "verification fallback" not in router_text:
        return fail('autonomous_workflow_router.md missing required section: "Verification fallback"')
    for trigger in ["ready", "check", "done", "готово", "проверь"]:
        if trigger not in router_text:
            return fail(
                "autonomous_workflow_router.md missing PR verification trigger "
                f'for "{trigger}"'
            )
    required_repository_first_sections = [
        ("delivery_protocol.md", "Repository-first delivery rule"),
        ("project_operating_protocol.md", "repository-first workflow rule"),
        ("testing_protocol.md", "Repository-first delivery test"),
    ]

    required_user_work_sections = [
        ("autonomous_workflow_router.md", "User-work minimization rule"),
        ("autonomous_workflow_router.md", "Source-state verification rule"),
        ("delegation_access_policy.md", "User-work minimization authority rule"),
        ("testing_protocol.md", "User-work minimization test"),
    ]
    section_texts = {
        "autonomous_workflow_router.md": (SOURCE_DIR / "autonomous_workflow_router.md").read_text(encoding="utf-8"),
        "delegation_access_policy.md": delegation_policy_text,
        "delivery_protocol.md": (SOURCE_DIR / "delivery_protocol.md").read_text(encoding="utf-8"),
        "project_operating_protocol.md": (SOURCE_DIR / "project_operating_protocol.md").read_text(encoding="utf-8"),
        "testing_protocol.md": testing_protocol_text,
    }
    for file_name, phrase in required_user_work_sections:
        if phrase not in section_texts[file_name]:
            return fail(f'{file_name} missing required section: "{phrase}"')

    for file_name, phrase in required_repository_first_sections:
        if phrase not in section_texts[file_name]:
            return fail(f'{file_name} missing required section: "{phrase}"')


    new_gate_phrases = [
        ("autonomous_workflow_router.md", "Execution substrate selection rule"),
        ("autonomous_workflow_router.md", "Execution failover rule"),
        ("autonomous_workflow_router.md", "Verification target lock rule"),
        ("autonomous_workflow_router.md", "Plan/state separation rule"),
        ("autonomous_workflow_router.md", "Completion ledger rule"),
        ("delegation_access_policy.md", "Evidence claim gate"),
        ("delegation_access_policy.md", "Rational route gate"),
        ("delegation_access_policy.md", "Delegation failure reframe rule"),
    ]
    for file_name, phrase in new_gate_phrases:
        if phrase not in section_texts[file_name]:
            return fail(f'{file_name} missing required section: "{phrase}"')

    for phrase in ["candidate pr", "do not spend time converting it to draft", "read-only audit"]:
        if phrase not in router_text:
            return fail(
                "autonomous_workflow_router.md missing required PR-state fallback phrase "
                f'"{phrase}"'
            )

    print("PASS: package guard validation succeeded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
