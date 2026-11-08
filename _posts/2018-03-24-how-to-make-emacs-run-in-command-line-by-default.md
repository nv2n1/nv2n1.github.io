---
title: "Running Emacs in Terminal-Only Mode"
date: 2018-03-24 08:21:51 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-make-emacs-run-in-command-line-by-default/
---

If you want Emacs to run in the terminal without opening an X window, you have several practical options depending on your setup and workflow.

## Option 1: Install emacs-nox (Recommended for servers)

The cleanest approach is installing the no-X variant of Emacs, which is built without X11 support. This reduces memory overhead and startup time on headless systems.

**Debian/Ubuntu:**

``` bash
sudo apt install emacs-nox
```

**Red Hat/CentOS/Fedora:**

``` bash
sudo dnf install emacs-nox
```

**Arch Linux:**

``` bash
sudo pacman -S emacs-nox
```

If you have both `emacs` and `emacs-nox` installed and want to make `emacs-nox` the default, use the alternatives system:

On Debian/Ubuntu:

``` bash
sudo update-alternatives --config emacs
```

On Red Hat-based systems:

``` bash
sudo alternatives --config emacs
```

Select the emacs-nox entry from the menu.

## Option 2: Use the -nw flag (Quickest for ad-hoc use)

If you already have Emacs installed or need to keep the standard build, use the `-nw` (no-window) flag:

``` bash
emacs -nw myfile.txt
```

This forces terminal-mode operation even if X is available. Useful for:

- SSH sessions on remote machines
- Quick edits when you want to avoid GUI overhead
- Systems where X is misconfigured or unavailable
- Testing terminal behavior

## Option 3: Create a wrapper script (Best for frequent switching)

If you regularly toggle between GUI and terminal editing, create a wrapper script in your PATH:

``` bash
mkdir -p ~/.local/bin
cat > ~/.local/bin/em << 'EOF'
#!/usr/bin/env bash
exec emacs -nw "$@"
EOF
chmod +x ~/.local/bin/em
```

Then use `em` instead of `emacs`:

``` bash
em myfile.txt
em ~/.bashrc
```

Ensure `~/.local/bin` is in your `$PATH`. Check with:

``` bash
echo $PATH
```

If it’s missing, add it to your shell profile (`~/.bashrc`, `~/.zshrc`, or `~/.config/fish/config.fish`):

``` bash
export PATH="$HOME/.local/bin:$PATH"
```

## Option 4: Disable DISPLAY temporarily

You can disable X server detection by clearing the `DISPLAY` variable:

``` bash
DISPLAY= emacs myfile.txt
```

Add a shell alias for frequent use:

``` bash
alias em='DISPLAY= emacs'
```

This forces Emacs to fall back to terminal mode without creating permanent scripts.

## Option 5: Set default in your shell configuration

For persistent terminal-only behavior without changing your system Emacs installation, add an alias to your shell profile:

``` bash
# In ~/.bashrc, ~/.zshrc, or equivalent
alias emacs='emacs -nw'
```

This affects your user only and leaves system defaults unchanged, making it safe for multi-user environments.

## Comparison: Which approach to use

| Method | Best for | Pros | Cons |
|----|----|----|----|
| `emacs-nox` | Servers, CI/CD, headless systems | Smaller binary, faster startup, clean separation | Requires separate installation |
| `-nw` flag | Ad-hoc usage, one-off edits | Simple, works immediately | Must remember the flag each time |
| Wrapper script | Frequent switching between modes | Convenient alias, keeps both available | Extra file to maintain |
| `DISPLAY=` | Temporary overrides | No script needed | Less discoverable by team |
| Shell alias | Consistent user preference | Simple, easy to document | Affects all terminal invocations |

Most sysadmins use `emacs-nox` on production servers and remote machines for reliability and performance. On development workstations, use a wrapper or alias if you need both GUI and terminal modes available.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Running Emacs in Terminal-Only Mode with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Running Emacs in Terminal-Only Mode. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
