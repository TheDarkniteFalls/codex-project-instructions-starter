# Codex Project Instructions Starter

Copyable project instructions for teams using Codex-style coding agents.

The templates are intentionally small. They help a repo say what the agent may
touch, what must stay private, which checks matter, and how to hand work off to
a human reviewer.

## Why It Exists

Agent-assisted work gets better when the project is explicit about boundaries:
scope, public/private rules, evidence, checks, and handoff shape.

This starter turns those rules into files a visitor can copy into a repo before
asking an agent to work there.

## Files

- `AGENTS.template.md`: project-local instructions for coding agents.
- `PUBLIC_BOUNDARIES.md`: what belongs in public work and what stays private.
- `HANDOFF_TEMPLATE.md`: a compact handoff shape for another agent or reviewer.
- `CHECKS.md`: a minimal checklist for proving a change is ready.

## Use

Copy the templates into a project and rename `AGENTS.template.md` to
`AGENTS.md`.

```sh
python3 check_templates.py
```

Expected result:

```text
PASS templates
```

## How These Fit Together

This repo is one piece of a small public toolkit:

- [Public Repo Safety Kit](https://github.com/TheDarkniteFalls/public-repo-safety-kit)
  checks a public-candidate repo before publishing.
- [EvidenceGate](https://github.com/TheDarkniteFalls/evidencegate) records the
  evidence and checks behind an AI-assisted change.
- [Local Model Reliability Example](https://github.com/TheDarkniteFalls/local-model-reliability-example)
  validates structured model output and protected-path boundaries before
  trusting it.
- [Context Boundary Examples](https://github.com/TheDarkniteFalls/context-boundary-examples)
  checks whether an answer stays inside supplied evidence.
- [Green-Spine QA Pattern](https://github.com/TheDarkniteFalls/green-spine-qa-pattern)
  bundles the important path behind one repeatable command.
- Codex Project Instructions Starter gives the agent clear project rules before
  any of those checks run.

## Public Data Notice

These templates are generic. Do not add private project notes, credentials,
connector exports, raw logs, personal context, or internal URLs.

## Quality Checks

```sh
python3 check_templates.py
python3 -m py_compile check_templates.py
```
