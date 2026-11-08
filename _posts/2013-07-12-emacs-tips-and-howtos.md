---
title: "Essential Emacs Tips and Workflows"
date: 2013-07-12 16:32:34 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /emacs-tips-and-howtos/
---

Emacs provides a built-in tutorial. Access it with:

    C-h t

For structured learning, the GNU Emacs Manual (built-in via `C-h i`) is the most authoritative resource. The Emacs Wiki also maintains community-driven guides and examples.

## Emacs configuration

Store your configuration in `~/.emacs.d/init.el` rather than the legacy `~/.emacs` file. This keeps your Emacs directory cleaner and is the modern standard. Example structure:

```elisp
;;; init.el --- Main Emacs configuration

;; Basic settings
(setq inhibit-startup-screen t)
(setq make-backup-files nil)

;; Load other configuration files
(load-file "~/.emacs.d/bindings.el")
(load-file "~/.emacs.d/development.el")
```

## Navigation and movement

### Jump to a specific line

    M-g M-g

Enter the line number and press `RET`.

### Navigate function definitions

Jump to the beginning or end of a function with:

    C-M-a   ; beginning-of-defun
    C-M-e   ; end-of-defun

This works across most programming modes.

### Move through parenthetical structures

Navigate balanced expressions and nested structures:

    C-M-f   ; forward-sexp
    C-M-b   ; backward-sexp
    C-M-d   ; down-list
    C-M-u   ; backward-up-list
    C-M-n   ; forward-list
    C-M-p   ; backward-list

Use `C-M-u` to jump out of nested parentheses, brackets, or braces.

### Position the screen

    C-l

Pressing it repeatedly cycles the current line between top, middle, and bottom of the window.

## Text editing operations

### Go to read-only files

Toggle a buffer’s read-only mode:

    C-x C-q

This allows you to edit read-only files if you have permission. After editing, save with `C-x C-s`.

### Remove Windows line endings (^M characters)

Convert CRLF to LF line endings:

    M-x replace-string RET C-q C-m RET RET

Alternatively, set the file’s line ending mode explicitly:

    C-x RET c unix RET

Then save the file. For batch conversion across files, `dos2unix` is more efficient on the command line.

### Kill a whole line

    C-S-backspace   ; kill-whole-line

This removes the entire line and newline regardless of cursor position. If your terminal doesn’t support this key combination, define your own:

```elisp
(global-set-key (kbd "C-c C-x") 'kill-whole-line)
```

### Duplicate a line

Method 1: Kill and yank

    C-S-backspace   ; kill the line
    C-y             ; yank at target location

Method 2: Copy line without deleting

```elisp
(defun copy-line (arg)
  "Copy lines (as many as prefix argument) in the kill ring."
  (interactive "p")
  (kill-ring-save (line-beginning-position)
                  (line-beginning-position (+ 1 arg)))
  (message "%d line%s copied" arg (if (= 1 arg) "" "s")))

(global-set-key (kbd "C-c C-k") 'copy-line)
```

### Find and replace

Interactive replace (prompted for each match):

    M-%   ; query-replace

Batch replace all occurrences:

    M-x replace-string

## Rectangle operations

Rectangle commands work on rectangular regions defined by column ranges across multiple lines. Set mark at one corner, point at the opposite corner, then apply commands:

    C-x r k             ; kill-rectangle
    C-x r d             ; delete-rectangle
    C-x r y             ; yank-rectangle
    C-x r o             ; open-rectangle (insert blanks)
    C-x r c             ; clear-rectangle (replace with spaces)
    C-x r N             ; rectangle-number-lines
    C-x r t STRING      ; string-rectangle (replace each line)

Example: Add a prefix to multiple lines. Select the rectangle at column 0, then:

    C-x r t "// "

This prepends `//` to each line in the rectangle.

## Spell checking

Check spelling in the buffer:

    M-x ispell

Enable continuous spell-checking in the current buffer:

    M-x flyspell-mode

For programming, check only comments and strings:

    M-x flyspell-prog-mode

When Ispell highlights a misspelled word, press `?` for correction options.

## TAGS for code navigation

Generate TAGS file recursively in the current directory:

```elisp
(defun regen-tags ()
  "Regenerate TAGS file for the current directory."
  (interactive)
  (let ((tag-file (concat default-directory "TAGS")))
    (shell-command "find . -type f -name '*.el' -o -name '*.c' -o -name '*.h' | xargs etags")
    (visit-tags-table tag-file)
    (message "TAGS regenerated")))

(global-set-key (kbd "C-c t") 'regen-tags)
```

Then navigate to definitions with:

    M-.     ; find-tag
    M-*     ; pop-tag-mark (return to previous location)

Modern projects should use `lsp-mode` instead of TAGS for better IDE-like navigation.

## Undo and redo

Emacs has a linear undo system tracking all buffer states:

    C-/     ; undo
    C-?     ; redo (undo the undo)

Alternatively:

    C-x u   ; undo

Performing regular commands after undo clears the redo stack. To recover undone changes, use `C-/` multiple times.

## Display and appearance

### Show line numbers

Modern Emacs (29+) includes `display-line-numbers-mode`:

    M-x display-line-numbers-mode

Enable globally by default:

```elisp
(global-display-line-numbers-mode)
```

The older `linum-mode` is slower and should be avoided.

### Set font and size

Configure the default font in your init file:

```elisp
(set-face-attribute 'default nil 
                    :family "Monospace" 
                    :height 120)
```

The height is in 1/10 of a point. Adjust font size in the current session:

    C-x C-+     ; increase
    C-x C--     ; decrease
    C-x C-0     ; reset to default

### Hide interface elements

Disable the toolbar:

```elisp
(tool-bar-mode -1)
```

Disable the menu bar (useful for terminal Emacs):

```elisp
(menu-bar-mode -1)
```

Toggle either at runtime with `M-x tool-bar-mode` or `M-x menu-bar-mode`.

## Compilation and error navigation

In compile mode, jump between errors:

    C-x `       ; next-error
    M-g M-p     ; previous-error
    M-g M-n     ; next-error (alternative)

Configure compile command:

```elisp
(global-set-key (kbd "C-c c") 'compile)
(setq compile-command "make -j4")
```
