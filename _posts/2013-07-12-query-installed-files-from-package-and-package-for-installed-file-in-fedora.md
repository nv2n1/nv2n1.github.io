---
title: "Querying Package Files and Reverse Lookups in Fedora"
date: 2013-07-12 16:32:03 +0000
layout: post
canonical: https://www.systutorials.com/query-installed-files-from-package-and-package-for-installed-file-in-fedora/
---

The `rpm` and `dnf` commands let you inspect exactly which files a package installed and find the package that owns a specific file. These queries work on both the host system and inside containers like Toolbox or Distrobox.

### List Files from an Installed Package

``` bash
rpm -ql package-name
```

This recursively lists all files and directories the package installed. For example:

``` bash
rpm -ql vim
```

Returns output like:

    /usr/bin/vim
    /usr/share/man/man1/vim.1.gz
    /usr/share/vim/vim90/autoload/...
    ...

To show only regular files (excluding directories):

``` bash
rpm -ql --fileprovide=1 package-name
```

Or pipe through grep to filter results:

``` bash
rpm -ql vim | grep -E '\.(so|a)$'  # shared libraries and archives
```

### Find the Package that Owns a File

``` bash
rpm -qf /path/to/file
```

This returns the package name that installed the file. For example:

``` bash
rpm -qf /usr/bin/vim
# Output: vim-9.0.xxx-x.fc41.x86_64
```

To get the package in a shorter format:

``` bash
rpm -qf --queryformat='%{NAME}\n' /usr/bin/vim
```

### Querying Uninstalled Packages

If you want to see what files a package *would* install without installing it, use `dnf`:

``` bash
dnf info --available package-name
```

For detailed file listing of an uninstalled package, download and inspect the RPM directly:

``` bash
dnf download --downloadonly package-name
rpm -ql ./package-name*.rpm
```

The `--downloadonly` option fetches the RPM without installing it.

### Using dnf5 for Package Queries

Modern Fedora systems use `dnf5` by default, which improves speed and reduces memory overhead. The `rpm` commands remain unchanged, but you can also query through dnf:

``` bash
dnf list installed package-name
```

This shows version and repository information, though `rpm -q` remains the fastest for simple package existence checks.

### Querying Inside Containers

If you’re using Toolbox or Distrobox to isolate development environments, the same commands work identically inside the container:

``` bash
toolbox run rpm -ql golang-bin
```

This queries files in the isolated container without affecting the host system. This is particularly useful when debugging dependency issues or verifying which version of a tool was installed.

### Practical Examples

Find all configuration files a package installed:

``` bash
rpm -ql nginx | grep etc
```

Locate all man pages:

``` bash
rpm -ql postgresql | grep man
```

Check which package provides a library your application needs:

``` bash
rpm -qf /usr/lib64/libssl.so.1.1
```

Verify that a package installed all expected binaries:

``` bash
rpm -ql git | grep bin
```

Get metadata about an installed package:

``` bash
rpm -qi vim  # full package information
rpm -q --changelog vim | head -20  # recent changelog entries
```

These tools are essential for package troubleshooting, auditing installed software, and verifying that critical files exist after installation.

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
