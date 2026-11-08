---
title: "Convert Line Endings Between DOS and Unix in Emacs"
date: 2018-03-24 11:40:31 +0000
layout: post
canonical: https://www.systutorials.com/how-to-convert-between-dos-and-unix-file-coding-in-emacs/
---

Emacs handles line ending conversions through its buffer coding system. Whether you’re converting CRLF (DOS/Windows) to LF (Unix) or the reverse, the process is straightforward.

## DOS to Unix (CRLF to LF)

Open the file in Emacs and run:

    M-x set-buffer-file-coding-system RET undecided-unix

Or use the keyboard shortcut:

    C-x RET f undecided-unix

Then save the file:

    C-x C-s

The `undecided-unix` coding system strips carriage returns and normalizes to Unix line endings (LF only).

## Unix to DOS (LF to CRLF)

For the reverse operation:

    M-x set-buffer-file-coding-system RET undecided-dos

Or the shortcut:

    C-x RET f undecided-dos

Save with `C-x C-s`.

## Check Current Line Endings

Verify which line ending style a file uses by checking the mode line at the bottom of the Emacs window. The coding system appears in parentheses:

- `(Unix)` — LF line endings
- `(DOS)` — CRLF line endings
- `(Mac)` — CR-only endings (legacy, rarely seen)

You can also query the coding system interactively:

    M-x describe-current-coding-system

## Batch Convert Multiple Files

For converting multiple files at once, use command-line utilities instead of opening each file in Emacs.

With `dos2unix`:

``` bash
dos2unix file1.txt file2.txt file3.txt
unix2dos file1.txt file2.txt file3.txt
```

With `sed`:

``` bash
sed -i 's/\r$//' file.txt      # DOS to Unix
sed -i 's/$/\r/' file.txt      # Unix to DOS
```

With `perl`:

``` bash
perl -pi -e 's/\r\n/\n/g' file.txt   # DOS to Unix
perl -pi -e 's/\n/\r\n/g' file.txt   # Unix to DOS
```

With `tr`:

``` bash
tr -d '\r' < file.txt > file.txt.tmp && mv file.txt.tmp file.txt   # DOS to Unix
```

## Prevent Mixed Line Endings in Projects

Configure your project’s `.gitattributes` to enforce consistent line endings across team members:

    * text=auto
    *.txt text eol=lf
    *.sh text eol=lf
    *.bat text eol=crlf
    *.ps1 text eol=crlf

The `text=auto` setting lets Git detect text files automatically. Specific rules override it — `.sh` files always use LF, `.bat` and PowerShell scripts use CRLF. This prevents line ending issues in version control regardless of each developer’s OS.

## Configure Emacs for Consistent Defaults

To default new files to UTF-8 with Unix line endings, add this to your `~/.config/emacs/init.el` (or `~/.emacs` for older setups):

```elisp
(setq buffer-file-coding-system 'utf-8-unix)
(setq default-buffer-file-coding-system 'utf-8-unix)
```

For projects that need DOS line endings by default:

```elisp
(setq buffer-file-coding-system 'utf-8-dos)
```

You can also set coding per-mode or per-directory using `.dir-locals.el`:

```elisp
((sh-mode . ((buffer-file-coding-system . utf-8-unix)))
 (batch-mode . ((buffer-file-coding-system . utf-8-dos))))
```

## Handle Mixed Encodings and Line Endings

If you work with files that have mixed UTF-8/UTF-16 or inconsistent line endings, Emacs can detect and convert them. When opening a file, use:

    M-x set-file-coding-system

Emacs will display available coding systems. Most common options:

- `utf-8-unix` — UTF-8 with LF
- `utf-8-dos` — UTF-8 with CRLF
- `utf-16-le` — UTF-16 little-endian
- `iso-8859-1` — Latin-1

After converting, save with `C-x C-s`.

## 2026 Best Practices and Advanced Techniques

For Convert Line Endings Between DOS and Unix in Emacs, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
