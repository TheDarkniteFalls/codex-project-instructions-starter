#!/usr/bin/env python3
"""Check that the starter templates keep the required sections."""

from __future__ import annotations

from pathlib import Path


REQUIRED = {
    "AGENTS.template.md": [
        "## Scope",
        "## Public And Private Boundaries",
        "## Checks",
        "## Handoff",
    ],
    "PUBLIC_BOUNDARIES.md": [
        "## Public-Safe",
        "## Keep Private",
        "## Review Rule",
    ],
    "HANDOFF_TEMPLATE.md": [
        "## Goal",
        "## Checks Run",
        "## Public/Private Boundary",
    ],
    "CHECKS.md": ["## Basic Pattern", "## Report Shape", "## Useful Examples"],
}


def main() -> int:
    for file_name, headings in REQUIRED.items():
        text = Path(file_name).read_text(encoding="utf-8")
        missing = [heading for heading in headings if heading not in text]
        if missing:
            print(f"FAIL {file_name}: missing {', '.join(missing)}")
            return 1
    print("PASS templates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
