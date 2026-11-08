---
title: "Managing Multiple GCC Versions on Ubuntu"
date: 2018-03-24 11:47:07 +0000
modified: 2026-04-12 16:37:35 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-install-older-version-gcc-g-in-ubuntu-other-linux-distro-are-similar/
---

Many legacy projects require specific GCC versions that differ from your system default. Ubuntu makes this straightforward through the package manager and the `update-alternatives` system.

## Check available GCC versions

First, see what versions are available in your distribution’s repositories:

``` bash
apt-cache search ^gcc- | grep -E '^\s*gcc-[0-9]'
```

For Ubuntu 20.04 and later, you’ll typically find GCC 7 through the current version. Older versions like GCC 4.4 are no longer in standard repositories but may be available in the Ubuntu Toolchain Test PPA for some releases.

## Install multiple GCC versions

Install the specific versions you need alongside your current default:

``` bash
sudo apt-get install gcc-9 g++-9
sudo apt-get install gcc-11 g++-11
```

You can install as many versions as needed. The `multilib` packages (`gcc-9-multilib`, `g++-9-multilib`) are only necessary if you need to compile for 32-bit targets on a 64-bit system.

## Register versions with update-alternatives

Use `update-alternatives` to create a switchable set of symlinks. The priority number (last argument) determines which version is default—higher numbers take precedence:

``` bash
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 90
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 90
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 110
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 110
```

Notice the second argument to `--install` should match the target symlink name (`gcc` or `g++`), not include the version. Also register associated tools like `cc` and `c++`:

``` bash
sudo update-alternatives --install /usr/bin/cc cc /usr/bin/gcc 30
sudo update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++ 30
```

## Switch between versions interactively

Once registered, switch versions with:

``` bash
sudo update-alternatives --config gcc
sudo update-alternatives --config g++
```

This opens a menu where you select which version to use. Your choice persists until changed again.

## Set a specific version programmatically

To set a version without interaction:

``` bash
sudo update-alternatives --set gcc /usr/bin/gcc-11
sudo update-alternatives --set g++ /usr/bin/g++-11
```

## Verify your selection

Check which version is active:

``` bash
gcc --version
g++ --version
```

## Using older GCC versions (GCC 4.4, 5, 6, 7)

For truly legacy versions no longer in standard repos, add the Ubuntu Toolchain Test PPA (use with caution on production systems):

``` bash
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install gcc-7 g++-7
```

Alternatively, compile GCC from source if the version isn’t packaged. Avoid creating manual symlinks in `/usr/bin` as shown in older guides—`update-alternatives` handles this correctly and tracks changes properly.

## Project-specific approach

For a single project, avoid system-wide changes. Instead, export the compiler at build time:

``` bash
CC=gcc-9 CXX=g++-9 ./configure
make
```

Or with CMake:

``` bash
cmake -DCMAKE_C_COMPILER=gcc-9 -DCMAKE_CXX_COMPILER=g++-9 ..
```

This keeps different projects isolated and prevents accidental breakage of system tools that depend on specific compiler versions.

## 2026 Best Practices and Advanced Techniques

For Managing Multiple GCC Versions on Ubuntu, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
