# Command Reference

Run from the skill root directory `onelap-strava-sync/`.

- Default sync: `python scripts/bootstrap.py`
- Sync since date: `python scripts/bootstrap.py --since 2026-03-01`
- Download only: `python scripts/bootstrap.py --download-only --since 2026-03-01`
- OneLap account init: `python scripts/bootstrap.py --onelap-auth-init`
- Strava OAuth init: `python scripts/bootstrap.py --strava-auth-init`
