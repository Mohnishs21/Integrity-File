function Calculate-File-Hash($filepath) {
    return Get-FileHash -Path $filepath -Algorithm SHA512
}

function Erase-Baseline-If-Already-Exists($baselineFile = "baseline.txt") {
    Remove-Item -Path $baselineFile -ErrorAction SilentlyContinue
}

function Get-UserChoice() {
    while ($true) {
        $response = Read-Host -Prompt "What would you like to do? (A) Collect new Baseline, (B) Begin monitoring files with saved Baseline"
        $response = $response.ToUpper()
        if ($response -in 'A', 'B') {
            return $response
        }
        Write-Host "Invalid choice. Please enter 'A' or 'B'."
    }
}

function Monitor-Files($baseline, $targetDirectory = ".\Files") {
    while ($true) {
        $files = Get-ChildItem -Path $targetDirectory
        foreach ($f in $files) {
            $hash = Calculate-File-Hash $f.FullName

            if ($baseline.ContainsKey($hash.Path)) {
                if ($baseline[$hash.Path] -ne $hash.Hash) {
                    Write-Host "$($hash.Path) has changed!!!" -ForegroundColor Yellow
                }
            } else {
                Write-Host "$($hash.Path) has been created!" -ForegroundColor Green
            }
        }

        foreach ($path in $baseline.Keys) {
            if (-Not (Test-Path -Path $path)) {
                Write-Host "$($path) has been deleted!" -ForegroundColor DarkRed -BackgroundColor Gray
            }
        }

        Start-Sleep -Seconds 1
    }
}

$response = Get-UserChoice

if ($response -eq 'A') {
    Erase-Baseline-If-Already-Exists
    $files = Get-ChildItem -Path ".\Files"  # Adjust the target directory if needed
    $baseline = @{}
    foreach ($f in $files) {
        $hash = Calculate-File-Hash $f.FullName
        $baseline.Add($hash.Path, $hash.Hash)
        "$($hash.Path)|$($hash.Hash)" | Out-File -FilePath ".\baseline.txt" -Append
    }
} elseif ($response -eq 'B') {
    $baseline = @{}
    Get-Content -Path ".\baseline.txt" | ForEach-Object {
        $path, $hash = $_.Split('|')
        $baseline.Add($path, $hash)
    }
    Monitor-Files $baseline
}
