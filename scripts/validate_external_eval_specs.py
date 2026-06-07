#!/usr/bin/env python3
"""Validate repo-only external eval/red-team specifications.

This validator intentionally avoids external runtime dependencies. It checks that
external eval specifications exist, are repo-only/evidence-layer scoped, map
assertions to protected behavior or regression test IDs, and do not claim ChatGPT
Project runtime activation.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    ROOT / "evals/promptfoo/project_designer_redteam.yaml",
    ROOT / "evals/promptfoo/assertions/project_designer_assertions.yaml",
    ROOT / "evals/security/prompt_injection_cases.md",
    ROOT / "reports/templates/release_report_template.md",
    ROOT / "reports/observability_ledger.md",
]

REQUIRED_MARKERS = {
    "evals/promptfoo/project_designer_redteam.yaml": [
        "repo-only",
        "external eval",
        "runtime activation",
        "Artifact Destination Contract",
        "PB-56",
        "PB-59",
        "T28",
    ],
    "evals/promptfoo/assertions/project_designer_assertions.yaml": [
        "assertions",
        "PB-56",
        "PB-57",
        "PB-58",
        "PB-59",
        "T28",
        "T32",
    ],
    "evals/security/prompt_injection_cases.md": [
        "prompt injection",
        "lower-authority",
        "source file",
        "T17",
        "PB-57",
    ],
    "reports/templates/release_report_template.md": [
        "Release ID",
        "Manifest status",
        "External evals",
        "Runtime activation status",
        "Stable promotion verdict",
    ],
    "reports/observability_ledger.md": [
        "Evidence layer",
        "Observed behavior",
        "Runtime",
        "Rollback needed",
    ],
}

FORBIDDEN_CLAIMS = [
    "external eval pass means runtime active",
    "promptfoo pass means runtime active",
    "scanner overrides safety",
    "upload evals as knowledge",
]

ID_RE = re.compile(r"\b(PB-(?:00A|00B|\d{2})|T\d{2})\b")


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def main() -> int:
    for path in REQUIRED_FILES:
        if not path.exists():
            return fail(f"Missing required external-eval/report file: {path.relative_to(ROOT)}")
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            return fail(f"Required external-eval/report file is empty: {path.relative_to(ROOT)}")
        rel = path.relative_to(ROOT).as_posix()
        for marker in REQUIRED_MARKERS[rel]:
            if marker not in text:
                return fail(f"{rel} missing required marker: {marker}")
        lowered = text.lower()
        for claim in FORBIDDEN_CLAIMS:
            if claim in lowered:
                return fail(f"{rel} contains forbidden claim: {claim}")
        if rel.startswith("evals/"):
            ids = set(ID_RE.findall(text))
            if not ids:
                return fail(f"{rel} must map checks to PB-* or T* IDs")

    manifest_text = (ROOT / "current/package_manifest/package_manifest.json").read_text(encoding="utf-8")
    for marker in ["evals/", "reports/", "external_eval_layers", "release_gates"]:
        if marker not in manifest_text:
            return fail(f"Manifest missing external eval/report marker: {marker}")

    print("PASS: external eval specs and report templates are present, mapped, and repo-only scoped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
