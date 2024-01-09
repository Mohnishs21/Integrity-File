
# File Integrity Monitor README

Description:

This PowerShell script monitors a specified directory for file changes, deletions, and new additions. It utilizes file hashes to detect modifications and provides real-time alerts.

Usage:

Save the script: Place the script in a convenient location.
Run the script: Open a PowerShell window and execute the script's file path.
Choose an action: The script will prompt you to either:
(A) Collect a new baseline of file hashes
(B) Begin monitoring files with a saved baseline
Follow instructions: The script will guide you through the process based on your choice.
Key Features:

Baseline Collection: Creates a baseline file containing file paths and their corresponding SHA512 hashes for future comparisons.
Continuous Monitoring: Repeatedly checks the target directory for changes and displays alerts in the console.
Change Detection: Identifies modified, deleted, and newly added files.
Color-Coded Alerts: Uses colors to visually distinguish different types of file changes.
Customizable Target Directory: Allows specifying the directory to monitor (default is ".\Files").
Requirements:

PowerShell version 3.0 or later
Additional Notes:

The script creates a file named "baseline.txt" to store file hashes for monitoring.
To modify the target directory, adjust the $targetDirectory variable within the script.
While the script is running, changes to files within the target directory will be detected and displayed in real-time.
To end the monitoring process, press Ctrl+C in the PowerShell window.
Testing:

It's highly recommended to test the script in a non-production environment before deployment.
Create a test directory with sample files to verify its functionality.
