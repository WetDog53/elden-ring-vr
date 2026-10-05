# VR Mod Blueprint

## Project intent

This file captures the first playable goal for the Elden Ring VR mod.

### One-sentence pitch

Elden Ring becomes a first-person VR action experience where the player uses tracked hands and motion-based inputs to wield weapons, cast spells, and move through Limgrave.

### Player loop in the first minute

- Start in Limgrave
- Put the headset on
- See the player hands in first-person view
- Grab a weapon with the dominant hand
- Swing it in a real motion arc to attack
- Move using the VR locomotion route
- Cast a basic spell with a hand gesture

### Required build targets

- Weapon swing detection from hand motion
- Spell gesture recognition
- Camera follow tied to headset pose
- UI adapted for VR instead of the flat menu
- Occasional outside-the-box comfort options

## Build approach

### 1. Source of truth: sheets

Everything begins in the JSON sheets under `sheets/`. Each row describes a single system element; each column captures a property. This keeps the design inspectable and prevents ad hoc code that is impossible to trace.

### 2. Preflight before build

Before any runtime code is created, every row and cell must be checked:
- every required field must be filled
- all references between sheets must resolve
- no duplicate action names or target IDs
- no unsupported control mapping if a required game path is missing

### 3. Runtime strategy

The actual implementation should be done in a small, testable sequence:
1. camera + head tracking
2. hand skeleton mapping
3. weapon swing detection
4. spell casting
5. UI interactions
6. locomotion and comfort options
7. packaging and validation for Melty

## Required modding route

The project should target ModEngine2 as the runtime loader for Elden Ring. Melty can install it itself, which matches the requirement to build on a loader Melty knows how to start in one click.

## Current status

This document is the initial blueprint. It is not a finished release. The next move is to populate the sheets and run the preflight validation.
