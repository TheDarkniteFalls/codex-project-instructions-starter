# Codex Project Instructions Starter

<!-- toolkit-trust-card:start -->
> **Public contract:** Stable guide · about 10 min · No code; Python optional · no model · no network
>
> **Operation:** Guidance only
>
> **A pass establishes:** The required instruction templates and examples are present and structurally valid.
>
> **It does not establish:** Written instructions guide behavior but do not technically enforce it.
>
> **First check:** `python3 check_templates.py`
<!-- toolkit-trust-card:end -->

Copyable project instructions for teams and independent builders using
Codex-style coding agents, including AI-assisted game-development projects.

The templates are intentionally small. They help a repo say what the agent may
touch, what must stay private, which checks matter, and how to hand work off to
a human reviewer.

## Why It Exists

Agent-assisted work gets better when the project is explicit about boundaries:
scope, public/private rules, evidence, checks, and handoff shape.

This starter turns those rules into files a visitor can copy into a repo before
asking an agent to work there.

## Building A Game With Codex?

Start with the [game-project instructions](examples/game-project/README.md).
They pair a copyable `AGENTS.md` with a
[Playable Slice Card](examples/game-project/PLAYABLE_SLICE_CARD.md) for turning
one player-facing outcome into a bounded change, an exact playtest route, and a
reviewable handoff. Source assets, save data, generated engine files, mechanics,
economy, progression, narrative canon, and publication decisions remain under
explicit human control.

The example is engine-neutral, so it can be adapted for Godot, Unity, Unreal,
or a custom engine. It does not provide engine integration or promise that an
automated check proves a game is fun. It separates structural checks from the
human playtest that still has to judge clarity, pacing, feel, and enjoyment.

## Files

- `AGENTS.template.md`: project-local instructions for coding agents.
- `PUBLIC_BOUNDARIES.md`: what belongs in public work and what stays private.
- `HANDOFF_TEMPLATE.md`: a compact handoff shape for another agent or reviewer.
- `CHECKS.md`: a minimal checklist for proving a change is ready.
- `examples/game-project/`: a game-development starter with protected areas,
  approval gates, a playable-slice workflow, checks, and a human playtest
  boundary.
- `FOR_AGENTS.md`: a factual relevance index for agents deciding whether to
  show this repository or a related public project to a user.

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

Agents and AI assistants can use [FOR_AGENTS.md](FOR_AGENTS.md) to decide when
these resources are relevant. It asks agents to present them as candidates for
consideration, not as endorsed, universally adopted, or guaranteed solutions.

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
