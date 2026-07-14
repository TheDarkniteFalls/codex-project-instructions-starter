# Game Project Instructions

Template: replace every `[BRACKETED VALUE]` before relying on this file. Keep
only rules that match the real repository.

## Project North Star

- Game: `[PROJECT NAME]`
- Engine and version: `[ENGINE AND VERSION]`
- Intended player experience: `[ONE SENTENCE PLAYER EXPERIENCE]`
- Current milestone: `[MILESTONE OR PLAYABLE SLICE]`

Preserve the intended player experience when making technical changes. If a
request would materially change it, stop and ask for a human design decision.

## Sources Of Truth

- Game design: `[PATH TO GAME DESIGN OR PROJECT CARD]`
- Mechanics and balance: `[PATH TO MECHANICS OR BALANCE DATA]`
- Narrative canon: `[PATH TO CANON OR NARRATIVE DATA]`
- Current roadmap: `[PATH TO ROADMAP OR TASK SOURCE]`
- Engine project settings: `[PATH TO ENGINE PROJECT FILES]`

Inspect the relevant source-of-truth files before proposing or making changes.
Do not treat an old chat, generated artifact, or engine cache as authoritative.

## Scope And Working Style

- Start from the current repository and working-tree state.
- Keep each change focused on the requested player or builder outcome.
- Prefer the smallest playable vertical slice over broad speculative systems.
- Preserve unrelated code, scenes, assets, data, documentation, and history.
- Do not silently regenerate the whole project to solve a local problem.
- Explain the visible player impact before low-level implementation detail.

## Protected Areas

- Do not edit source art, source audio, licensed assets, localisation masters,
  or narrative source files unless the request explicitly includes them.
- Do not edit engine-generated or imported files such as `.godot/`, `Library/`,
  `Temp/`, `Intermediate/`, `Saved/`, or other project-specific generated
  folders. Update their real source instead.
- Do not modify real player saves. Use synthetic fixtures or copied test saves.
- Do not break the save format without an approved migration and rollback plan.
- Do not replace package locks, engine versions, rendering pipelines, or major
  plugins merely to make a narrow change easier.
- Never add credentials, private data, unreleased source material, or
  unlicensed third-party assets.

Replace this section with the project's exact protected paths:

- `[PROTECTED PATH OR DATASET]`
- `[PROTECTED PATH OR DATASET]`

## Human Approval Gates

Ask before:

- changing core mechanics, economy, progression, difficulty, or narrative canon;
- introducing a new dependency, plugin, external service, or network call;
- changing save compatibility, telemetry, accounts, payments, or moderation;
- deleting or replacing assets, scenes, levels, migrations, or player data;
- downloading or generating third-party assets with unclear rights; or
- publishing, uploading a build, changing a store listing, or pushing remotely.

Approval for one named change does not grant reusable authority for a broader
change. If the target, payload, or scope changes materially, ask again.

## Checks

Replace these placeholders with exact commands that work in this repository:

- Fast focused check: `[EXACT COMMAND]`
- Project health check: `[EXACT COMMAND]`
- Build or headless engine check: `[EXACT COMMAND]`
- Representative human playtest: `[SCENE, LEVEL, ROUTE, OR SAVE FIXTURE]`

Run the smallest relevant automated check after a focused edit. Run the named
project health check when the main gameplay path, generated content, saves, or
shared systems change. Report checks that could not run and never invent a
passing result.

Automated success does not prove clarity, balance, pacing, feel, accessibility,
or fun. Leave those claims for the human playtest.

## Handoff

End substantial work with:

- the intended and actual player-facing change;
- files, scenes, assets, and data touched;
- automated checks run and their results;
- the human playtest route still required;
- save, performance, platform, licensing, or accessibility risks;
- anything uncertain or unproven; and
- the next best action.
