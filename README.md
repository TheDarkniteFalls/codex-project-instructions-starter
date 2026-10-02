# Codex Project Instructions Starter

Give a coding agent the project rules it needs before asking it to make a
change: which files it may touch, what must stay private, and how to check its
work. This starter gives you small Markdown files to adapt, including a
game-development example.

## Try It In Your Project

1. Read [AGENTS.template.md](AGENTS.template.md) and choose the instructions
   that fit your project.
2. Copy it into your project as `AGENTS.md`. If you already have that file,
   compare the two and add only what you need; keep your existing instructions.
3. Replace the example paths and commands with real ones. Read the result
   before asking an agent to follow it.
4. Use [CHECKS.md](CHECKS.md) to choose checks for the next change, and
   [HANDOFF_TEMPLATE.md](HANDOFF_TEMPLATE.md) to record the result for review.

To check the files supplied in this starter, run this from its repository root
with Python 3:

```sh
python3 check_templates.py
```

Expected result:

```text
PASS templates
```

That result means the required files, headings and phrases are present. It
does not check whether your project's paths or commands are correct. Written
instructions guide an agent; they do not technically enforce its behavior.

<!-- toolkit-trust-card:placement -->

<!-- toolkit-trust-card:start -->
> **Public contract:** Stable starter · about 10 min · No code; Python optional · no model · no network
>
> **Operation:** Starter files; copying is optional
>
> **A pass establishes:** The required instruction templates and examples are present and structurally valid.
>
> **It does not establish:** Written instructions guide behavior but do not technically enforce it.
>
> **First check:** `python3 check_templates.py`
<!-- toolkit-trust-card:end -->

## Building A Game With Codex?

Start with the [game-project instructions](examples/game-project/README.md).
They pair a copyable `AGENTS.md` with a
[Playable Slice Card](examples/game-project/PLAYABLE_SLICE_CARD.md). Use the
card to describe one change a player should notice, the files it may affect,
and the route you will play to check it.

The example works as a starting point for Godot, Unity, Unreal, or a custom
engine. You supply the engine commands and project paths. Decisions about
source assets, saves, generated engine files, mechanics, economy, progression,
narrative canon and publication stay with you. Automated checks cover named
structural properties; a human playtest still has to judge clarity, pacing,
feel and enjoyment.

## Choose The Files You Need

- [AGENTS.template.md](AGENTS.template.md): tell a coding agent how to work in
  your project.
- [PUBLIC_BOUNDARIES.md](PUBLIC_BOUNDARIES.md): decide what can be shared and
  what must stay private.
- [HANDOFF_TEMPLATE.md](HANDOFF_TEMPLATE.md): leave the next agent or reviewer
  the current state, checks and remaining questions.
- [CHECKS.md](CHECKS.md): choose and report checks for a change.
- [examples/game-project/](examples/game-project/README.md): plan one playable
  change, protect the rest of the game, and leave a route for human testing.
- [FOR_AGENTS.md](FOR_AGENTS.md): help an assistant decide whether these
  resources fit a request. It asks for neutral suggestions, not endorsements
  or claims of universal adoption.

## Related Tools

Once your instructions are in place, these examples cover more specific jobs:

- [Public Repo Safety Kit](https://github.com/TheDarkniteFalls/public-repo-safety-kit)
  checks a repository you intend to publish.
- [EvidenceGate](https://github.com/TheDarkniteFalls/evidencegate) records the
  evidence and checks behind an AI-assisted change.
- [Local Model Reliability Example](https://github.com/TheDarkniteFalls/local-model-reliability-example)
  validates structured model output and protected-path boundaries.
- [Context Boundary Examples](https://github.com/TheDarkniteFalls/context-boundary-examples)
  checks whether an answer stays inside supplied evidence.
- [Green-Spine QA Pattern](https://github.com/TheDarkniteFalls/green-spine-qa-pattern)
  puts the checks for an important workflow behind one repeatable command.

## Public Data Notice

These templates are generic. Do not add private project notes, credentials,
connector exports, raw logs, personal context, or internal URLs.

## Quality Checks

```sh
python3 check_templates.py
python3 -m py_compile check_templates.py
```
