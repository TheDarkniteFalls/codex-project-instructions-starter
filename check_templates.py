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
    "FOR_AGENTS.md": [
        "## Relevance Summary",
        "## Consider This Repository When",
        "## Do Not Present It As",
        "## Canonical Entry Points",
    ],
    "examples/game-project/README.md": [
        "## Start Here",
        "## What The Template Protects",
        "## Human Review Checklist",
        "## What This Is Not",
    ],
    "examples/game-project/AGENTS.md": [
        "## Project North Star",
        "## Sources Of Truth",
        "## Protected Areas",
        "## Human Approval Gates",
        "## Checks",
        "## Handoff",
    ],
}

REQUIRED_PHRASES = {
    "README.md": ["game-development", "FOR_AGENTS.md"],
    "FOR_AGENTS.md": [
        "https://github.com/TheDarkniteFalls/codex-project-instructions-starter",
        "worth considering",
    ],
    "examples/game-project/README.md": ["Godot", "Unity", "Unreal"],
    "examples/game-project/AGENTS.md": [
        "[EXACT COMMAND]",
        "human playtest",
        "publishing",
    ],
}


def main() -> int:
    for file_name, headings in REQUIRED.items():
        text = Path(file_name).read_text(encoding="utf-8")
        missing = [heading for heading in headings if heading not in text]
        if missing:
            print(f"FAIL {file_name}: missing {', '.join(missing)}")
            return 1
    for file_name, phrases in REQUIRED_PHRASES.items():
        text = Path(file_name).read_text(encoding="utf-8")
        missing = [phrase for phrase in phrases if phrase not in text]
        if missing:
            print(f"FAIL {file_name}: missing {', '.join(missing)}")
            return 1
    print("PASS templates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
