---
title: "How to Export and Backup PuTTY Sessions"
date: 2018-03-24 08:18:01 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-save-putty-profiles-sessions/
---

PuTTY stores session configurations in the Windows Registry. If you’re migrating to a new computer, setting up multiple workstations, or just want a backup, here’s how to export and backup your PuTTY sessions.

## Export from Windows Registry

PuTTY sessions are stored at `HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions`. Export them using regedit or the command line:

```wp-block-code
# Export all PuTTY sessions
regedit /e "%USERPROFILE%\Desktop\putty-sessions.reg" HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions

# Export all PuTTY configuration (sessions + sshkeys + settings)
regedit /e "%USERPROFILE%\Desktop\putty-all.reg" HKEY_CURRENT_USER\Software\SimonTatham\PuTTY
```

The `.reg` file is a plain text file that you can import on another Windows machine by double-clicking it.

## Export Specific Sessions

To export individual sessions, find the session name in the registry:

```wp-block-code
# Each session is a subkey under Sessions
# Session names are stored as URL-encoded strings
# "My Server" appears as "My%20Server"

# Export a single session
regedit /e "%USERPROFILE%\Desktop\myserver.reg" "HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\My%20Server"
```

## Export SSH Keys

PuTTY stores saved SSH keys separately at `HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\SshHostKeys`:

```wp-block-code
regedit /e "%USERPROFILE%\Desktop\putty-ssh-keys.reg" HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\SshHostKeys
```

This exports the known host key fingerprints. Your private keys (.ppk files) are stored on disk, not in the registry — back those up separately from wherever you saved them.

## Import on Another Machine

Copy the `.reg` file to the new computer and double-click it. Windows will ask for confirmation to add the entries to the registry. After importing, open PuTTY and your sessions will appear in the saved sessions list.

From the command line:

```wp-block-code
regedit /i putty-sessions.reg
```

## Convert to Portable Format

If you want to run PuTTY from a USB drive without touching the registry, use **PuTTY Portable** from PortableApps.com. It stores sessions in INI files instead of the registry.

To convert existing registry sessions to INI format for PuTTY Portable:

1.  Install PuTTY Portable
2.  Export your registry sessions as described above
3.  Use a conversion tool like `putty-session2ini` to transform the .reg data into PuTTY Portable’s format

## Convert PuTTY Sessions to OpenSSH Config

If you’re migrating from Windows/PuTTY to Linux/macOS with OpenSSH, convert your sessions:

```wp-block-code
# Install the conversion tool
pip install putty-ssh-config-generator

# Convert exported .reg to ~/.ssh/config
putty2ssh putty-sessions.reg > ~/.ssh/config
```

Or manually create entries based on PuTTY settings. A PuTTY session maps to an SSH config entry like:

```wp-block-code
Host myserver
    HostName 192.168.1.100
    User admin
    Port 2222
    IdentityFile ~/.ssh/mykey.pem
    ServerAliveInterval 60
```

## Backup Script

Automate regular backups with a batch script:

```wp-block-code
@echo off
set BACKUP_DIR=%USERPROFILE%\Backups\Putty
set DATE=%date:~-4,4%%date:~-7,2%%date:~-10,2%
mkdir "%BACKUP_DIR%" 2>nul
regedit /e "%BACKUP_DIR%\putty-sessions-%DATE%.reg" HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions
regedit /e "%BACKUP_DIR%\putty-ssh-keys-%DATE%.reg" HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\SshHostKeys
echo PuTTY backup saved to %BACKUP_DIR%
```

Schedule this with Windows Task Scheduler for automatic daily or weekly backups.

## Using WinSCP Instead

WinSCP can import PuTTY sessions directly and stores its own sessions in an INI file, making them easier to back up and portable. If you use both tools, consider managing sessions through WinSCP and launching PuTTY from WinSCP’s interface.

## Using PowerShell for Export

On modern Windows, use PowerShell for more control over the export:

```wp-block-code
# Export PuTTY sessions to individual files
$regPath = "HKCU:\Software\SimonTatham\PuTTY\Sessions"
$backupDir = "$env:USERPROFILE\Backups\PuTTY"
New-Item -ItemType Directory -Force -Path $backupDir

Get-ChildItem $regPath | ForEach-Object {
    $sessionName = $_.PSChildName -replace '%20', ' '
    $output = "$backupDir\$sessionName.txt"
    Get-ItemProperty $_.PSPath | Out-File $output
    Write-Host "Exported: $sessionName"
}
```

## Migrating to OpenSSH on Windows

Windows 10 and 11 include OpenSSH natively. If you’re moving away from PuTTY, convert your sessions to the SSH config format:

```wp-block-code
# Windows SSH config location: C:\Users\YourName\.ssh\config

Host myserver
    HostName 192.168.1.100
    User admin
    Port 2222
    IdentityFile ~/.ssh/mykey
    ServerAliveInterval 60
```

Convert PuTTY .ppk keys to OpenSSH format:

```wp-block-code
# Using puttygen (WSL or Linux)
puttygen mykey.ppk -O private-openssh -o ~/.ssh/mykey
chmod 600 ~/.ssh/mykey
```

OpenSSH on Windows uses the same config format as Linux and macOS, making your configuration portable across all platforms without registry dependencies.
