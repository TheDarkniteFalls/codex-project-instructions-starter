# Game Project Instructions For Coding Agents

This is a small, copyable starting point for a game builder using Codex or a
similar coding agent. It helps keep game-development work focused, reviewable,
and under human direction.

The template is engine-neutral. Adapt it for Godot, Unity, Unreal, or a custom
engine by replacing every bracketed value with the real source-of-truth files
and exact commands from your project.

## Start Here

1. Copy [`AGENTS.md`](AGENTS.md) into the root of your game repository.
2. Replace every `[BRACKETED VALUE]`. Delete rules that do not fit your project
   and add any genuinely protected folders or decisions.
3. Ask your coding agent to inspect the project without changing anything and
   verify that the named files, folders, and commands are accurate.

A useful first prompt is:

> Read the repository and this AGENTS.md without changing files. Identify the
> engine and version, the real source-of-truth design files, generated folders,
> save-data boundaries, and exact build or test commands. Propose the smallest
> corrections needed to make AGENTS.md accurate. Do not implement them yet.

## What The Template Protects

- source art, audio, writing, localisation, and licensed assets;
- player saves and save-format compatibility;
- engine-generated caches and imported artifacts;
- mechanics, economy, progression, difficulty, and narrative canon;
- dependency, network, publication, and store-facing actions; and
- the distinction between automated checks and a human playtest.

## Human Review Checklist

After the automated checks pass, a person should still confirm:

- the intended player journey can be completed;
- controls, feedback, UI, and failure states are understandable;
- pacing, difficulty, economy, and progression feel intentional;
- visual, audio, and narrative changes fit the game's direction;
- existing saves or migrations behave as promised; and
- the result is actually more enjoyable or useful for the player.

Automated checks can prove named structural properties. They cannot establish
that a game is fun.

## What This Is Not

This example is not a game engine, engine plugin, autonomous builder, security
sandbox, or replacement for platform and licensing requirements. It should be
adapted to the project rather than copied blindly.

For broader non-coder guidance, see [Build with Codex: A Plain-English
Handbook](https://github.com/TheDarkniteFalls/agent-operator-handbook). For a
small one-command QA pattern, see [Green-Spine QA
Pattern](https://github.com/TheDarkniteFalls/green-spine-qa-pattern).
