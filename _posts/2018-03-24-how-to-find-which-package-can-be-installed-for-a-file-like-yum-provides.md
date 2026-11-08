---
title: "How to Find Which Package Provides a File"
date: 2018-03-24 11:43:38 +0000
modified: 2026-04-12 16:04:58 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-find-which-package-can-be-installed-for-a-file-like-yum-provides/
---

When you need a command or library file but don’t have the package installed, you need to search for which package provides it. On Red Hat/Fedora systems, `yum provides` or `dnf provides` does this. On Debian/Ubuntu, the equivalent is `apt-file`.

## Red Hat, Fedora, and CentOS (DNF/YUM)

Use `dnf provides` (or `yum provides` on older systems):

``` bash
$ dnf provides /usr/bin/ghci
ghc-9.2.8-1.fc37.x86_64 : The Glasgow Haskell Compilation system
Repo        : fedora
Matched from:
Filename    : /usr/bin/ghci
```

You can also search for partial paths or just the filename:

``` bash
$ dnf provides ghci
```

If you want to find what provides a library, search with the full path:

``` bash
$ dnf provides /usr/lib64/libssl.so.3
openssl-libs-3.0.7-1.fc37.x86_64 : Secure Sockets Layer and cryptography libraries and tools
Repo        : @System
Matched from:
Filename    : /usr/lib64/libssl.so.3
```

To install the package directly from the provides output:

``` bash
$ dnf install /usr/bin/ghci
```

DNF will resolve the package automatically.

## Debian and Ubuntu (apt-file)

Install and set up `apt-file`:

``` bash
$ sudo apt-get install apt-file
$ sudo apt-file update
```

The update step downloads the package file lists from configured repositories. This only needs to run once initially, then periodically to refresh:

``` bash
$ sudo apt-file search ghci
ghc: /usr/bin/ghci
ghc: /usr/bin/ghci-9.2.4
ghc: /usr/lib/ghc/bin/ghci
ghc: /usr/lib/ghc/bin/ghci-9.2.4
ghc: /usr/lib/ghc/ghci-usage.txt
ghc: /usr/share/man/man1/ghci.1.gz
ghc-doc: /usr/share/doc/ghc-doc/html/users_guide/ghci.html
hlint: /usr/share/hlint/hlint.ghci
```

The first column shows the package name, the second shows the full file path.

Search for libraries by name:

``` bash
$ apt-file search libssl.so.3
libssl3: /usr/lib/x86_64-linux-gnu/libssl.so.3
```

You can also search for executable names without the full path:

``` bash
$ apt-file search --basename curl
curl: /usr/bin/curl
```

Useful `apt-file` options:

- `--basename`: Search only in the filename, not the full path (faster for executables)
- `--package-only`: Show only package names, not paths
- `--limit N`: Show only the first N results

``` bash
$ apt-file search --package-only --basename gcc | head -5
gcc
gcc-11
gcc-12
gcc-13
g++
```

## When to Use Each Method

- **DNF/YUM**: Use the `dnf provides` syntax — it’s faster than `apt-file` because it queries live repository metadata without needing a pre-downloaded file list.
- **APT-file**: Requires an initial `apt-file update` step. The tradeoff is that it can search packages not currently in your configured repos, but the data can get stale.

Both methods answer the same question: “Which package do I need to install to get this file?”

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
