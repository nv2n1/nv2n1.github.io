---
title: "Generating TAGS Files Recursively for Emacs Projects"
date: 2018-03-24 08:22:50 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/generating-tags-file-for-emacs-recursively/
---

The built-in etags command doesn’t recursively traverse directories by default, but generating TAGS files across your entire project is straightforward with the right tools and setup.

## Using ctags (Recommended)

The simplest approach is ctags with the `-e` flag, which generates Emacs-compatible TAGS files:

``` bash
ctags -e -R .
```

The `-R` flag enables recursive traversal. This works reliably across most projects and outperforms alternatives in speed.

To exclude common directories (build artifacts, dependencies, version control):

``` bash
ctags -e -R --exclude=.git --exclude=node_modules --exclude=.venv .
```

For persistent exclusion rules across projects, create a `.ctags.d/` configuration directory. Add a file like `.ctags.d/project.ctags`:

    --exclude=.git
    --exclude=node_modules
    --exclude=.venv
    --exclude=__pycache__
    --exclude=.pytest_cache
    --exclude=build
    --exclude=dist
    --exclude=.mypy_cache
    --exclude=.coverage

Then run ctags without repeating exclusions:

``` bash
ctags -e -R .
```

You can also use language-specific filtering to reduce file clutter. For a Python project:

``` bash
ctags -e -R --languages=Python .
```

## Using etags with find

If you’re restricted to the standard etags command, combine it with find:

``` bash
find . -type f \( -name "*.py" -o -name "*.js" -o -name "*.c" \) ! -path "*/node_modules/*" ! -path "*/.git/*" | xargs etags -
```

The `-` at the end tells etags to read filenames from stdin. This approach gives fine-grained control over which files to index.

For deeper control, exclude directories first:

``` bash
find . -type f -name "*.py" ! -path "*/build/*" ! -path "*/.venv/*" ! -path "*/__pycache__/*" | xargs etags -
```

## Configuring Emacs to Use TAGS

After generating the TAGS file, tell Emacs where to find it. Add this to your Emacs configuration:

```elisp
(setq tags-file-name "/path/to/your/project/TAGS")
```

Or use `M-x visit-tags-table` interactively to select it.

For multiple projects, configure Emacs to search through several TAGS files:

```elisp
(setq tags-table-list '("/project1/TAGS" "/project2/TAGS" "/project3/TAGS"))
```

Use `M-.` to jump to a tag definition and `M-*` to jump back. You can also use `C-u M-.` to search all loaded TAGS files.

## Automating TAGS Generation

For active development, regenerate TAGS automatically using a Git hook. Create `.git/hooks/post-commit`:

``` bash
#!/bin/bash
# .git/hooks/post-commit
ctags -e -R --exclude=.git .
```

Make it executable:

``` bash
chmod +x .git/hooks/post-commit
```

This regenerates tags after every commit, keeping them in sync with your code.

Alternatively, use a Makefile target:

``` makefile
.PHONY: tags
tags:
    ctags -e -R --exclude=.git --exclude=node_modules .
```

Run `make tags` before major development sessions or add it to your CI pipeline.

For watch-based regeneration during development, use `entr`:

``` bash
find . -type f -name "*.py" -o -name "*.js" | entr ctags -e -R .
```

This automatically regenerates TAGS whenever source files change.

## Modern Alternative: LSP with eglot

Emacs 29+ includes eglot, a built-in Language Server Protocol client that provides superior symbol navigation without maintaining TAGS files:

```elisp
(use-package eglot
  :hook ((python-mode . eglot-ensure)
         (js-mode . eglot-ensure)
         (go-mode . eglot-ensure)))
```

LSP handles symbol definitions dynamically, provides real-time diagnostics, and scales better with large codebases. However, TAGS files remain useful for offline work, legacy projects, or when LSP servers aren’t available for your language.

For hybrid workflows, keep TAGS generation but use eglot as your primary navigation tool. The two approaches coexist without conflict.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Generating TAGS Files Recursively for Emacs Projects with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Generating TAGS Files Recursively for Emacs Projects. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
