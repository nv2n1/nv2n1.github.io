---
title: "Capturing stderr with tee in Linux"
date: 2018-03-24 11:51:14 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-make-tee-catch-the-stderr-only-in-linux/
---

The `tee` command by default reads from stdin and writes to both stdout and files. To capture only stderr, you need to explicitly redirect it.

## Basic stderr redirection to tee

The straightforward approach is to redirect stderr to stdout, then pipe to tee:

``` bash
command 2>&1 | tee output.log
```

This captures both stdout and stderr. If you want *only* stderr:

``` bash
command 2>&1 1>/dev/null | tee error.log
```

This works by:

1.  `2>&1` — redirects stderr to stdout
2.  `1>/dev/null` — discards the original stdout
3.  `| tee error.log` — captures only stderr to the file

## Using process substitution for cleaner syntax

A more readable approach uses process substitution:

``` bash
command 2> >(tee error.log)
```

This syntax:

- `2>` redirects stderr to a process
- `>(tee error.log)` creates a process that receives stderr and writes it to both the terminal and `error.log`

The advantage here is clarity — it’s immediately obvious you’re capturing stderr.

## Capturing both streams separately

If you need stdout and stderr in different files simultaneously:

``` bash
command > >(tee stdout.log) 2> >(tee stderr.log)
```

Both streams display on the terminal and write to their respective files.

## Combining with grep or other filters

You can pipe stderr through filters before tee:

``` bash
command 2>&1 1>/dev/null | grep "ERROR" | tee errors-only.log
```

This captures only lines containing “ERROR” from stderr.

## Real-world example: capturing deployment logs

``` bash
./deploy.sh 2> >(tee deploy-errors.log >&2) | tee deploy-full.log
```

This:

- Captures stderr to `deploy-errors.log` while keeping it on stderr (`>&2`)
- Captures stdout to `deploy-full.log`
- Displays both streams on the terminal

The `>&2` at the end ensures stderr goes back to the terminal after being teed.

## Appending instead of overwriting

Use the `-a` flag to append rather than overwrite:

``` bash
command 2> >(tee -a error.log)
```

## Suppressing terminal output while saving to file

If you only want the file, not the terminal output:

``` bash
command 2> >(tee error.log >/dev/null)
```

The inner `>/dev/null` discards tee’s terminal output; stderr is still written to the file.

## Combining with systemd services

For systemd services, capture stderr/stdout through `journalctl`:

``` bash
journalctl -u service-name -f | tee service.log
```

This follows live logs and saves them to a file. For persistent capture, configure the service file:

``` ini
[Service]
StandardOutput=journal
StandardError=journal
SyslogIdentifier=myservice
```

Then logs appear in journalctl with your identifier tag.

## Performance considerations

Process substitution adds a small file descriptor overhead. For high-frequency logging (thousands of lines/second), consider:

``` bash
command 2>>error.log 1>>stdout.log
```

Direct redirection has less overhead than pipes, though you lose real-time terminal visibility.

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
