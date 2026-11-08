---
title: "SCP Multiple Files from Remote Server to Linux"
date: 2018-03-24 11:50:02 +0000
layout: post
canonical: https://www.systutorials.com/how-to-scp-multiple-files-from-remote-to-local-on-linux/
---

The scp command handles multiple files efficiently, whether you’re pushing to a remote server or pulling from one. Here are the practical approaches for copying multiple files from remote to local.

### Brace Expansion

Use brace expansion to specify discrete files:

``` bash
scp user@remote:file{1,2,3} ./
```

This works well when you have a known set of files with predictable naming. You can expand the list as needed:

``` bash
scp user@remote:config{.yml,.yaml,.json} ./
```

### Quoted Space-Separated List

Quote the remote path to pass multiple filenames as a single argument:

``` bash
scp user@remote:"file1 file2 file3" ./
```

This approach is useful when filenames contain spaces or special characters, though it requires careful quoting.

### Glob Patterns

For files matching a pattern, use wildcards. The `?` matches a single character:

``` bash
scp user@remote:file? ./
```

Use `*` for any number of characters:

``` bash
scp user@remote:*.log ./
```

Or match specific extensions:

``` bash
scp user@remote:*.{txt,md,rst} ./
```

When using glob patterns, the remote shell expands them server-side. If expansion fails (no matching files), scp will report an error.

### Recursive Directory Copy

To copy entire directories with their contents:

``` bash
scp -r user@remote:/path/to/directory ./
```

The `-r` flag enables recursive copying. This is essential when dealing with nested directory structures.

### Performance with Multiple Files

For large numbers of files, consider using rsync instead of scp:

``` bash
rsync -avz user@remote:/path/to/files/ ./
```

rsync is more efficient for bulk transfers because it:

- Skips already-transferred files
- Compresses data in transit
- Provides better progress reporting
- Can resume interrupted transfers with the `--partial` flag

### SSH Key Authentication

When using scp, ensure your SSH key is properly configured to avoid repeated password prompts:

``` bash
scp -i ~/.ssh/id_rsa user@remote:file1 file2 ./
```

Use an SSH agent to manage keys across multiple commands:

``` bash
eval $(ssh-agent)
ssh-add ~/.ssh/id_rsa
scp user@remote:file{1,2,3} ./
```

### Preserving File Metadata

Use the `-p` flag to preserve file modification times and permissions:

``` bash
scp -p user@remote:file{1,2} ./
```

This is important when copying configuration files or scripts where timestamps matter.

### Specifying Port and Options

If SSH runs on a non-standard port:

``` bash
scp -P 2222 user@remote:file{1,2} ./
```

Note: scp uses `-P` (uppercase) while ssh uses `-p` (lowercase) for port specification.

Combine multiple flags as needed:

``` bash
scp -P 2222 -r -p user@remote:/backup/configs ./
```

### Practical Example: Backup Multiple Log Files

``` bash
scp user@webserver:"/var/log/{apache2,nginx,syslog}" ~/backups/
```

This pulls three different log files from a web server into your local backups directory.

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
