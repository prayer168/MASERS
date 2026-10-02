$ErrorActionPreference = "Continue"
Write-Output "MASERS BUILD CAPTURE STOP: $(Get-Date -Format o)"
git status --short --branch
git log -3 --format="%h %ad %s" --date=iso-strict
Stop-Transcript
