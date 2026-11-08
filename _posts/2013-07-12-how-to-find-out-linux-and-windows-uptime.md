---
title: "Checking System Uptime on Linux and Windows"
date: 2013-07-12 16:32:21 +0000
layout: post
canonical: https://www.systutorials.com/how-to-find-out-linux-and-windows-uptime/
---

The `uptime` command is the quickest way to check how long your system has been running:

``` bash
$ uptime
22:19:29 up 10 days, 22:26,  5 users,  load average: 0.00, 0.00, 0.01
```

This output shows:

- Current time: 22:19:29
- System running for: 10 days, 22 hours, 26 minutes
- Active user sessions: 5
- Load averages: 1-minute, 5-minute, and 15-minute values (0.00, 0.00, 0.01)

For just the uptime value without additional information, use:

``` bash
$ uptime -p
up 10 days, 22 hours, 26 minutes
```

To get the system boot time:

``` bash
$ uptime -s
2024-11-29 23:53:03
```

If you need more detailed boot information, use the `who` command:

``` bash
$ who -b
         system boot  2024-11-29 23:53
```

For systems using systemd (most modern distributions), check boot time with:

``` bash
$ systemctl show --property=SinceBootUSec
```

Or use `journalctl`:

``` bash
$ journalctl -n 1 -b
```

The `last` command shows boot history:

``` bash
$ last -x | grep boot
```

## Getting System Uptime on Windows

### Via Command Line

The most direct method is using `systeminfo`:

``` powershell
systeminfo | find "System Boot Time"
```

This returns output like:

    System Boot Time: 12/15/2024, 2:30:45 PM

To calculate uptime manually, get the current date and time:

``` powershell
Get-Date
```

PowerShell provides a cleaner method. Get the last boot time directly:

``` powershell
(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
```

This displays uptime as a TimeSpan object showing days, hours, minutes, and seconds.

For a more detailed view in PowerShell:

``` powershell
$LastBoot = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
$Uptime = (Get-Date) - $LastBoot
Write-Host "System Uptime: $($Uptime.Days) days, $($Uptime.Hours) hours, $($Uptime.Minutes) minutes"
```

The older `net statistics server` command still works on many systems:

``` powershell
net statistics server
```

Look for the “Statistics since” line which shows the boot timestamp. This command is less reliable on modern Windows versions.

### Via GUI

Open Task Manager (Ctrl+Shift+Esc) and navigate to the **Performance** tab. Select **System** from the left sidebar — uptime displays in the lower section.

## Practical Considerations

On Linux, systems running for months or years may show large numbers. Monitor uptime regularly to track unexpected reboots caused by crashes, kernel updates, or power events.

On Windows, uptime resets after system updates that require reboots. Some enterprise environments use tools like WSUS or scheduled maintenance windows that cause regular reboots.

For automation and monitoring, parsing uptime in scripts:

**Linux example:**

``` bash
UPTIME=$(uptime -s)
echo "Last boot: $UPTIME"
```

**PowerShell example:**

``` powershell
$LastBoot = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
if ($LastBoot -lt (Get-Date).AddDays(-30)) {
    Write-Host "Warning: System has been up for more than 30 days"
}
```

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
