---
title: "Upgrading ELPA Packages in Emacs"
date: 2018-03-24 11:44:52 +0000
modified: 2026-04-12 08:38:56 +0000
author: "Eric Ma"
layout: post
categories: [linux-system-configuration]
canonical: /how-to-upgrade-packages-installed-by-elpa-in-emacs/
---

ELPA (Emacs Lisp Package Archive) packages receive regular updates. Keeping your packages current ensures you have the latest features and bug fixes. Here’s how to upgrade ELPA packages in Emacs.

## Interactive Upgrade (Recommended)

Use Emacs’s built-in package manager:

1.  Open the package list: `M-x list-packages`
2.  Press **U** to mark all upgradable packages
3.  Press **x** to execute the upgrades
4.  Restart Emacs to load the updated packages

In the package list buffer:

- **i** — mark for install
- **d** — mark for delete
- **U** — mark all upgradable packages
- **x** — execute marked actions
- **g** — refresh the package list
- **h** — show help

## Upgrade from Elisp

For programmatic upgrades (useful in your init file or scripts):

```wp-block-code
;; Upgrade all packages automatically
(defun upgrade-all-packages ()
  "Upgrade all installed packages."
  (interactive)
  (package-refresh-contents)
  (dolist (package package-alist)
    (let ((name (car package)))
      (when (package-installed-p name)
        (package-update name)))))

;; Call it
(upgrade-all-packages)
```

## Using use-package for Management

If you use `use-package` (recommended for modern Emacs configurations), packages are auto-updated when you run `package-refresh-contents` and then `package-install`:

```wp-block-code
;; In your init.el
(use-package magit
  :ensure t    ;; Auto-install if missing
  :pin melpa)  ;; Use MELPA for updates

(use-package company
  :ensure t
  :pin melpa-stable)  ;; Use stable channel
```

To update all use-package managed packages:

```wp-block-code
M-x package-refresh-contents RET
M-x package-install-selected-packages RET
```

## Auto-upgrade with auto-package-update

The `auto-package-update` package automates the upgrade process:

```wp-block-code
(use-package auto-package-update
  :ensure t
  :config
  (setq auto-package-update-delete-old-versions t
        auto-package-update-hide-results t
        auto-package-update-interval 7)  ;; Check weekly
  (auto-package-update-maybe))
```

This checks for updates every 7 days and automatically upgrades packages when Emacs starts.

## Package Archives Configuration

Ensure you have the right package archives configured for the widest selection:

```wp-block-code
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(add-to-list 'package-archives '("melpa-stable" . "https://stable.melpa.org/packages/") t)
(add-to-list 'package-archives '("org" . "https://orgmode.org/elpa/") t)
(package-initialize)
```

## Handling Upgrade Problems

**Package dependency conflicts:**

```wp-block-code
;; Delete and reinstall the problematic package
M-x package-delete RET problem-package RET
M-x package-install RET problem-package RET
```

**Broken package database:**

```wp-block-code
;; Delete the package directory cache
rm -rf ~/.emacs.d/elpa/
rm -rf ~/.emacs.d/elpa/archives/

;; Restart Emacs and reinstall
M-x package-refresh-contents
M-x package-install-selected-packages
```

**Version mismatch after upgrade:**

Sometimes byte-compiled files from the old version cause issues. Force recompilation:

```wp-block-code
M-: (byte-recompile-directory package-user-dir nil t)
```

## Using straight.el for Reproducible Installs

For more control over package versions, `straight.el` uses git directly instead of ELPA tarballs:

```wp-block-code
(use-package straight
  :ensure t
  :config
  (setq straight-use-package-by-default t))

;; Packages are pinned to git commits
;; Lockfile at ~/.emacs.d/straight/versions/default.el
```

This gives you reproducible builds — every machine gets the exact same package versions from the lockfile.

## Quick Reference

- `M-x list-packages` → **U** → **x** — Interactive upgrade
- `package-refresh-contents` — Update package list
- `package-install-selected-packages` — Install/update selected packages
- `auto-package-update` — Automatic weekly upgrades
- `straight.el` — Reproducible git-based package management

## Cleaning Up Old Package Versions

Over time, old package versions accumulate and consume disk space:

```wp-block-code
;; Check package directory size
M-: (directory-files package-user-dir)

;; Delete old versions automatically
(setq package-archive-upload-base nil)
(setq delete-old-versions t)
```

Or manually remove old versions:

```wp-block-code
;; List all package directories with sizes
M-: (let ((dir package-user-dir))
      (dolist (f (directory-files dir))
        (when (file-directory-p (expand-file-name f dir))
          (message "%s %s" f (nth 7 (file-attributes (expand-file-name f dir)))))))
```

For a clean start, remove the entire package directory and reinstall:

```wp-block-code
rm -rf ~/.emacs.d/elpa/
```

Then restart Emacs and run `M-x package-install-selected-packages` to reinstall everything from your configuration.

## Monitoring Package Health

Check for package issues with these commands:

```wp-block-code
;; List packages with problems
M-x package-list-packages
;; Look for status "dependency", "unsigned", or "incompatible"

;; Check for orphaned packages (installed but not in use-package)
M-: (seq-difference package-activated-packages
      (mapcar #'car use-package-alist))
```

Regularly reviewing your package list helps keep your Emacs configuration lean and fast-loading.
