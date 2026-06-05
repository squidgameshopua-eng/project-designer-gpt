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
    ROOT / ".github/workflows/build_knowledge_package.yml",
    ROOT / "scripts/validate_package_guard.py",
    ROOT / "scripts/build_knowledge_package.py",
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
    required_pb_ids = ["PB-00", "PB-00A", "PB-00B"] + [f"PB-{n:02d}" for n in range(1, 51)]
    for pb_id in required_pb_ids:
        if pb_id not in registry_text:
            return fail(f"protected_behavior_registry.md missing required ID: {pb_id}")

    required_registry_phrases = [
        "User-work minimization",
        "Repository-first delivery",
        "Cost/Capability Gate",
        "Free-Route Fallback",
        "Source Safety / No Secrets Gate",
        "Audit-only Before Patch Gate",
        "GitHub Instruction/Knowledge Delivery Format",
        "User-Facing Russian Output Gate",
        "Minimal User Action / Action Compression Gate",
        "Target Placement and Result Lock",
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

    explicit_gate_names = [
        "Durable Ledger",
        "State Reconciliation",
        "Completion Ledger",
        "Activation Semantics",
        "Plan/State Separation",
    ]
    for gate_name in explicit_gate_names:
        if gate_name not in instruction_text:
            return fail(f'current/instructions/Instructions.md missing explicit gate name: "{gate_name}"')
    forbidden_grouped_gate_names = [
        "Ledger/Reconciliation/Completion",
        "Activation/Plan-State",
    ]
    for grouped_name in forbidden_grouped_gate_names:
        if grouped_name in instruction_text:
            return fail(f'current/instructions/Instructions.md uses compressed grouped gate name: "{grouped_name}"')
    final_gate_line = next((line for line in instruction_text.splitlines() if line.startswith("Final gate:")), "")
    kernel_line = next((line for line in instruction_text.splitlines() if line.startswith("Kernel self-preservation:")), "")
    if not final_gate_line:
        return fail("current/instructions/Instructions.md missing Final gate line")
    if not kernel_line:
        return fail("current/instructions/Instructions.md missing Kernel self-preservation line")
    for gate_name in explicit_gate_names:
        if gate_name not in final_gate_line:
            return fail(f'Final gate missing explicit gate name: "{gate_name}"')
        if gate_name not in kernel_line:
            return fail(f'Kernel self-preservation missing explicit gate name: "{gate_name}"')

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
        "package_state_protocol.md": (SOURCE_DIR / "package_state_protocol.md").read_text(encoding="utf-8"),
        "output_templates.md": (SOURCE_DIR / "output_templates.md").read_text(encoding="utf-8"),
        "protected_behavior_registry.md": registry_text,
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


    required_missing_gate_phrases = [
        ("autonomous_workflow_router.md", "Cost/Capability Gate"),
        ("autonomous_workflow_router.md", "Free-Route Fallback"),
        ("autonomous_workflow_router.md", "Audit-only Before Patch Gate"),
        ("delegation_access_policy.md", "Cost/capability delegation gate"),
        ("delegation_access_policy.md", "Free-route fallback delegation rule"),
        ("delegation_access_policy.md", "No secrets delegation rule"),
        ("delegation_access_policy.md", "Audit-only delegation rule"),
        ("delivery_protocol.md", "Cost/capability delivery rule"),
        ("delivery_protocol.md", "Free-route delivery fallback"),
        ("delivery_protocol.md", "Audit-only delivery blocker"),
        ("source_safety_policy.md", "No-secrets source safety gate"),
        ("source_safety_policy.md", "Secrets/settings audit rule"),
        ("testing_protocol.md", "Cost/Capability Gate test"),
        ("testing_protocol.md", "Free-Route Fallback test"),
        ("testing_protocol.md", "Source Safety / No Secrets Gate test"),
        ("testing_protocol.md", "Audit-only Before Patch Gate test"),
        ("output_templates.md", "Secrets/settings audit template"),
    ]
    section_texts["source_safety_policy.md"] = (SOURCE_DIR / "source_safety_policy.md").read_text(encoding="utf-8")
    for file_name, phrase in required_missing_gate_phrases:
        if phrase not in section_texts[file_name]:
            return fail(f'{file_name} missing required PB-38..PB-41 phrase: "{phrase}"')

    for phrase in ["candidate pr", "do not spend time converting it to draft", "read-only audit"]:
        if phrase not in router_text:
            return fail(
                "autonomous_workflow_router.md missing required PR-state fallback phrase "
                f'"{phrase}"'
            )

    required_operation_watchdog_phrases = [
        ("protected_behavior_registry.md", "PB-42"),
        ("protected_behavior_registry.md", "PB-43"),
        ("protected_behavior_registry.md", "PB-44"),
        ("protected_behavior_registry.md", "PB-45"),
        ("protected_behavior_registry.md", "PB-46"),
        ("autonomous_workflow_router.md", "Operation Watchdog"),
        ("autonomous_workflow_router.md", "Atomic Write Limit"),
        ("autonomous_workflow_router.md", "Checkpoint Before Mutation"),
        ("autonomous_workflow_router.md", "Failed Write Fallback"),
        ("autonomous_workflow_router.md", "No Silent Long Task"),
        ("autonomous_workflow_router.md", "Operation Checkpoint"),
        ("testing_protocol.md", "Silent hang test"),
        ("testing_protocol.md", "Repeated route failure test"),
        ("testing_protocol.md", "Atomic write test"),
        ("testing_protocol.md", "Checkpoint before mutation test"),
        ("delivery_protocol.md", "No Silent Delivery Rule"),
        ("package_state_protocol.md", "Operation State"),
        ("delegation_access_policy.md", "Failed write delegation rule"),
    ]
    for file_name, phrase in required_operation_watchdog_phrases:
        if phrase not in section_texts[file_name]:
            return fail(f'{file_name} missing required Operation Watchdog phrase: "{phrase}"')

    required_pb48_pb49_pb50_phrases = [
        ("protected_behavior_registry.md", "PB-48 User-Facing Russian Output Gate"),
        ("protected_behavior_registry.md", "PB-49 Minimal User Action / Action Compression Gate"),
        ("protected_behavior_registry.md", "PB-50 Target Placement and Result Lock"),
        ("current/instructions/Instructions.md", "User-Facing Russian Output"),
        ("current/instructions/Instructions.md", "Minimal User Action"),
        ("current/instructions/Instructions.md", "Target Placement and Result Lock"),
        ("autonomous_workflow_router.md", "Minimal User Action / Action Compression rule"),
        ("autonomous_workflow_router.md", "User-Facing Russian Output routing rule"),
        ("autonomous_workflow_router.md", "Target Placement and Result Lock rule"),
        ("delegation_access_policy.md", "Minimal User Action / Action Compression authority rule"),
        ("delegation_access_policy.md", "User-Facing Russian Output delegation rule"),
        ("delegation_access_policy.md", "Target Placement and Result Lock delegation rule"),
        ("testing_protocol.md", "PB-48 User-Facing Russian Output Gate tests"),
        ("testing_protocol.md", "PB-49 Minimal User Action / Action Compression tests"),
        ("testing_protocol.md", "PB-50 Target Placement and Result Lock tests"),
        ("testing_protocol.md", "Russian user-facing output test"),
        ("testing_protocol.md", "Minimal user action test"),
        ("testing_protocol.md", "Target placement test"),
        ("output_templates.md", "PB-48 User-facing Russian output template"),
        ("output_templates.md", "PB-49 Minimal User Action / Action Compression template"),
        ("output_templates.md", "PB-50 Target Placement and Result Lock template"),
        ("output_templates.md", "User-facing language: Russian"),
        ("output_templates.md", "User actions required per route"),
        ("output_templates.md", "Exact target object to modify"),
    ]
    section_texts["current/instructions/Instructions.md"] = instruction_text
    for file_name, phrase in required_pb48_pb49_pb50_phrases:
        if phrase not in section_texts[file_name]:
            return fail(f'{file_name} missing required PB-48/PB-49/PB-50 phrase: "{phrase}"')

    kernel_line_exact = next((line for line in instruction_text.splitlines() if line.startswith("Kernel self-preservation:")), "")
    final_gate_line_exact = next((line for line in instruction_text.splitlines() if line.startswith("Final gate:")), "")
    for phrase in ["User-Facing Russian Output", "Minimal User Action", "Target Placement and Result Lock"]:
        if phrase not in kernel_line_exact:
            return fail(f'Kernel self-preservation missing PB-48/PB-49/PB-50 phrase: "{phrase}"')
        if phrase not in final_gate_line_exact:
            return fail(f'Final gate missing PB-48/PB-49/PB-50 phrase: "{phrase}"')

    required_pb47_phrases = [
        ("protected_behavior_registry.md", "PB-47"),
        ("protected_behavior_registry.md", "GitHub Instruction/Knowledge Delivery Format"),
        ("delivery_protocol.md", "PB-47 GitHub Instruction/Knowledge Delivery Format"),
        ("delivery_protocol.md", "scripts/build_knowledge_package.py"),
        ("delivery_protocol.md", "Knowledge/"),
        ("output_templates.md", "PB-47 GitHub Instruction/Knowledge delivery template"),
        ("testing_protocol.md", "PB-47 GitHub Instruction/Knowledge Delivery Format tests"),
        ("testing_protocol.md", "Build Knowledge Package test"),
    ]
    for file_name, phrase in required_pb47_phrases:
        if phrase not in section_texts[file_name]:
            return fail(f'{file_name} missing required PB-47 phrase: "{phrase}"')

    build_script = ROOT / "scripts/build_knowledge_package.py"
    build_workflow = ROOT / ".github/workflows/build_knowledge_package.yml"
    build_script_text = build_script.read_text(encoding="utf-8")
    build_workflow_text = build_workflow.read_text(encoding="utf-8")
    for phrase in ["Instructions.md", "Knowledge/", "UPLOAD_GUIDE.md", "package_manifest.json", "active_source_files"]:
        if phrase not in build_script_text:
            return fail(f'scripts/build_knowledge_package.py missing required PB-47 phrase: "{phrase}"')
    if "python scripts/build_knowledge_package.py --output" not in build_workflow_text:
        return fail("build_knowledge_package.yml missing package build command")

    print("PASS: package guard validation succeeded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
