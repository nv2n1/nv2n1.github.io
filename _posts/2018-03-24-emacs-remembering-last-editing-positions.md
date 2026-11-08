---
title: "Restore Cursor Position in Emacs with save-place-mode"
date: 2018-03-24 11:41:26 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /emacs-remembering-last-editing-positions/
---

Emacs doesn’t restore your cursor to the last editing position by default—Vim does this out of the box. Fortunately, `save-place-mode` is built into Emacs and requires minimal configuration to enable this behavior.

## Basic Setup

Add this to your `~/.emacs.d/init.el`:

```elisp
(save-place-mode 1)
```

That’s all you need. The mode automatically saves your cursor position when you close a file and restores it the next time you visit that file. Position data is stored in `~/.emacs.d/places` by default.

If you want to customize the storage location:

```elisp
(setq save-place-file "~/.emacs.d/saveplace")
(save-place-mode 1)
```

## Configuration with use-package

If you’re using `use-package` for package management:

```elisp
(use-package saveplace
  :ensure t
  :init
  (save-place-mode 1)
  :custom
  (save-place-file "~/.emacs.d/saveplace")
  (save-place-limit 500))
```

## Excluding Files and Directories

By default, `save-place-mode` saves positions for most files. You can exclude specific files using regex patterns:

```elisp
(setq save-place-ignore-files-regexp
      "\\(?:COMMIT_EDITMSG\\|hg-editor-[0-9a-z]+\\.txt\\|svn-commitmessage\\.[0-9a-z]+\\)")
```

This excludes commit message files from version control systems, which is useful since you typically don’t need to return to the same position in a commit message.

You can also limit the total number of positions remembered:

```elisp
(setq save-place-limit 500)  ;; Default is nil (unlimited)
```

## Dired Buffer Positions

By default, `save-place-mode` doesn’t save scroll positions in Dired buffers. Enable this with:

```elisp
(setq save-place-dired-regexp "\\`/")  ;; Save positions for all dired buffers
```

This is helpful if you frequently navigate deep directory structures and want to return to the same scroll position when revisiting a directory.

## Combining with Other Restoration Features

### Session Management

For more comprehensive session restoration, combine `save-place-mode` with `desktop-save-mode` to restore entire sessions including multiple buffers and their states:

```elisp
(save-place-mode 1)
(desktop-save-mode 1)
```

Be aware that `desktop-mode` can slow startup if you have many buffers open. You can control this behavior with:

```elisp
(setq desktop-restore-frames nil)  ;; Don't restore window frames
(setq desktop-restore-eager 5)     ;; Restore only 5 buffers on startup
```

### Window Layout Restoration

Combine `save-place-mode` with `winner-mode` to restore both buffer positions and window layouts:

```elisp
(save-place-mode 1)
(winner-mode 1)  ;; Use C-c C-/ to undo window configs, C-c C-? to redo
```

### Recent Files Integration

`save-place-mode` integrates seamlessly with `recentf-mode`. If you’re using `recentf` to track recently opened files, saved positions will be restored automatically:

```elisp
(recentf-mode 1)
(save-place-mode 1)
```

## Troubleshooting

If positions aren’t being restored, verify the mode is enabled:

```elisp
(message "save-place-mode: %s" (if save-place-mode "enabled" "disabled"))
```

Check that the `~/.emacs.d/places` file exists and is readable:

``` bash
ls -la ~/.emacs.d/places
```

If the file doesn’t exist after closing a buffer, it will be created automatically on the next kill.

Narrowed buffers will correctly restore to their position within the narrowed range, so you don’t need special handling for those cases.

Clear the saved positions if you want to start fresh:

``` bash
rm ~/.emacs.d/places
```

## 2026 Best Practices and Advanced Techniques

For Restore Cursor Position in Emacs with save-place-mode, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
