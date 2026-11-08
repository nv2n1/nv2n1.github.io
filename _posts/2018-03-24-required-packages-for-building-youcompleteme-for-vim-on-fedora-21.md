---
title: "Fix YouCompleteMe Build Errors on Fedora"
date: 2018-03-24 11:46:44 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /required-packages-for-building-youcompleteme-for-vim-on-fedora-21/
---

YouCompleteMe’s installation script fails on Fedora with a CMake error about missing `PYTHON_LIBRARIES` and `PYTHON_INCLUDE_DIRS`, even when Python is already installed. The error looks like this:

    CMake Error at /usr/share/cmake/Modules/FindPythonLibs.cmake:201
      Could NOT find PythonLibs (missing: PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS)

The issue is that you have the Python runtime libraries installed but not the development headers needed for compilation.

## Installing the Required Packages

On Fedora, install the Python development package:

``` bash
sudo dnf install python3-devel
```

If you’re building YouCompleteMe for Python 2 (not recommended — Python 2 reached end-of-life in 2020), you’d use:

``` bash
sudo dnf install python2-devel
```

Note: `dnf` is the modern package manager on current Fedora versions. Older Fedora releases used `yum`, but that’s been deprecated since Fedora 22.

## Complete Build Dependencies

Beyond Python headers, YouCompleteMe requires a full C/C++ build environment. Install all necessary dependencies at once:

``` bash
sudo dnf install python3-devel cmake gcc gcc-c++ make git
```

## Building YouCompleteMe

Once dependencies are installed, build YouCompleteMe from your plugin directory:

``` bash
cd ~/.vim/bundle/YouCompleteMe
./install.py --clangd-completer
```

Or if using vim-plug or another plugin manager, navigate to the installation directory (usually `~/.vim/plugged/YouCompleteMe` for vim-plug).

### Build Options

The `install.py` script supports several completion engines:

- `--clangd-completer` — C/C++ and Objective-C support (recommended, requires clangd)
- `--java-completer` — Java support (requires Maven)
- `--go-completer` — Go support
- `--rust-completer` — Rust support (requires rustup)

For example, to build with C/C++ and Rust support:

``` bash
./install.py --clangd-completer --rust-completer
```

## Troubleshooting the Build

If the build still fails after installing python3-devel, verify CMake can find Python:

``` bash
cmake --system-information | grep Python
```

Check your Python installation path:

``` bash
python3 -c "import sys; print(sys.prefix)"
python3-config --includes
```

If you have multiple Python versions installed, explicitly point CMake to the correct one:

``` bash
./install.py --clangd-completer --cmake-flags="-DPython3_EXECUTABLE=$(which python3)"
```

## Using Modern Alternatives

If YouCompleteMe proves difficult to maintain, consider these modern alternatives:

- **vim-lsp** with language servers — lightweight and language-agnostic
- **coc.nvim** — more active maintenance, though heavier
- **neovim with built-in LSP** — if you can switch to Neovim

For Neovim 0.8+, native LSP with Mason for language server management is significantly easier to set up than YouCompleteMe.

## Related Linux Commands

These related commands are often used alongside the tools discussed in this article:

- man command-name – Read the manual page for any command
- which command-name – Find the location of an executable
- rpm -qa or dpkg -l – List installed packages
- journalctl -u service-name – Check service logs
- ss -tulpn – List listening ports and services

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Best Practices and Advanced Techniques

For Fix YouCompleteMe Build Errors on Fedora, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
