---
name: onelap-strava-sync
description: Sync OneLap FIT files to Strava and run auth initialization flows. Use when users ask to sync activities, download FIT files only, initialize OneLap account credentials, or initialize Strava OAuth tokens.
compatibility: Requires Python 3 and network access for first dependency install.
---

# OneLap to Strava Sync

中文名：OneLap 同步 Strava

## Purpose

Use this skill to run OneLap to Strava sync workflows directly from this skill package.

## Trigger

- User asks to sync OneLap FIT files to Strava.
- User asks to download OneLap FIT files without upload.
- User asks to initialize or configure OneLap account credentials.
- User asks to initialize Strava OAuth tokens.

## How to run

All commands should run via bootstrap launcher:

- `python scripts/bootstrap.py`

See `references/commands.md` for full command examples.

## Runtime behavior

- First trigger creates isolated venv: `~/.agents/venvs/onelap-strava-sync/`
- Installs dependencies from `scripts/requirements.txt`
- Reuses venv on later runs
