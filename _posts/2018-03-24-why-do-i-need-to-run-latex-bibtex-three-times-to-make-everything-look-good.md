---
title: "Why You Need to Run LaTeX and BibTeX Multiple Times"
date: 2018-03-24 11:54:37 +0000
author: "Weiwei Jia"
layout: post
categories: [programming-languages]
canonical: /why-do-i-need-to-run-latex-bibtex-three-times-to-make-everything-look-good/
---

The classic LaTeX workflow requires running pdflatex multiple times with BibTeX in between:

``` bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

This seems redundant, but there’s a solid reason for it.

## How the Three-Pass Workflow Works

**First LaTeX pass:** LaTeX processes your document and writes all `\cite{}` commands to the `.aux` file. At this point, it doesn’t know what labels those citations should have—it just records that citations exist.

**BibTeX pass:** BibTeX reads the `.aux` file to see which bibliography entries are cited. It pulls those entries from your `.bib` file, sorts them (alphabetically, by appearance, or by a custom order depending on your style), and writes formatted entries to the `.bbl` file.

**Second LaTeX pass:** LaTeX includes the `.bbl` file and now knows what label each citation should get (e.g., `[1]`, `[Smith2024]`). It writes these correct labels back to the `.aux` file. However, your document still has placeholder numbers from the first pass.

**Third LaTeX pass:** LaTeX reads the correct labels from `.aux` and inserts them into the final document. Cross-references and page numbers now stabilize.

## Why This Design?

This multi-pass requirement comes from constraints that mattered in 1980s computing: limited memory and slow file I/O. You can’t reliably read and write the same file in a single pass, especially when dealing with forward references and the complexity of collecting, sorting, and formatting bibliography data.

## Modern Alternatives

If you’re tired of running LaTeX three times, consider switching to **biblatex** with **Biber**:

``` bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

While this still requires multiple passes, `biblatex` with `biber` is more robust and handles Unicode better. The real advantage is flexibility—you can configure citation styles directly in your preamble rather than relying on `.bst` files.

For an even smoother workflow, use `latexmk`:

``` bash
latexmk -pdf main.tex
```

`latexmk` automatically determines how many passes are needed and runs them for you. It watches for changes in your `.aux` and `.bbl` files and stops once everything stabilizes. This is the standard approach in 2026—it handles the complexity invisibly.

## Stabilization During Development

During document preparation, you’ll recompile many times anyway. Your citations and cross-references stabilize naturally as you edit. The three-pass requirement only matters if you’re creating a final PDF from scratch—and even then, `latexmk` removes the burden of thinking about it.

## When You Might Still See Instability

Sometimes you’ll see warnings about undefined references or changed citations after multiple passes. This typically happens when:

- You add new citations without running BibTeX
- Your `.bib` file has malformed entries
- You’re using complex cross-referencing packages like `hyperref` or `cleveref`

In these cases, a full clean rebuild helps:

``` bash
latexmk -pdf -C main.tex  # Clean previous artifacts
latexmk -pdf main.tex     # Rebuild completely
```

If you’re using an editor like VS Code with LaTeX Workshop or TeXShop on macOS, these tools often call `latexmk` under the hood, so you never see the individual passes. Just save your file and the tool handles the rest.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Why You Need to Run LaTeX and BibTeX Multiple Times with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Why You Need to Run LaTeX and BibTeX Multiple Times. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
