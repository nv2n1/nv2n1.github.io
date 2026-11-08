---
title: "Listing Running Services on Linux with systemctl"
date: 2018-03-24 11:44:56 +0000
layout: post
canonical: https://www.systutorials.com/how-to-list-all-running-system-service-on-linux-mint-17-1/
---

Listing active services is essential for system monitoring and troubleshooting. Whether you’re investigating a hung process, checking if a daemon started correctly, or auditing what’s actually running on your system, knowing how to query service status quickly saves time.

## Basic Command

The standard way to list running services across all modern Linux distributions is:

``` bash
systemctl list-units --type=service --state=running
```

This shows only services that are currently active. The output includes the service name, load state, active state, and a brief description.

## Common Variations

To see all services (including stopped ones):

``` bash
systemctl list-units --type=service --all
```

For a more compact output with just service names:

``` bash
systemctl list-units --type=service --state=running --no-pager
```

The `--no-pager` flag is useful in scripts or when piping output to other commands.

To see services that failed to start:

``` bash
systemctl list-units --type=service --state=failed
```

## Detailed Service Information

If you need to inspect a specific service in detail:

``` bash
systemctl status nginx
```

This shows the full status, recent log entries, and whether the service is enabled to start at boot.

To see all enabled services (those that start automatically):

``` bash
systemctl list-unit-files --type=service --state=enabled
```

## Real-Time Resource Monitoring

For a top-like view of service resource consumption by cgroup:

``` bash
systemd-cgtop
```

This tool displays CPU usage, memory consumption, and I/O metrics for each service in real time. It’s invaluable when tracking down resource-hungry daemons without spawning multiple monitoring tools.

## Filtering and Searching

Pipe systemctl output to grep for targeted searches:

``` bash
systemctl list-units --type=service --all | grep mysql
```

Or use systemctl’s built-in filtering:

``` bash
systemctl list-units --type=service --state=running --no-pager | grep -E "nginx|apache|mysql"
```

## Legacy Commands

The older `service --status-all` command still works on most distributions for backward compatibility:

``` bash
service --status-all
```

However, this lacks the dependency tracking and detailed state information that systemctl provides. Avoid relying on it for new scripts or automation.

## Practical Use Cases

Check if a service is running before attempting to restart it:

``` bash
systemctl is-active nginx && echo "Running" || echo "Not running"
```

Get a count of total running services:

``` bash
systemctl list-units --type=service --state=running --no-pager | wc -l
```

Export a list of all enabled services for documentation:

``` bash
systemctl list-unit-files --type=service --state=enabled --no-pager > enabled-services.txt
```

Modern systemd provides far more insight into service state, dependencies, and resource usage than older init systems. Mastering `systemctl` is essential for effective Linux system administration.

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
