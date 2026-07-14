# Playable Slice Card

Use this card for one change a player can notice and review. Ask the coding
agent to draft what it can from the current repository, then decide the player
outcome and any protected design choices yourself.

Keep the completed card short. If it grows into several journeys, mechanics, or
milestones, split it before implementation.

## Copyable Card

### Player Outcome

- **Player-visible change:** `[WHAT SHOULD THE PLAYER SEE, UNDERSTAND, OR DO?]`
- **Why it matters now:** `[PROBLEM OR MILESTONE THIS ADVANCES]`
- **Out of scope:** `[USEFUL WORK DELIBERATELY NOT INCLUDED]`

### Starting Point

- **Current behavior:** `[WHAT HAPPENS NOW?]`
- **Start from:** `[SCENE, LEVEL, ROUTE, OR SYNTHETIC SAVE FIXTURE]`
- **Reproduction steps:** `[SHORTEST RELIABLE STEPS]`
- **Recovery point:** `[BRANCH, COMMIT, BACKUP, OR RESTORABLE FILE SET]`

### Sources And Boundaries

- **Sources of truth:** `[DESIGN, MECHANICS, CANON, ROADMAP, OR ENGINE FILES]`
- **May change:** `[EXACT SYSTEMS, FILES, SCENES, OR DATA]`
- **Must not change:** `[MECHANICS, BALANCE, SAVES, ASSETS, CANON, OR OTHER NON-GOALS]`
- **Ask again before:** `[DECISIONS OR ACTIONS REQUIRING FRESH APPROVAL]`

### Acceptance

- **Observable success:** `[WHAT MUST HAPPEN FOR THE PLAYER?]`
- **Observable failure handling:** `[WHAT MUST HAPPEN WHEN THE PLAYER FAILS OR THE FEATURE IS UNAVAILABLE?]`
- **Focused automated check:** `[EXACT COMMAND OR NAMED TEST]`
- **Project health check:** `[EXACT COMMAND]`
- **Human playtest route:** `[EXACT START, ACTIONS, AND END STATE]`
- **Human questions:** `[ONE OR TWO SPECIFIC EXPERIENCE QUESTIONS]`
- **Evidence expected:** `[CHANGED-ITEM LIST, TEST OUTPUT, SCREENSHOT, VIDEO, OR BEFORE/AFTER]`
- **Still unproven after this slice:** `[KNOWN LIMITS]`

### Required Handoff

- **Intended and actual player result:**
- **Items changed:**
- **Checks and outcomes:**
- **What the checks do not prove:**
- **Human playtest still required:**
- **Save, performance, platform, licensing, or accessibility risk:**
- **Decision needed:** `[ACCEPT, REVISE, ROLL BACK, OR HOLD]`
- **Recommended next action:**

## Filled Synthetic Example

This example is fictional. It uses no private project details, real saves, or
third-party assets.

### Player Outcome

- **Player-visible change:** When the hero reaches critical health, the existing
  health display gains a clear warning state and the next hit explains the
  defeat before restart.
- **Why it matters now:** First-time players currently lose without recognizing
  that they were in immediate danger.
- **Out of scope:** Damage values, enemy behavior, difficulty, new art, audio,
  controller vibration, accessibility settings, and the restart rules.

### Starting Point

- **Current behavior:** Health reaches zero and the scene restarts, but the
  danger and defeat states use the same neutral presentation as normal play.
- **Start from:** Synthetic test scene `tests/fixtures/low_health_room` with the
  hero at two health and one stationary training hazard.
- **Reproduction steps:** Start the fixture, touch the hazard once, wait for its
  cooldown, then touch it again.
- **Recovery point:** Clean branch plus the original health-display scene and
  defeat-message script.

### Sources And Boundaries

- **Sources of truth:** The health-state enum, existing UI style tokens, defeat
  flow, and the current milestone card.
- **May change:** The health-display state binding, existing warning style, the
  defeat-message copy, and focused tests for those behaviors.
- **Must not change:** Health math, damage, hazard timing, restart behavior,
  saves, source art, sound, input, or game-wide difficulty.
- **Ask again before:** Adding assets, changing a mechanic, or expanding the
  warning into other scenes.

### Acceptance

- **Observable success:** At critical health, the existing display changes to
  the warning state without changing the health value.
- **Observable failure handling:** At zero health, the defeat message appears
  before the existing restart becomes available.
- **Focused automated check:** Run the named health-display state test.
- **Project health check:** Run the repository's existing green-spine command.
- **Human playtest route:** Complete the two-hit fixture once with keyboard and
  once with controller, observing critical health, defeat, and restart.
- **Human questions:** Was danger understandable before the final hit? Was the
  reason for defeat clear without reading debug output?
- **Evidence expected:** Before/after screenshots, changed-file list, focused
  test result, green-spine result, and the unmodified health values.
- **Still unproven after this slice:** Broader accessibility, localization,
  every display size, and whether the warning improves the full game.

### Example Implementation Prompt

```text
Read this completed slice and the current repository without editing first.
Confirm the observed starting behavior, exact files you expect to touch,
protected non-goals, recovery point, and checks. Then implement only the
critical-health and defeat-feedback slice. Do not change health math, damage,
difficulty, restart behavior, assets, saves, or input. Run the focused test and
the existing green-spine check after the final edit, then leave the two-hit
human playtest route and a plain-language evidence packet.
```
