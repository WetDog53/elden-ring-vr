# Elden Ring VR Mod

This repository is the working scaffold for a Melty-eligible Elden Ring VR mashup that uses Elden Ring as the required host game and Blade & Sorcery's VR input system as the source for motion controls.

## Goal

Create a first-person VR mode for Elden Ring with:
- hand tracking and grab interactions
- weapon swings driven by tracked hand motion
- spell casting through hand gestures
- VR-friendly locomotion and camera behavior
- a playable prototype that can be launched through ModEngine2 offline

## Required games

- Elden Ring (required host game)
- Blade & Sorcery (required VR input source for the initial pass)

## Safe build route

This project is designed to launch with ModEngine2 in offline mode. Elden Ring's online mode uses Easy Anti-Cheat; the mod should never be launched online.

## Repository structure

- `docs/vr-mod-blueprint.md` — design notes and project plan
- `sheets/` — source-of-truth JSON sheets for systems, actions, weapons, UI, and locomotion
- `scripts/preflight.py` — validates the sheet references before any build
- `scripts/export_mapping.py` — generates a rough action map from the sheets

## Status

This repo is intentionally a buildable foundation, not a finished game mod yet. The design sheets are the source of truth, and every row is expected to be checked before a release is considered playable.

## Quick start

1. Review the design sheet files in `sheets/`.
2. Run the preflight check:
   ```bash
   python scripts/preflight.py
   ```
3. Fix any unresolved references before building a code layer.
4. Use the generated mapping and design docs to bridge into the real game runtime.

## Notes

- This repo is for the mod source and validation process.
- The actual runtime packaging for Melty should happen only after a working offline build is validated.
- Do not publish anything until the mod is tested in the game and the recipe passes one-click checks.
