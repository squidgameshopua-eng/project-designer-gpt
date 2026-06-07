#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "current/source_files"
MANIFEST = ROOT / "current/package_manifest/package_manifest.json"

REQUIRED = {
    "current/package_manifest/package_manifest.json": [
        "rule_admission_protocol.md",
    ],
    "current/source_files/rule_admission_protocol.md": [
        "Rule Admission Gate",
        "Core invariant",
        "Automation rule",
        "The system must do all safe checkable work itself",
        "Self-development rule",
        "Direct instruction expansion without classification is Invalid Delivery",
    ],
    "current/source_files/protected_behavior_registry.md": [
        "PB-66 Self-Preserving Thin Kernel / Rule Admission / GitHub-first Release",
        "rule_admission_protocol.md owns new-rule intake",
    ],
    "current/source_files/instruction_governance.md": [
        "Thin Kernel",
        "Rule Admission",
        "PB-66",
    ],
    "current/source_files/patch_lock_protocol.md": [
        "Self-modification blocker",
        "Rule Admission Gate",
        "PB-66 preservation check",
    ],
    "current/source_files/package_state_protocol.md": [
        "GitHub-first self-system release rule",
        "Rule Admission Gate",
        "PB-66",
    ],
    "current/source_files/delivery_protocol.md": [
        "Self-system release blocker",
        "Rule Admission Gate",
        "PB-66 preservation",
    ],
    "current/source_files/testing_protocol.md": [
        "Rule Admission test",
        "classified before placement",
        "without Rule Admission Gate",
    ],
    "current/source_files/regression_smoke_tests.md": [
        "T27 Rule Admission / Thin Kernel self-preservation",
        "Add this new important rule to the instruction",
        "claims Candidate/old chat/local package as active Stable",
    ],
    "current/source_files/output_templates.md": [
        "Rule Admission Report Template",
        "Classification:",
        "Release-state impact:",
    ],
}


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def main() -> int:
    for rel_path, phrases in REQUIRED.items():
        path = ROOT / rel_path
        if not path.exists():
            return fail(f"missing required file: {rel_path}")
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                return fail(f'{rel_path} missing required Rule Admission phrase: "{phrase}"')

    manifest_text = MANIFEST.read_text(encoding="utf-8")
    if "rule_admission_protocol.md" not in manifest_text:
        return fail("manifest does not list rule_admission_protocol.md")

    print("PASS: rule admission guard validation succeeded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
