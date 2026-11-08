---
title: "Converting Relative Paths to Absolute Paths in Linux"
date: 2018-03-24 08:04:07 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-find-linux-absolute-path-for-a-relative-path/
---

When working with relative paths in Linux, you often need the absolute path for scripting, logging, or passing to other programs. Several tools can resolve this, each with different strengths.

### Using readlink

The `readlink` command is the traditional tool for this job. The `-f` flag follows symlinks and resolves the path to its absolute form:

``` bash
readlink -f ./
```

For a file in a subdirectory:

``` bash
readlink -f ./documents/file.txt
```

One caveat: `readlink -f` will fail if the target doesn’t exist. If you need to resolve a path that may not exist yet, use `-m` instead:

``` bash
readlink -m ./path/that/doesnt/exist/yet
```

The difference matters in scripts. Use `-f` when verifying actual files and directories; use `-m` for paths you’re about to create.

### Using realpath

The `realpath` command is more modern and often clearer in intent:

``` bash
realpath ./
realpath ./documents/file.txt
```

Like `readlink -f`, it requires the path to exist. For non-existent paths, add `--relative-to`:

``` bash
realpath --relative-to=/some/base ./relative/path
```

You can also use the `--quiet` flag to suppress errors if a path doesn’t exist:

``` bash
realpath --quiet ./maybe/missing/file.txt
```

### Using pwd with cd

In shell scripts, you can combine `cd` with `pwd`:

``` bash
cd ./documents && pwd
```

This works reliably but changes your current directory, so it’s less clean in scripts. Better to use a subshell:

``` bash
(cd ./documents && pwd)
```

The subshell approach preserves your original location.

### Practical Examples

Find the absolute path of the current directory:

``` bash
readlink -f .
realpath .
```

Resolve a relative path and use it in a variable:

``` bash
TARGET=$(realpath ./config/app.conf)
echo "Configuration file: $TARGET"
```

Handle symlinks explicitly:

``` bash
# Follow symlinks to the actual file
readlink -f ./link-to-file

# Show the symlink target without following further
readlink ./link-to-file
```

Batch resolve multiple paths:

``` bash
for path in ./dir1 ./dir2 ./file.txt; do
  realpath "$path"
done
```

### Choosing the Right Tool

- **readlink -f**: Available on most Linux systems, POSIX-compliant
- **realpath**: Clearer semantics, better error handling, available in GNU coreutils
- **pwd with subshell**: Useful when you need current working directory context

For new scripts, prefer `realpath` if it’s available on your target systems (it ships with most modern Linux distributions). For maximum portability, use `readlink -f`, but test with `-m` if dealing with non-existent paths.

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
