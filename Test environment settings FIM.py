# Test environment settings
$testDirectory = "C:\TestFiles"  # Specify the directory to monitor for testing
$baselineFile = "C:\TestBaseline.txt"  # Specify a test baseline file

# Function calls
$response = Get-UserChoice

if ($response -eq 'A') {
    Erase-Baseline-If-Already-Exists $baselineFile
    $files = Get-ChildItem -Path $testDirectory
    $baseline = @{}
    foreach ($f in $files) {
        $hash = Calculate-File-Hash $f.FullName
        $baseline.Add($hash.Path, $hash.Hash)
        "$($hash.Path)|$($hash.Hash)" | Out-File -FilePath $baselineFile -Append
    }
} elseif ($response -eq 'B') {
    $baseline = @{}
    Get-Content -Path $baselineFile | ForEach-Object {
        $path, $hash = $_.Split('|')
        $baseline.Add($path, $hash)
    }
    Monitor-Files $baseline $testDirectory
}
