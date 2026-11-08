---
title: "Migrating a Git Repository from Google Code to GitHub"
date: 2018-03-24 11:41:48 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-import-a-googlecode-git-project-to-github-project/
---

Google Code was shut down in 2016, but you might still need to migrate legacy projects that were hosted there. If you have a local Git repository from Google Code or an archived mirror, here’s how to push it to GitHub while preserving all history.

## Prerequisites

- A GitHub account and a new empty repository created
- Git installed locally
- Access to the original repository (either live or as a local clone)

## Migration Steps

### 1. Clone the original repository

If the Google Code repository is still accessible via Git:

``` bash
git clone https://code.google.com/p/project-name.git
cd project-name
```

If Google Code is no longer available, you’ll need to work from a local copy or archived mirror you already have.

### 2. Create a new repository on GitHub

Go to GitHub and create a new empty repository. Don’t initialize it with a README, .gitignore, or license — you want it completely empty to avoid merge conflicts.

### 3. Update the remote URL

Change the remote origin from the old Google Code URL to your new GitHub repository:

``` bash
git remote set-url origin https://github.com/username/repo-name.git
```

Verify the change:

``` bash
git remote -v
```

You should see output like:

    origin  https://github.com/username/repo-name.git (fetch)
    origin  https://github.com/username/repo-name.git (push)

### 4. Push all branches and tags

Push the entire repository history to GitHub:

``` bash
git push -u origin --all
git push -u origin --tags
```

The `--all` flag pushes all local branches, and the `--tags` flag ensures all Git tags are transferred. The `-u` flag sets the upstream tracking.

## Using SSH Instead of HTTPS

For better security and to avoid entering credentials repeatedly, use SSH:

``` bash
git remote set-url origin git@github.com:username/repo-name.git
git push -u origin --all
git push -u origin --tags
```

Make sure you have SSH keys configured in GitHub first.

## Verifying the Migration

After pushing, verify everything transferred correctly:

``` bash
git log --oneline | head -20
git branch -a
git tag | head -20
```

Compare the commit count and tags on GitHub with your local repository to ensure nothing was lost.

## Handling Large Repositories

If the repository is very large (over 1 GB), GitHub may reject the push. In that case:

1.  Increase the HTTP post buffer:

    ``` bash
    git config http.postBuffer 524288000
    ```

2.  Use a shallower clone if you don’t need full history:

    ``` bash
    git clone --depth=1000 https://code.google.com/p/project-name.git
    ```

3.  Consider using `git-lfs` for large binary files.

## Common Issues

**Authentication failures**: Use SSH keys instead of HTTPS, or generate a personal access token on GitHub for HTTPS authentication.

**Refusing to merge unrelated histories**: If you’re combining repos, add the `--allow-unrelated-histories` flag to your merge command.

**Missing commits or branches**: Ensure you used `git push --all` rather than just `git push`, which only pushes the current branch by default.

## 2026 Best Practices and Advanced Techniques

For Migrating a Git Repository from Google Code to GitHub, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
