---
title: "Speeding Up Emacs Startup with Daemon Mode and Native Compilation"
date: 2018-03-24 08:20:58 +0000
author: "Eric Ma"
layout: post
categories: [code-optimization]
canonical: /how-to-make-emacs-start-up-faster/
---

Emacs startup time matters when you’re opening files frequently from the command line or in scripts. A few targeted optimizations can reduce perceived startup overhead from seconds to near-instant.

## Run Emacs as a daemon with emacsclient

The most effective optimization is the server/client architecture. Start Emacs once as a daemon, then reuse that instance for all subsequent file operations.

Start the daemon:

``` bash
emacs --daemon
```

Then open files in the running instance:

``` bash
emacsclient -nw myfile.txt
```

The `-nw` flag opens in your terminal. Use `-c` for a graphical frame:

``` bash
emacsclient -c myfile.txt
```

**Set environment variables** so external tools use your Emacs instance:

``` bash
export EDITOR='emacsclient -t'
export VISUAL='emacsclient -c'
```

Now `git commit`, `crontab -e`, and similar commands automatically open in your running Emacs session instead of spawning a new process.

**Ensure the daemon starts automatically.** If you use systemd (most modern Linux distributions), create a user-level service unit at `~/.config/systemd/user/emacs.service`:

``` ini
[Unit]
Description=Emacs Daemon
Documentation=info:emacs

[Service]
Type=simple
ExecStart=/usr/bin/emacs --daemon
Restart=on-failure

[Install]
WantedBy=default.target
```

Then enable it:

``` bash
systemctl --user enable emacs
systemctl --user start emacs
```

If you don’t use systemd, add this to your shell rc file (`.bashrc`, `.zshrc`, etc.):

``` bash
if ! pgrep -x emacs > /dev/null; then
    emacs --daemon &
fi
```

This spawns the daemon only if it’s not already running, avoiding duplicate processes across shell sessions.

## Lazy-load packages in your configuration

Even with a daemon running, your initial startup time matters when you first start Emacs. Defer expensive operations in `init.el`:

**Use use-package with `:defer` and `:bind`** to delay loading until the binding is actually invoked:

```elisp
(use-package helm
  :defer t
  :bind (("C-x C-f" . helm-find-files)
         ("C-x b" . helm-buffers-list)))
```

**Attach packages to hooks** so they load only when relevant:

```elisp
(use-package lsp-mode
  :hook (python-mode . lsp)
  :defer t
  :custom
  (lsp-enable-file-watchers nil)
  (lsp-idle-delay 0.5))
```

**Load language modes only for matching file extensions:**

```elisp
(use-package rust-mode
  :defer t
  :mode "\\.rs\\'")

(use-package go-mode
  :defer t
  :mode "\\.go\\'")
```

The `:mode` keyword automatically defers loading until a file matching that extension is opened.

**Disable unnecessary default packages** if you don’t use them:

```elisp
(setq package-load-list '(all (eglot . nil) (python . nil)))
```

This prevents Emacs from loading `eglot` and `python` packages by default.

## Profile your startup

Measure where time is actually spent before optimizing blindly.

**Use built-in timing:**

```elisp
(add-hook 'emacs-startup-hook
  (lambda () 
    (message "Emacs loaded in %.2fs" 
      (float-time (time-subtract (current-time) before-init-time)))))
```

**Use the `benchmark-init` package for detailed breakdown:**

```elisp
(use-package benchmark-init
  :config
  (benchmark-init/activate)
  (add-hook 'after-init-hook 'benchmark-init/show-durations))
```

Run `emacs -Q` (no init file) to get a baseline startup time, then compare with your full configuration. The difference shows the cost of your customizations.

## Byte-compile your configuration

Elisp files load faster when byte-compiled to `.elc` files:

``` bash
emacs -batch -f batch-byte-compile ~/.emacs.d/init.el
```

Recompile after updating your configuration:

``` bash
emacs -batch -f batch-byte-compile ~/.emacs.d/**/*.el
```

Some package managers like `straight.el` and `elpaca` byte-compile packages automatically.

## Enable native compilation (Emacs 28+)

Native compilation converts Elisp to machine code at load time. Build Emacs with:

``` bash
./configure --with-native-compilation --with-tree-sitter
make
make install
```

The `--with-tree-sitter` flag is also recommended for modern syntax highlighting performance.

If you’re using a distribution package, check whether it’s already built with native compilation:

``` bash
emacs --version | grep native
```

Native compilation noticeably improves both startup and runtime performance for large packages.

## Practical workflow

Combine these strategies for the best results:

1.  **Always run Emacs as a daemon** on system startup via systemd or shell rc
2.  **Alias your shell** to use emacsclient: `alias emacs='emacsclient -t'`
3.  **Defer heavy packages** in your configuration (LSP, treesitter, IDE features)
4.  **Byte-compile your init.el** after updates
5.  **Enable native compilation** if using Emacs 28+
6.  **Profile startup** with `benchmark-init` if it still feels slow

With this setup, opening a file is effectively instant—the daemon is already running, and emacsclient connects in milliseconds.
