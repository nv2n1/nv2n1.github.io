---
title: "UTop Keyboard Shortcuts and Keybindings"
date: 2018-03-24 08:19:32 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/utop-key-bindings-key-shortcuts/
---

utop is an improved OCaml REPL with line editing, history, context-sensitive completion, and syntax highlighting. While powerful, its key bindings differ from standard GNU readline, which can be jarring if you’re used to standard shell behavior.

## Getting the key bindings list

The simplest way to see all available bindings is to run the `#utop_bindings` directive in utop:

``` ocaml
#utop_bindings;;
```

This will output the complete binding table with descriptions. Here’s a reference of the most commonly used bindings:

## Essential navigation

| Key                | Action    | Notes                                      |
|--------------------|-----------|--------------------------------------------|
| `Ctrl-A`           | goto-bol  | Jump to beginning of line                  |
| `Ctrl-E`           | goto-eol  | Jump to end of line                        |
| `Ctrl-F` / `→`     | next-char | Move right one character                   |
| `Ctrl-B` / `←`     | prev-char | Move left one character                    |
| `Alt-F` / `Ctrl-→` | next-word | Move to end of next word                   |
| `Alt-B` / `Ctrl-←` | prev-word | Move to beginning of previous word         |
| `Home`             | goto-bot  | Jump to line start (alternative to Ctrl-A) |
| `End`              | goto-eot  | Jump to line end (alternative to Ctrl-E)   |

## History navigation

| Key               | Action                        |
|-------------------|-------------------------------|
| `↑` / `Ctrl-P`    | history-prev                  |
| `↓` / `Ctrl-N`    | history-next                  |
| `Ctrl-R`          | prev-search                   |
| `Alt-P` / `Alt-N` | Alternative history prev/next |

## Editing and deletion

| Key | Action | Notes |
|----|----|----|
| `Backspace` / `Ctrl-H` | delete-prev-char | Delete character before cursor |
| `Delete` | delete-next-char | Delete character after cursor |
| `Ctrl-U` | kill-prev-line | Delete from cursor to line start |
| `Ctrl-K` | kill-next-line | Delete from cursor to line end |
| `Alt-Backspace` / `Alt-Delete` | kill-prev-word | Delete word before cursor |
| `Alt-D` | kill-next-word | Delete word after cursor |
| `Ctrl-W` | kill | Delete current selection |
| `Ctrl-_` / `Ctrl-/` | undo | Undo last change |

## Completion

| Key | Action | Notes |
|----|----|----|
| `Tab` | complete | Standard completion (inline) |
| `Alt-Tab` | complete-bar | Show completion menu |
| `Alt-↑` | complete-bar | Alternative to Alt-Tab |
| `Alt-←` / `Alt-→` | complete-bar-prev/next | Navigate completion menu |
| `Alt-Home` / `Alt-End` | complete-bar-first/last | Jump to start/end of completions |

## Copy and paste

| Key          | Action   |
|--------------|----------|
| `Ctrl-Space` | set-mark |
| `Alt-W`      | copy     |
| `Ctrl-Y`     | yank     |

## Other useful bindings

| Key | Action | Notes |
|----|----|----|
| `Ctrl-L` | clear-screen | Clear the screen |
| `Ctrl-C` | break | Cancel current input |
| `Ctrl-D` | interrupt-or-delete-next-char | Exit if at empty prompt, otherwise delete |
| `Ctrl-Z` | suspend | Suspend the session |
| `Alt-Enter` | newline | Insert literal newline without executing |
| `Insert` | switch-erase-mode | Toggle between insert and overwrite modes |

## Macros

utop supports recording and replaying command macros:

| Key                    | Action               |
|------------------------|----------------------|
| `Ctrl-X (`             | start-macro          |
| `Ctrl-X )`             | stop-macro           |
| `Ctrl-X E`             | play-macro           |
| `Ctrl-X Ctrl-K Tab`    | insert-macro-counter |
| `Ctrl-X Ctrl-K Ctrl-A` | add-macro-counter    |
| `Ctrl-X Ctrl-K Ctrl-C` | set-macro-counter    |

## Practical tips

**Multi-line input**: If you need to enter multi-line expressions, use `Alt-Enter` to insert newlines without executing. This is particularly useful for let-bindings and function definitions that span multiple lines.

**Search mode**: Use `Ctrl-R` to search your history backward. Keep typing to narrow results, or press `Ctrl-R` again to find the next match. Press `Escape` to exit search mode.

**Customizing bindings**: You can customize utop’s key bindings by editing the configuration file at `~/.config/utop/utoprc`. Create this file if it doesn’t exist. The syntax uses the same key binding format as Lambda Term (the underlying terminal library).

Example customization to add a common Emacs-style binding:

    [binding]
    key = "C-s"
    command = "next-search"

**Word vs character navigation**: Note that `Alt-F` and `Alt-B` consider word boundaries differently than bash. A “word” in utop is any sequence of alphanumeric characters and underscores, which matters when editing OCaml identifiers.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers UTop Keyboard Shortcuts and Keybindings with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for UTop Keyboard Shortcuts and Keybindings. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
