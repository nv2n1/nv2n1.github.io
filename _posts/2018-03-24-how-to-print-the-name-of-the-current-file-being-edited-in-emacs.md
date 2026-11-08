---
title: "Getting the Current File Path in Emacs"
date: 2018-03-24 11:40:27 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-print-the-name-of-the-current-file-being-edited-in-emacs/
---

To see the current file path immediately, use the Elisp evaluation prompt:

    M-: buffer-file-name

This displays the full path in the echo area. Alternatively, press `M-x`, type `eval-expression`, and enter `buffer-file-name`.

## In Elisp code

Reference `buffer-file-name` directly in your configuration or custom commands:

```elisp
(message "Editing: %s" buffer-file-name)
```

This prints to the echo area and logs to the `*Messages*` buffer for later review.

## Extract just the filename or directory

When you need components of the path:

```elisp
;; Filename only (without directory)
(file-name-nondirectory buffer-file-name)

;; Directory path only
(file-name-directory buffer-file-name)

;; Basename without extension
(file-name-sans-extension (file-name-nondirectory buffer-file-name))
```

## Display file path in the mode line

Add the file path persistently to your mode line:

```elisp
(setq-default mode-line-format
  '("%e" mode-line-mule-info mode-line-modified " "
    mode-line-buffer-identification " " buffer-file-name))
```

For a cleaner look, use only the filename:

```elisp
(setq-default mode-line-format
  '("%e" mode-line-mule-info mode-line-modified " "
    (:eval (file-name-nondirectory buffer-file-name))))
```

## Copy file path to clipboard

Create a command to copy the current file path:

```elisp
(defun copy-buffer-path ()
  "Copy the current buffer's file path to the clipboard."
  (interactive)
  (if buffer-file-name
      (progn
        (kill-new buffer-file-name)
        (message "Copied: %s" buffer-file-name))
    (message "Buffer has no associated file")))

(global-set-key (kbd "C-c C-l") 'copy-buffer-path)
```

For just the filename:

```elisp
(defun copy-buffer-filename ()
  "Copy just the filename to the clipboard."
  (interactive)
  (if buffer-file-name
      (let ((filename (file-name-nondirectory buffer-file-name)))
        (kill-new filename)
        (message "Copied: %s" filename))
    (message "Buffer has no associated file")))

(global-set-key (kbd "C-c C-f") 'copy-buffer-filename)
```

## Handle unsaved and non-file buffers

`buffer-file-name` returns `nil` for unsaved buffers, temporary buffers, and special buffers (like `*scratch*`). Always guard against this:

```elisp
(if buffer-file-name
    (message "File: %s" buffer-file-name)
  (message "Buffer is not associated with a file"))
```

Use this pattern in any function that depends on an actual file:

```elisp
(defun my-file-operation ()
  (interactive)
  (unless buffer-file-name
    (error "This buffer is not visiting a file"))
  ;; Safe to use buffer-file-name now
  (do-something-with buffer-file-name))
```

## Related variables and functions

- `buffer-name` — The name of the current buffer (independent of file association)
- `default-directory` — The working directory for the current buffer
- `default-file-name-coding-system` — Character encoding used for file paths
- `expand-file-name` — Convert relative paths to absolute paths
- `file-truename` — Resolve symlinks and get the true file path
- `locate-file` — Search for a file in a list of directories
- `dired-current-directory` — In Dired mode, the directory being browsed

## Example: Insert file path at cursor

```elisp
(defun insert-buffer-path-at-point ()
  "Insert the current file path at the cursor position."
  (interactive)
  (if buffer-file-name
      (insert buffer-file-name)
    (error "Buffer has no associated file")))
```

## Essential Editor Configuration

A well-configured editor dramatically improves productivity. For Vim users, invest time in crafting a solid vimrc. For Emacs users, use use-package for cleaner configuration management. Both editors support extensive plugin ecosystems that can transform them into full IDEs.

Learn the navigation commands thoroughly before adding plugins. Mastery of core movement commands (word, paragraph, search motions in Vim; mark, isearch, ace-jump in Emacs) provides more productivity gains than any single plugin.

## Performance Tips

Large files can slow down both editors. For Vim, set lazyredraw and disable syntax highlighting for files over a certain size. For Emacs, use so-long-mode for files with long lines. Both editors benefit from disabling line numbers on very large files to improve scrolling performance.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
