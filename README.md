# sync_onelap_strava_agent_skills

[简体中文](README.zh-CN.md)

Standalone Agent Skills distribution for OneLap -> Strava sync.

## What this repo provides

- A self-contained skill at `onelap-strava-sync/`
- Runtime Python code bundled under `onelap-strava-sync/scripts/`
- Lazy bootstrap installer that creates an isolated venv on first trigger

## Quick Install

```bash
npx skills add https://github.com/yintianan/sync_onelap_strava_agent_skills
```

This command automatically downloads and registers the skill in your local OneLap Agents environment. But you still need to run the manual initialization steps below before syncing.

## Copy-and-run usage

1. Copy `onelap-strava-sync` to `~/.agents/skills/`.
2. Trigger the skill with a OneLap/Strava sync request.
3. On first trigger, the skill creates:
   - `~/.agents/venvs/onelap-strava-sync/`
4. Dependencies are installed automatically from `scripts/requirements.txt`.

## Manual initialization required

Before syncing, run these two commands manually and follow the prompts:

```bash
python scripts/bootstrap.py --onelap-auth-init
python scripts/bootstrap.py --strava-auth-init
```

Note: OneLap (顽鹿) password input is hidden in terminal — no echo while typing. This is expected behavior.

**Before running `--strava-auth-init`**, you must register your own Strava API application to obtain a `client_id` and `client_secret`:

1. Go to [https://www.strava.com/settings/api](https://www.strava.com/settings/api) (login required).
2. Fill in the application name and other fields, then submit.
3. Copy your `Client ID` and `Client Secret` — you will be prompted to enter them when running `--strava-auth-init`.

## Acceptance checklist

- `python scripts/bootstrap.py --onelap-auth-init`
- `python scripts/bootstrap.py --strava-auth-init`
- `python scripts/bootstrap.py --since 2026-03-01`
- `python scripts/bootstrap.py --download-only --since 2026-03-01`

## Maintenance

- Source runtime repo: `C:/Users/13247/Documents/Code Project/opencode test`
- Sync helper: `tools/sync_from_runtime.ps1`

## Disclaimer

- This project is for **learning purposes only**.
- Do **not** use it for commercial purposes.
- Account information is stored **locally only**.
- Do **not** provide your account credentials to any agent.
- You are **solely responsible** for any consequences of using this tool.
