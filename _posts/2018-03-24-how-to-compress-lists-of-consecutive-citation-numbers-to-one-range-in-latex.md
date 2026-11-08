---
title: "Compressing Consecutive Citation Numbers in LaTeX"
date: 2018-03-24 11:40:26 +0000
modified: 2026-04-12 16:54:15 +0000
author: "Eric Ma"
layout: post
categories: [testing-devops]
canonical: /how-to-compress-lists-of-consecutive-citation-numbers-to-one-range-in-latex/
---

When you have multiple consecutive citations like \[14\], \[15\], \[16\], \[17\], \[19\], LaTeX renders them individually by default, wasting space. Citation management packages automatically compress these to \[14–17\], \[19\], which is standard practice for numerical citation styles.

## Using the cite Package

The `cite` package is the simplest approach. Add it to your preamble:

``` latex
\usepackage{cite}
```

When you cite multiple references:

``` latex
Some research shows this\cite{paper14,paper15,paper16,paper17,paper19}.
```

The output becomes \[14–17\], \[19\] instead of individual citations. The package automatically sorts citations numerically and compresses consecutive sequences, regardless of the order you list them in your `\cite` command.

The `cite` package handles:

- Sorting citations in numerical order
- Detecting and compressing consecutive sequences
- Formatting ranges with en-dashes (–)
- Processing unsorted citation lists internally

## Using natbib for Additional Features

If you need author-year citations or more control over formatting, `natbib` provides similar compression:

``` latex
\usepackage[sort&compress]{natbib}
```

The `sort&compress` option enables both sorting and compression. This is useful when you’re already using `natbib` for mixed citation styles:

``` latex
\citet{paper1,paper2,paper3}      % Author (Year) format
\citep{paper1,paper2,paper3}      % (Author, Year) format
```

With `sort&compress`, both parenthetical and textual citations compress consecutive numbers appropriately.

## Using biblatex (Modern Standard)

For new projects, `biblatex` with Biber is the recommended approach:

``` latex
\usepackage[
  backend=biber,
  style=numeric,
  sortcites=true,
  maxbibnames=99
]{biblatex}

\addbibresource{references.bib}
```

Enable `sortcites=true` for citation compression. Place `\printbibliography` at the end of your document.

Advantages of biblatex:

- Extensive customization of citation formatting
- Full Unicode support
- More flexible sorting and filtering options
- Clean separation between bibliography style and content
- Better handling of complex multilingual bibliographies

## Key Configuration Considerations

**Numeric styles only**: Citation compression works reliably only with numeric citation styles (`numeric`, `numeric-comp`, `numeric-verb`). Alphabetic and author-year styles don’t benefit from range compression since the citation labels aren’t inherently sequential.

**Minimum range length**: Most packages only compress ranges of three or more consecutive citations. For example, \[5\], \[6\], \[7\] becomes \[5–7\], but \[5\], \[6\], \[8\] might render as \[5–6\], \[8\] depending on configuration.

**Backend choice**:

- `cite` and `natbib` use BibTeX by default
- `biblatex` uses Biber (more robust for complex bibliographies)
- Biber handles UTF-8 better and offers more advanced sorting options

**Package conflicts**: Don’t load `cite` and `natbib` together—they conflict. Choose one approach and stick with it.

## Complete Working Example

``` latex
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{cite}

\begin{document}

According to multiple studies\cite{ref1,ref2,ref3,ref5,ref6}, 
this finding is well established.

\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

Compile with:

``` bash
pdflatex document.tex
bibtex document.aux
pdflatex document.tex
pdflatex document.tex
```

## Customizing Compression Behavior

With `biblatex`, you can fine-tune compression:

``` latex
\usepackage[
  backend=biber,
  style=numeric-comp,
  mincitenames=3
]{biblatex}
```

The `numeric-comp` style specifically compresses three or more citations. Some users prefer `numeric-verb` for verbose output or adjust `mincitenames` to control which citations appear in compressed form.

## Troubleshooting

If citations aren’t compressing:

- Verify your package options are correct
- Ensure you’re using a numeric citation style
- Rebuild the bibliography cache: delete `.aux`, `.bbl`, and `.bcf` files, then recompile
- Check that your bibliography entries exist in your `.bib` file

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Compressing Consecutive Citation Numbers in LaTeX with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Compressing Consecutive Citation Numbers in LaTeX. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
