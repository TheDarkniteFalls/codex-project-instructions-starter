# Checks

Run the smallest checks that prove the requested change.

## Basic Pattern

1. Check the working tree.
2. Run the focused command for the changed area.
3. Run the repo's named green-spine or health command if the change affects a
   main workflow.
4. Run a public/private boundary review before publishing.

## Report Shape

- Checks passed:
- Checks failed:
- Checks not run:
- Remaining risk:

## Useful Examples

- Documentation-only change: markdown review plus public/private scan.
- Python script: self-test plus `py_compile`.
- Browser-facing change: structural DOM or browser QA check.
- Agent-assisted change: receipt plus reviewer handoff.
