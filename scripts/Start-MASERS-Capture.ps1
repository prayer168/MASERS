$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$evidenceDir = Join-Path $repoRoot "docs\video\evidence\transcripts"
New-Item -ItemType Directory -Path $evidenceDir -Force | Out-Null
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$transcriptPath = Join-Path $evidenceDir "build-$stamp.txt"
Start-Transcript -Path $transcriptPath -NoClobber
Set-Location $repoRoot
Write-Output "MASERS BUILD CAPTURE START: $(Get-Date -Format o)"
Write-Output "Repository: $repoRoot"
Write-Output "Git branch and status:"
git status --short --branch
Write-Output "Recent commits:"
git log -5 --format="%h %ad %s" --date=iso-strict
Write-Output "Python:"
python --version
Write-Output "Transcript: $transcriptPath"
Write-Output "Recording remains active in this PowerShell host. Stop it with .\scripts\Stop-MASERS-Capture.ps1"
