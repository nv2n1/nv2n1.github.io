---
title: "Identifying Which Process Listens on a Port in Linux"
date: 2018-03-24 11:46:35 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-find-which-program-or-process-is-listening-on-a-certain-port-in-linux/
---

When your application fails to bind to a port, you need to identify what’s already using it. This is one of the most common debugging tasks in Linux system administration.

## Using ss (Modern Approach)

The `ss` command has largely replaced `netstat` in modern Linux distributions. It’s faster, more efficient, and provides clearer output:

``` bash
ss -ltnp | grep :9999
```

Breaking down the flags:

- `l` — show listening sockets only
- `t` — TCP sockets
- `n` — numeric addresses (no DNS lookups)
- `p` — include process name and PID

If you need to check UDP ports as well:

``` bash
ss -ltnup | grep :9999
```

For a specific port without grep:

``` bash
ss -ltnp sport = :9999
```

You’ll typically need `sudo` to see process names and PIDs for sockets owned by other users:

``` bash
sudo ss -ltnp | grep :9999
```

## Using netstat (Legacy Alternative)

If your system still uses `netstat`, the syntax is similar:

``` bash
sudo netstat -pln | grep 9999
```

The flags mean:

- `p` — show process information
- `l` — listening sockets
- `n` — numeric format

Add `t` for TCP-only or `u` for UDP-only filtering:

``` bash
sudo netstat -ptln | grep 9999
sudo netstat -puln | grep 9999
```

## Using lsof

Another useful tool is `lsof`, which shows open files and network connections:

``` bash
sudo lsof -i :9999
```

This gives you the process name, PID, user, and connection status in an easy-to-read format.

## Practical Examples

Check what’s listening on port 80:

``` bash
sudo ss -ltnp | grep :80
```

Example output:

    LISTEN    0      511                0.0.0.0:80              0.0.0.0:*    users:(("nginx",pid=1234,fd=6))

Find all processes listening on any port:

``` bash
sudo ss -ltnp
```

Check if a specific service (like PostgreSQL on port 5432) is running:

``` bash
sudo ss -ltnp | grep :5432
```

Verify both TCP and UDP listeners on port 53 (DNS):

``` bash
sudo ss -ltnup | grep :53
```

## Permission Notes

If you run these commands without `sudo`, you’ll only see processes owned by your current user. System services and processes owned by other users will show as `(-)` in the output. Always use `sudo` for complete visibility when troubleshooting port conflicts.

## Why ss Over netstat

The `netstat` command is deprecated in many distributions. `ss` is part of the `iproute2` package and provides superior performance, especially on systems with many connections. If you’re writing scripts or automation for modern systems, prefer `ss`.

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
