# Missile Defense Modernization Plan

## Goal
Modernize Missile Defense in `docs/index.html` so it feels more polished, replayable, and visually aligned with the shared Robrary brand while preserving the game's mechanically distinct identity, single-file delivery model, and deployability via GitHub Pages.

## Context and Constraints
- The game currently ships as a single self-contained document in `docs/index.html` with inline HTML, CSS, and JavaScript; the modernization must preserve this delivery pattern.
- Existing gameplay already includes core base-defense loops, limited ammo, city protection, wave progression, a normal/flak weapon toggle, splitter missiles, bombers, local leaderboard persistence, and keyboard shortcuts for pause/end game.
- The current UI partially overlaps the target direction, but it misses the Robrary-specific aesthetic details: it uses `Inter`/`Roboto` instead of `Courier New`, mixed-case labels, inconsistent overlay/button language, and a more generic grayscale sci-fi treatment.
- The menu and screen flow currently consist of start, wave-complete, and game-over overlays only. The plan should unify structure and copy with the other Jules games by standardizing the overlay hierarchy and command language.
- This repo includes lightweight Playwright-based verification scripts in `verification/verify_game.py` and `verification/verify_weapon.py`; build mode should extend or replace them with concrete checks that match the modernization work.
- The existing document contains several textual inconsistencies that implementation should address while modernizing, including the `Missle` typo in the title and hero heading.
- No bundler, package manifest, or automated lint/test workflow is currently present, so validation needs to rely on static checks plus browser automation that can run against a local static server.

## Assumptions
- "Shared Robrary brand aesthetic" means implementation should standardize on a Neon Noir presentation using grayscale as the dominant palette with a single restrained accent color used sparingly for emphasis, alerts, and focus states.
- "Keep the game mechanically distinct" means Missile Defense should stay centered on deliberate interception, ammo economy, and city/silo defense rather than being refactored into another Jules game pattern or simplified into a generic shooter.
- "Unify menu structure with the other Jules games" means matching terminology, visual hierarchy, and overlay affordances without requiring external shared assets or a multi-file component system.
- Because there is only one production file, implementation should prefer well-separated sections, small helper functions, and clear constants inside `docs/index.html` instead of adding new source files.
- If there is no canonical Robrary accent already stored in this repo, build mode should choose one subdued accent such as cyan, acid green, or amber and apply it consistently rather than introducing multiple competing highlight colors.
- Manual QA can assume a local static server such as `python3 -m http.server 8080` launched from the repository root.

## Deliverables
- A modernized `docs/index.html` that upgrades visual design, gameplay feedback, menu structure, and copy while remaining a single-file deployable game.
- Refined HUD and overlay language that consistently uses uppercase terminal-style labels and Robrary wording such as `INITIATE`, `DEPLOY`, `PAUSED`, `MISSION FAILED`, `REBOOT`, and `WAVE X` announcements.
- Gameplay improvements that add depth and readability without erasing current distinct mechanics such as dual weapon modes, city defense tension, and ammo management.
- Updated verification coverage in `verification/` that proves the modernized UI flow, critical controls, and key gameplay states still work after the refactor.
- Optional README touch-ups only if build mode finds the documentation materially misleading after implementation; this is lower priority than shipping and validating the single-file game.

## Todo Checklist
- [ ] Audit all current overlay copy, HUD labels, button text, and title strings in `docs/index.html` for Robrary brand alignment and typo fixes.
- [ ] Define a compact design token block in `docs/index.html` for Neon Noir colors, glass surfaces, borders, glows, typography, spacing, and motion timings.
- [ ] Replace the current font stack with a `Courier New`-led monospace stack and normalize uppercase terminal-style UI labels throughout menus and HUD.
- [ ] Rework the start, wave, pause, and game-over overlays into a unified menu system with shared layout, shared button treatment, and consistent command language.
- [ ] Introduce richer atmospheric visuals for the battlefield background, skyline, missile trails, explosions, and transitions while staying mostly grayscale plus one restrained accent.
- [ ] Improve HUD readability and terminology to show `SCORE`, `HI-SCORE`, `WAVE`, `LIVES`, and `AMMO`, and decide how `LIVES` maps to current silo/city survival data.
- [ ] Add distinct wave announcement and status messaging such as `WAVE X`, `PAUSED`, and `MISSION FAILED` that match Robrary presentation.
- [ ] Refine gameplay pacing and feedback loops so waves feel more dramatic and readable while preserving mechanical distinction from other Jules titles.
- [ ] Revisit weapon differentiation so `NORMAL` and `FLAK` remain understandable, valuable, and visually distinct under the new presentation.
- [ ] Ensure mobile and desktop layouts both remain playable, including canvas scaling, overlay fit, button tap targets, and readable HUD density.
- [ ] Update or expand Playwright verification scripts in `verification/` to cover start flow, HUD labels, pause overlay, wave messaging, weapon toggle behavior, and game-over/restart flow.
- [ ] Run concrete manual smoke checks against a local server and verify the page still deploys as a single `docs/index.html` GitHub Pages artifact.

## Implementation Plan
1. Establish the brand system inside `docs/index.html`.
   - Replace the current root CSS variables with a tighter token set for background layers, glass panels, border alpha, blur strength, accent glow, danger text, and hover-lift motion.
   - Update body and overlay styling to move from a generic flat dark background to a more intentional Neon Noir scene: layered gradients, subtle grid/noise feel, grayscale skyline atmosphere, and sparse accent glows.
   - Swap typography to a `Courier New`, Courier, monospace stack and enforce uppercase treatment for all navigational and HUD copy.

2. Unify information architecture and overlay language.
   - Refactor the start screen, wave-complete screen, pause state, and game-over screen into a shared overlay pattern with consistent card sizing, border treatment, blur, white edge highlight, and soft outer glow.
   - Standardize commands and labels to Robrary wording: e.g. start button `INITIATE` or `DEPLOY`, restart button `REBOOT`, failure heading `MISSION FAILED`, pause heading `PAUSED`, and wave interstitials `WAVE X` / `WAVE X COMPLETE`.
   - Preserve the leaderboard, but restyle it so it reads like a terminal ranking panel rather than a default list.
   - Correct the title/heading typo from `Missle Defense` to `Missile Defense` wherever it appears.

3. Modernize the HUD without breaking the single-file architecture.
   - Recompose the top HUD into a more compact terminal readout using uppercase labels and improved grouping.
   - Add an explicit `LIVES` readout. If city count and silo health are both important, either represent `LIVES` as active cities while exposing silo integrity separately, or rename one metric to avoid misleading players; implementation should choose the least confusing mapping and keep it consistent across HUD and overlays.
   - Restyle the weapon toggle as a hover-lift glass control with clearer affordance and a restrained accent pulse when `FLAK` is active.
   - Ensure HUD updates remain cheap and readable inside the main loop.

4. Improve gameplay feel while preserving mechanical distinctness.
   - Keep the defense/interception core, city-loss stakes, ammo pressure, flak tradeoff, wave progression, splitter missiles, and bomber threats.
   - Tune pacing using data constants rather than scattered literals: wave missile counts, spawn cadence, bomber probability, missile speeds, explosion radius, ammo refill rules, and score values.
   - Add enhancements that deepen identity without cloning other games, such as clearer telegraphing, more legible enemy class cues, stronger chain-reaction reward feedback, brief wave-start safe windows, or refined ammo economy between waves.
   - Make sure any new mechanic remains readable in the HUD/overlays and can be tested with deterministic enough criteria.

5. Upgrade visual feedback and animation.
   - Improve missile trails, explosion layering, particle behavior, screen shake restraint, and impact flashes so the battlefield feels premium but still performant in a single file.
   - Use accent color sparingly for state changes, active weapon mode, high-score celebration, and focus/hover states; keep the main playfield predominantly grayscale.
   - Replace the current canvas-drawn `PAUSED` text with a shared overlay or branded in-canvas treatment that matches the rest of the menu system.
   - Add concise wave announcement presentation that does not block play longer than necessary and remains legible on mobile.

6. Align structure with other Jules games while staying self-contained.
   - Consolidate repeated screen markup/CSS patterns so future Jules-style updates are easier to port.
   - If needed, create small internal rendering helpers for overlays, announcements, HUD state, and leaderboard formatting instead of scattering direct DOM updates.
   - Keep all assets inline or procedurally generated; do not introduce external font, image, or script dependencies that would weaken single-file portability.

7. Harden verification for build mode.
   - Update `verification/verify_game.py` to assert brand-critical UI text, overlay visibility transitions, and basic gameplay startup rather than only taking screenshots.
   - Update `verification/verify_weapon.py` to validate the renamed/modernized HUD labels and the full toggle flow after the visual redesign.
   - Add at least one additional automated verification path for pause/restart or game-over flow if practical within the current Playwright/Python setup.

## Files and Areas to Touch
- `docs/index.html`
  - CSS root variables, typography, overlay styling, button styling, responsive rules.
  - HUD markup and labels.
  - Start screen, wave screen, pause treatment, leaderboard, game-over copy.
  - JavaScript config/constants, UI state handling, overlay orchestration, gameplay tuning, and rendering effects.
- `verification/verify_game.py`
  - Expand assertions for startup overlay, branded labels, begin-play transition, and at least one gameplay/HUD state.
- `verification/verify_weapon.py`
  - Update selectors/assertions to match new HUD copy and ensure weapon switching still works.
- `verification/`
  - If necessary, add one more focused Playwright script for pause or restart flow while keeping the verification footprint simple.
- `README.md`
  - Only touch if post-implementation instructions or visual/style description become materially inaccurate.

## Validation and Test Criteria
- Automated checks
  - Start a local server from the repo root with `python3 -m http.server 8080`.
  - Run `python3 verification/verify_game.py` and require it to pass without uncaught exceptions.
  - Run `python3 verification/verify_weapon.py` and require it to pass without uncaught exceptions.
  - If a new verification script is added for pause/restart or game-over flow, run it explicitly, for example `python3 verification/verify_pause_restart.py`.
  - Add concrete Playwright assertions for the following at minimum:
    - Start overlay shows branded title and uppercase command button.
    - HUD exposes `SCORE`, `HI-SCORE`, `WAVE`, and `AMMO`, plus the chosen survival metric label.
    - Starting the game hides the start overlay and leaves the canvas interactive.
    - Toggling weapon mode changes the weapon label/state and remains functional via both click and keyboard.
    - Pausing the game surfaces a visible `PAUSED` state and unpausing returns to play.
    - Restart/end-game flow presents the branded failure/reboot language expected by the new UI.
- Manual verification
  - Open `http://localhost:8080/docs/index.html` on desktop and confirm the page fills the viewport with no scrollbars and no external asset failures.
  - Verify the visual system is mostly grayscale with one restrained accent, glass overlays have blur, white border, and soft glow, and buttons use a noticeable hover-lift interaction.
  - Confirm all player-facing labels that belong to the Robrary command layer are uppercase and use consistent terminology across start, pause, wave, and game-over screens.
  - Play through at least three waves and confirm the game remains mechanically centered on defending cities with meaningful ammo decisions and visibly distinct `NORMAL` vs `FLAK` behavior.
  - Force or play into a failure state and confirm `MISSION FAILED` and `REBOOT` flow works, leaderboard entry still functions, and local high-score persistence survives a page reload.
  - Verify mobile responsiveness using a narrow viewport in browser devtools: overlays fit, HUD remains legible, touch input still fires shots, and no controls become unreachable.
  - Reload the page after a completed session and confirm single-file delivery still works without any build step or missing dependency.

## Risks and Open Questions
- The exact menu structure used by the other Jules games is not present in this repo, so build mode will need to infer a compatible structure from the stated terminology and brand rules rather than matching an imported template.
- Adding too many new mechanics could dilute the current game's identity; implementation should prioritize polish, pacing, readability, and one or two focused gameplay upgrades over feature sprawl.
- `LIVES` is not a current first-class concept in the game logic, so implementation must decide whether it represents remaining cities, silo integrity, or a new aggregated metric; this should be resolved early to avoid confusing HUD copy.
- More dramatic visual effects could hurt readability or performance on mobile if blur, particles, and glow are overused; build mode should keep effects scalable and test on a narrow viewport.
- Existing Playwright scripts assume specific selectors and text. Any UI restructuring must preserve stable selectors or update the scripts in lockstep.
