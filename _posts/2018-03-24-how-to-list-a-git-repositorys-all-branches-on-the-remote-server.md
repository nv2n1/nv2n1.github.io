---
title: "How to List All Remote Branches in Git"
date: 2018-03-24 08:16:32 +0000
modified: 2026-04-12 16:57:34 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-list-a-git-repositorys-all-branches-on-the-remote-server/
---

### Local branches

List all branches on your local repository:

``` bash
git branch
```

This shows only branches that exist locally on your machine.

### Remote branches

To list all branches on the remote server, use the `-r` flag:

``` bash
git branch -r
```

This displays remote-tracking branches — local references to branches that exist on the remote repository. These are read-only pointers that track the state of branches on the remote.

### All branches (local and remote)

To see both local and remote branches together:

``` bash
git branch -a
```

The output distinguishes between them:

- Local branches appear without a prefix
- Remote branches appear with the remote name prefix (typically `origin/`)

### More detailed branch information

For additional details about branches, including tracking relationships and last commit info:

``` bash
git branch -vv
```

This shows:

- Local branch names
- Commit hash and message
- Which remote branch each local branch is tracking (if any)

### Listing only remote branches with more detail

If you want to see remote branches with their last commit information:

``` bash
git branch -rv
```

Or get the same information from the remote without storing local tracking branches:

``` bash
git ls-remote --heads origin
```

This queries the remote directly and shows all branch references without creating local tracking branches.

### Filtering branches

You can also use `git branch` with grep to filter results:

``` bash
git branch -r | grep feature
```

This is useful when working with repositories that have many branches.

### Common workflows

**Checking if a remote branch exists before fetching:**

``` bash
git branch -r | grep "origin/feature-xyz"
```

**Fetching a specific remote branch and creating a local tracking branch:**

``` bash
git checkout --track origin/feature-name
```

Or the shorthand (if the branch name is unique):

``` bash
git checkout feature-name
```

**Deleting a remote branch locally (not on the server):**

``` bash
git branch -dr origin/old-branch
```

This removes the local tracking branch but doesn’t affect the remote.

**See what’s on the remote without fetching:**

``` bash
git remote show origin
```

This displays detailed information about the remote, including all branches and their tracking status.

## Git Best Practices

When working with Git, follow these practices for a cleaner history:

- Write clear, descriptive commit messages that explain what changed and why
- Make small, focused commits rather than large sweeping changes
- Use branches for features and experiments, merge or rebase when ready
- Review changes with git diff before committing
- Use .gitignore to exclude build artifacts and environment files

## Useful Git Aliases

Speed up your workflow with these aliases in ~/.gitconfig:

```wp-block-code
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    lg = log --oneline --graph --decorate
    last = log -1 HEAD
    unstage = reset HEAD --
    amend = commit --amend --no-edit
```

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers How to List All Remote Branches in Git with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for How to List All Remote Branches in Git. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
