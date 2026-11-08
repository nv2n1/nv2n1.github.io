---
title: "Locating procps Utilities Source Code"
date: 2018-03-24 11:48:53 +0000
modified: 2026-04-12 16:06:32 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /where-is-the-source-code-for-the-free-command-on-linux/
---

The `free` command—along with `ps`, `top`, `kill`, `pgrep`, and dozens of other system utilities—is maintained as part of the **procps-ng** project.

## Source repository

The source code is hosted at:

    https://gitlab.com/procps-ng/procps

You can clone it with:

``` bash
git clone https://gitlab.com/procps-ng/procps.git
cd procps
```

Most distributions package procps-ng, so you likely already have it installed. You can verify the version and check where the binary lives:

``` bash
free --version
which free
```

## What procps-ng is

procps-ng is a collection of command-line and full-screen utilities that read from the `/proc` pseudo-filesystem. This virtual filesystem exposes kernel data structures in a human-readable format, allowing these tools to report on running processes, memory usage, and system performance.

The `/proc` interface is Linux-specific; similar tools on other Unix systems may have different implementations, but the Linux procps-ng utilities are the standard for the ecosystem.

## Key utilities in procps-ng

- **free** — Display free, used, and cached memory
- **ps** — List running processes with detailed information
- **top** — Interactive real-time process and resource monitor
- **htop** — Improved interactive process viewer (separate project, but similar role)
- **pgrep/pkill** — Find and signal processes by name or attributes
- **pmap** — Show memory map and resident set of a process
- **vmstat** — Virtual memory statistics and I/O activity
- **slabtop** — Kernel memory slab allocation in real time
- **uptime** — System uptime and load average
- **w** — Connected users and their active commands
- **sysctl** — Read and modify kernel runtime parameters
- **snice** — Change process priority by name
- **watch** — Run a command repeatedly with full-screen output

Note: `skill` and `snice` are deprecated in favor of `pkill` and standard `nice`/`renice` commands.

## Building from source

If you need a custom build or the latest development version:

``` bash
git clone https://gitlab.com/procps-ng/procps.git
cd procps
./autogen.sh
./configure
make
sudo make install
```

Check the README and INSTALL files in the repository for build dependencies (typically autoconf, automake, and pkg-config).

## Why look at the source?

Reading the procps-ng source is useful if you’re:

- Debugging unexpected behavior in `free`, `ps`, or related tools
- Contributing patches or reporting bugs to the maintainers
- Understanding how Linux exposes process and memory information
- Porting these tools to non-standard environments
- Implementing similar functionality in your own code

The codebase is well-maintained, reasonably readable, and the GitLab repository accepts merge requests and issues from the community.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
