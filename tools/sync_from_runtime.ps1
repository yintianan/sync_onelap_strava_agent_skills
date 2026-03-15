param(
    [string]$RuntimeRepoPath = "C:\Users\13247\Documents\Code Project\opencode test",
    [string]$SkillRepoPath = "C:\Users\13247\Documents\Code Project\sync_onelap_strava_agent_skills"
)

$source = Join-Path $RuntimeRepoPath "src\sync_onelap_strava"
$target = Join-Path $SkillRepoPath "onelap-strava-sync\scripts\sync_onelap_strava"

if (-not (Test-Path $source)) {
    throw "source path not found: $source"
}

New-Item -ItemType Directory -Force -Path $target | Out-Null
Copy-Item -Path (Join-Path $source "*.py") -Destination $target -Force
Copy-Item -Path (Join-Path $RuntimeRepoPath "requirements.txt") -Destination (Join-Path $SkillRepoPath "onelap-strava-sync\scripts\requirements.txt") -Force

Write-Output "sync complete"
