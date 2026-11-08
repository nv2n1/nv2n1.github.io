---
title: "Display Line Numbers Separately from Text in Emacs"
date: 2018-03-24 08:21:05 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-add-a-space-between-the-line-numbers-and-text-content-in-emacs/
---

Line number displays in Emacs can feel cramped without proper spacing. Modern Emacs provides built-in control over line number formatting and width—no external packages needed.

## Using display-line-numbers-mode

`display-line-numbers-mode` is the standard in Emacs 25+ and should be your default choice. It’s faster and more maintainable than the older `linum-mode`.

Enable it globally:

```elisp
(global-display-line-numbers-mode t)
```

To add spacing between line numbers and text, set an explicit width:

```elisp
(setq display-line-numbers-width 4)
```

This allocates a 4-character space for line numbers plus padding. Adjust the number based on your file size and preference. For files with 100+ lines, use 4 or 5. For smaller files, 3 works fine.

Alternatively, let Emacs calculate width dynamically based on your file’s total line count:

```elisp
(setq display-line-numbers-width-start t)
```

This is useful if you want automatic adjustment without manual tuning.

## Control line number appearance

Customize how line numbers look using the `line-number` and `line-number-current-line` faces:

```elisp
(custom-set-faces
 '(line-number ((t (:foreground "#555555" :background "#f5f5f5"))))
 '(line-number-current-line ((t (:foreground "#000000" :background "#ffffff" :weight bold)))))
```

The current line number stands out with bold text and contrasting background.

## Enable line numbers selectively

You don’t always need line numbers everywhere. Hook into specific modes:

```elisp
(add-hook 'prog-mode-hook #'display-line-numbers-mode)
(add-hook 'text-mode-hook #'display-line-numbers-mode)
```

To disable in specific modes:

```elisp
(add-hook 'org-mode-hook (lambda () (display-line-numbers-mode -1)))
```

## Visual vs. absolute line numbers

By default, `display-line-numbers-mode` shows absolute line numbers. To count wrapped lines instead:

```elisp
(setq display-line-numbers-type 'visual)
```

Use `'relative'` for relative numbering (useful with evil-mode or vim keybindings):

```elisp
(setq display-line-numbers-type 'relative)
```

## Legacy linum-mode

If you’re on older Emacs or must use `linum-mode`, customize the format string:

```elisp
(require 'linum)
(global-linum-mode t)

(setq linum-format (lambda (line)
  (let ((w (length (number-to-string (count-lines (point-min) (point-max))))))
    (propertize (format (concat "%" (number-to-string w) "d ") line)
                'face 'linum))))
```

The space after `d` adds padding. Use two spaces for more breathing room:

```elisp
(setq linum-format (lambda (line)
  (let ((w (length (number-to-string (count-lines (point-min) (point-max))))))
    (propertize (format (concat "%" (number-to-string w) "d  ") line)
                'face 'linum))))
```

Note: `linum-mode` recalculates on every buffer change and is noticeably slower on large files (10,000+ lines). Avoid it if possible.

## Apply changes

Evaluate your configuration with `M-x eval-buffer` or restart Emacs. Test with different `display-line-numbers-width` values to find your preferred spacing.

## Essential Editor Configuration

A well-configured editor dramatically improves productivity. For Vim users, invest time in crafting a solid vimrc. For Emacs users, use use-package for cleaner configuration management. Both editors support extensive plugin ecosystems that can transform them into full IDEs.

Learn the navigation commands thoroughly before adding plugins. Mastery of core movement commands (word, paragraph, search motions in Vim; mark, isearch, ace-jump in Emacs) provides more productivity gains than any single plugin.

## Performance Tips

Large files can slow down both editors. For Vim, set lazyredraw and disable syntax highlighting for files over a certain size. For Emacs, use so-long-mode for files with long lines. Both editors benefit from disabling line numbers on very large files to improve scrolling performance.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
