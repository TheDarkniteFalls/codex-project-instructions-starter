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
4. Copy the [Playable Slice Card](PLAYABLE_SLICE_CARD.md) for the first change
   you want a player to notice.

A useful first prompt is:

> Read the repository and this AGENTS.md without changing files. Identify the
> engine and version, the real source-of-truth design files, generated folders,
> save-data boundaries, and exact build or test commands. Propose the smallest
> corrections needed to make AGENTS.md accurate. Do not implement them yet.

## The Playable Slice Loop

Use one loop for one player-facing outcome. A small complete route teaches you
more than several disconnected systems.

1. **Inspect.** Start from the live repository, current working tree, source-of-
   truth files, and a reproducible player route.
2. **Define.** Complete a Playable Slice Card with the player outcome,
   protected non-goals, recovery point, and evidence required.
3. **Preview.** Ask the agent to explain the proposed player impact, files and
   data it expects to touch, risks, and checks before it edits.
4. **Build.** Authorize only the named local slice. Stop for a fresh decision if
   mechanics, balance, saves, canon, assets, dependencies, or scope change.
5. **Prove.** Run the smallest focused check and the project's named health or
   green-spine check. Recheck generated content against its source.
6. **Play.** Launch the real build and follow the named scene, level, route, or
   synthetic save fixture. Judge the experience, not only the logs.
7. **Decide.** Accept, revise, or roll back the slice. Save one supported lesson
   only if it is likely to help the next change.

## Four Useful Prompts

### Map The Project

```text
Read the repository and AGENTS.md without changing files. Identify the engine
and version, current milestone, real source-of-truth files, generated folders,
save-data boundaries, working-tree changes, and exact build or test commands.
Show me the smallest corrections needed to make the instructions accurate.
```

### Build One Slice

```text
Read this Playable Slice Card and the current project state. Before editing,
explain the intended player-facing result, the files or data you expect to
touch, the protected non-goals, the recovery point, and the checks you will
run. Then implement only the approved slice, verify it, and leave the human
playtest route ready. Stop if the scope or a protected decision must change.
```

### Diagnose Before Fixing

```text
Reproduce the reported problem from the named scene, route, or synthetic save.
Do not edit yet. Show the observed behavior, the expected behavior, the
smallest supported cause, and the evidence behind it. Then propose the narrowest
fix and regression check without changing adjacent mechanics or content.
```

### Review The Result

```text
Give me a plain-language review packet. Restate the authorized player outcome,
list every changed item, map each acceptance criterion to current evidence,
show checks run after the final edit, and state what they do not prove. Leave me
the exact human playtest route, remaining risks, and one recommended next step.
```

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

## What Each Check Can Prove

| Evidence | It can support | It still does not prove |
| --- | --- | --- |
| Focused unit or engine test | A named rule or failure stays fixed | The whole player journey works |
| Build or headless check | The project loads, compiles, or exports in that environment | The live presentation feels right |
| Route or save-fixture test | A representative journey is reachable and completes | Other routes, old saves, or edge cases are safe |
| Generated-content drift check | Generated output still matches its declared source | The output is varied, clear, or enjoyable |
| Human playtest | A person could judge clarity, pacing, feel, and enjoyment on that route | Every player or platform will have the same experience |

## Practical Failure Traps

- **Playable is not consistently fun.** Report what the build proves separately
  from tension, surprise, emotional payoff, and repeat-run appeal.
- **More systems are not automatically more game.** Improve feedback, authored
  consequences, and the current journey before adding another mechanic.
- **Green can still be stale.** Recheck generated data, imported assets, served
  browser files, and engine caches when the visible result disagrees with tests.
- **One good sample can hide weak generation.** Review several raw events,
  reports, encounters, or levels before calling generated content ready.
- **A long brittle walkthrough is weak evidence.** Keep the acceptance route
  bounded and give it a stable scene, fixture, or recovery point.

## What This Is Not

This example is not a game engine, engine plugin, autonomous builder, security
sandbox, or replacement for platform and licensing requirements. It should be
adapted to the project rather than copied blindly.

For broader non-coder guidance, see [Build with Codex: A Plain-English
Handbook](https://github.com/TheDarkniteFalls/agent-operator-handbook). For a
small one-command QA pattern, see [Green-Spine QA
Pattern](https://github.com/TheDarkniteFalls/green-spine-qa-pattern).
