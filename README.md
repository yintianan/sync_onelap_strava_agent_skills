# sync_onelap_strava_agent_skills

Standalone Agent Skills distribution for OneLap -> Strava sync.

## What this repo provides

- A self-contained skill at `onelap-strava-sync/`
- Runtime Python code bundled under `onelap-strava-sync/scripts/`
- Lazy bootstrap installer that creates an isolated venv on first trigger

## Copy-and-run usage

1. Copy `onelap-strava-sync` to `~/.agents/skills/`.
2. Trigger the skill with a OneLap/Strava sync request.
3. On first trigger, the skill creates:
   - `~/.agents/venvs/onelap-strava-sync/`
4. Dependencies are installed automatically from `scripts/requirements.txt`.

## Acceptance checklist

- `python scripts/bootstrap.py --onelap-auth-init`
- `python scripts/bootstrap.py --strava-auth-init`
- `python scripts/bootstrap.py --since 2026-03-01`
- `python scripts/bootstrap.py --download-only --since 2026-03-01`

## Maintenance

- Source runtime repo: `C:/Users/13247/Documents/Code Project/opencode test`
- Sync helper: `tools/sync_from_runtime.ps1`
