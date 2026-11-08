---
title: "Standardizing Tree Output Across Linux Distributions"
date: 2018-03-24 11:48:14 +0000
layout: post
canonical: https://www.systutorials.com/how-to-make-tree-output-consistent-on-linux/
---

When running `tree` across multiple servers or sharing output with teammates, you’ll notice the formatting can vary significantly. Some systems display box-drawing characters while others use ASCII pipes and dashes, making diff comparisons and documentation inconsistent.

## Understanding the Charset Differences

The `tree` command respects the system’s locale and character encoding settings. By default, it will output Unicode box-drawing characters on UTF-8 systems and ASCII on legacy systems:

**UTF-8 output (default on modern systems):**

    .
    ├── test2
    │   ├── test4
    │   └── test5
    └── test3

    1 directory, 3 files

**ASCII output (legacy/portable):**

    .
    |-- test2
    |   |-- test4
    |   `-- test5
    `-- test3

    1 directory, 3 files

## Using –charset for Consistent Output

Force consistent output with the `--charset` flag:

``` bash
tree --charset=ascii
tree --charset=utf-8
```

The ASCII option is more portable and reliable across heterogeneous environments—embedded systems, older terminals, CI/CD logs, and equipment with limited UTF-8 support will all render it correctly.

## Making It Your Default

For permanent consistency, add an alias to your `.bashrc` or `.zshrc`:

``` bash
alias tree='tree --charset=ascii'
```

Or set it environment-wide by creating `/etc/profile.d/tree.sh`:

``` bash
export TREE_CHARSET=ascii
```

Note: The environment variable approach works with some versions of `tree`, but the alias method is more reliable across distributions.

## Additional Options for Consistent Output

Combine `--charset` with other flags for reproducible results:

``` bash
# ASCII with directory-only view (useful for diffs)
tree --charset=ascii -d

# ASCII with hidden files included
tree --charset=ascii -a

# ASCII with permissions and ownership
tree --charset=ascii -pug

# ASCII with file sizes (useful for documentation)
tree --charset=ascii -h
```

## Comparing Output Across Systems

When verifying directory structures with `diff`:

``` bash
# On system A
tree --charset=ascii > /tmp/tree_a.txt

# On system B
tree --charset=ascii > /tmp/tree_b.txt

# Compare
diff /tmp/tree_a.txt /tmp/tree_b.txt
```

If you need to ignore file counts or timestamps, pipe through `head -n -2` to strip the summary line:

``` bash
tree --charset=ascii | head -n -2 > tree_output.txt
```

## Checking Your tree Version

Some older `tree` installations don’t support the `--charset` option. Verify support:

``` bash
tree --help | grep charset
```

If unavailable, upgrade `tree`:

``` bash
# Debian/Ubuntu
sudo apt install tree

# RHEL/CentOS/Fedora
sudo dnf install tree

# macOS
brew install tree
```

The `--charset=ascii` approach is the standard for ensuring consistency across heterogeneous infrastructure and is the best choice when cross-platform reliability matters.

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
