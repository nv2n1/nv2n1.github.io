---
title: "How to Reset All Git Submodules"
date: 2020-10-11 15:03:16 +0000
modified: 2026-04-12 16:47:21 +0000
author: "David Yang"
layout: post
categories: [testing-devops]
canonical: /how-to-reset-all-submodules-in-git/
---

Git submodules let you keep a Git repository as a subdirectory of another Git repository. When they get into a bad state—detached HEAD, local changes, merge conflicts—you need a clean reset.

## The complete deinit and reinit method

This is the most thorough approach. It removes all submodule state and rebuilds from scratch:

``` bash
git submodule deinit -f .
git submodule update --init --recursive
```

What’s happening:

- `git submodule deinit -f .` forcefully removes all submodule registrations from `.git/config` and clears working directories
- `git submodule update --init --recursive` reinitializes every submodule and checks out the exact commit pinned in your parent repository

The `-f` flag is necessary if submodules have uncommitted changes. Without it, Git will refuse to deinit and ask you to clean up first.

This approach is best when submodules are in a genuinely broken state—refs you can’t reason about, corrupted metadata, or you just want a guaranteed clean checkout.

## The update-only method

If you want to preserve your submodule state metadata and just reset working directories to their pinned commits:

``` bash
git submodule update --recursive --force
```

This skips reinitialization. It:

- Respects existing submodule configurations in `.git/config`
- Discards local changes in each submodule working directory
- Checks out the exact commit your parent repo expects

Use this when submodules are registered correctly but their working directories are dirty or on the wrong commit.

## Preserving local work

If you have uncommitted changes in a submodule that you need to keep, handle it before resetting:

``` bash
cd path/to/submodule
git stash
cd ../..
git submodule update --recursive
```

Or if the work should be committed:

``` bash
cd path/to/submodule
git add .
git commit -m "Work in progress"
cd ../..
git submodule deinit -f .
git submodule update --init --recursive
```

## Alternative: sparse checkout or subtrees

Submodules remain useful, but consider these patterns depending on your needs:

**Git subtree** — Embeds dependency history directly into your repository. No detached HEAD concerns, but larger repository size and trickier merges:

``` bash
git subtree add --prefix path/to/dep https://github.com/user/repo.git branch
```

**Monorepo** — Keep all related code in a single repository. Eliminates the coordination problem entirely but requires more discipline on access control.

**Package managers** — For true dependencies (libraries, frameworks, tools), let npm, pip, conan, or language-native package managers handle versioning. Reserve submodules for tightly coupled codebases you control.

## Checking submodule status

Before resetting, see what state you’re in:

``` bash
git submodule status
```

This shows commit hashes, whether submodules are at their pinned commits, and any prefix indicators:

- `-` means not initialized
- `+` means uncommitted changes
- `U` means merge conflict

You can also check individual submodule configuration:

``` bash
git config --file .gitmodules -l
```

This lists all submodule URLs and paths, helpful for debugging missing or misconfigured entries.

## 2026 Best Practices and Advanced Techniques

For How to Reset All Git Submodules, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
