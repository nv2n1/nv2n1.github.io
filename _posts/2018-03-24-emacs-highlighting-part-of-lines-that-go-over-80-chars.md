---
title: "Highlight Long Lines in Emacs"
date: 2018-03-24 11:40:40 +0000
layout: post
canonical: https://www.systutorials.com/emacs-highlighting-part-of-lines-that-go-over-80-chars/
---

The most straightforward approach is `whitespace-mode`, which provides built-in visual feedback for lines exceeding a specified column width.

Add this to your Emacs configuration:

```elisp
(require 'whitespace)
(setq whitespace-style '(face empty tabs lines-tail trailing))
(setq whitespace-line-column 80)
(global-whitespace-mode t)
```

The `lines-tail` style highlights only the portion of the line exceeding `whitespace-line-column`, which is less visually intrusive than highlighting the entire line and keeps focus on the actual problem.

Customize the appearance by setting a face:

```elisp
(set-face-attribute 'whitespace-line nil
                    :background "#3a3a3a"
                    :foreground "#a8a8a8")
```

## Selective enablement per mode

Enable `whitespace-mode` only for specific major modes rather than globally:

```elisp
(require 'whitespace)
(setq whitespace-style '(face empty tabs lines-tail trailing))
(setq whitespace-line-column 80)

(add-hook 'python-mode-hook 'whitespace-mode)
(add-hook 'emacs-lisp-mode-hook 'whitespace-mode)
(add-hook 'sh-mode-hook 'whitespace-mode)
(add-hook 'c-mode-hook 'whitespace-mode)
```

Toggle interactively with `M-x whitespace-mode` or `M-x whitespace-toggle-options` for temporary checks without persistent configuration.

## Subtle visual indicator: display-fill-column-indicator

If you prefer minimal visual clutter, use `display-fill-column-indicator` (available since Emacs 27):

```elisp
(setq-default display-fill-column-indicator-column 80)
(global-display-fill-column-indicator-mode t)
```

This draws a subtle vertical line at column 80. Customize the character and color:

```elisp
(setq display-fill-column-indicator-character ?┃)
(set-face-attribute 'fill-column-indicator nil
                    :foreground "#404040")
```

This approach shows the boundary without highlighting actual content violations, making it less distracting during normal editing.

## Pattern-based highlighting with highlight-lines-matching-regexp

For one-off checks or complex patterns, use the built-in `highlight-lines-matching-regexp`:

    M-x highlight-lines-matching-regexp RET .{81} RET

This matches any line with 81 or more characters. Remove highlighting with:

    M-x unhighlight-regexp RET

Bind it to a key for quick access:

```elisp
(global-set-key (kbd "C-c h l") 
                (lambda () (interactive)
                  (highlight-lines-matching-regexp ".{81}")))
```

## Comparison

| Method | Pros | Cons |
|----|----|----|
| `whitespace-mode` with `lines-tail` | Fine-grained, shows exactly what exceeds limit | Can look busy with other whitespace visualization |
| `display-fill-column-indicator` | Subtle, doesn’t highlight content, minimal distraction | Doesn’t highlight violations, only shows boundary |
| `highlight-lines-matching-regexp` | Flexible regex patterns, good for temporary use | Requires manual activation each session |

## Choosing the right approach

**For strict enforcement:** Use `whitespace-mode` with `lines-tail` if you want immediate visual feedback on violations and enforce line length consistently across your team.

**For guidelines:** Use `display-fill-column-indicator` if you prefer a visual guide that allows flexibility and doesn’t distract with highlighting.

**For temporary checks:** Use `highlight-lines-matching-regexp` when auditing existing code or testing specific patterns without modifying your permanent configuration.

Most development teams benefit from combining approaches—use the fill column indicator as a constant visual guide with `whitespace-mode` enabled selectively in languages with strict line limits (Python, Go, shell scripts).

## Essential Editor Configuration

A well-configured editor dramatically improves productivity. For Vim users, invest time in crafting a solid vimrc. For Emacs users, use use-package for cleaner configuration management. Both editors support extensive plugin ecosystems that can transform them into full IDEs.

Learn the navigation commands thoroughly before adding plugins. Mastery of core movement commands (word, paragraph, search motions in Vim; mark, isearch, ace-jump in Emacs) provides more productivity gains than any single plugin.

## Performance Tips

Large files can slow down both editors. For Vim, set lazyredraw and disable syntax highlighting for files over a certain size. For Emacs, use so-long-mode for files with long lines. Both editors benefit from disabling line numbers on very large files to improve scrolling performance.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
