---
title: "Using Emacs Server and Client for Faster Editing Sessions"
date: 2014-03-31 02:59:40 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/making-emacs-startup-faster/
---

Emacs startup is slow. If you’re using it for quick edits alongside other tools, waiting 2-3 seconds every time becomes friction. Heavy mode configurations, lazy loading chains, and initialization hooks add up fast.

The server/client architecture solves this: start an Emacs server once, then spawn lightweight clients that connect almost instantly. Your first edit waits for server startup. Every edit after that is \<100ms.

## How Server/Client Architecture Works

Emacs can run as a persistent daemon listening for client connections on a Unix socket (or TCP socket for remote access). The first client connection initializes the server—slow, but happens only once. Subsequent clients attach to the running server and inherit its state: loaded packages, buffers, customizations, everything.

The `emacsclient` command includes a `-a` flag designed exactly for this. When you run `emacsclient -a "" file.txt`, it says: “Connect to the running server. If none exists, start `emacs --daemon` first, then connect.” This automation means you don’t manage the server lifecycle manually.

## Setting Up the Client Wrapper

Create an executable script in your `$PATH`:

``` bash
#!/bin/bash
emacsclient -c -a "" "$@"
```

Save it as `~/bin/em` and make it executable:

``` bash
chmod +x ~/bin/em
```

Verify `~/bin` is in your `$PATH`:

``` bash
echo $PATH | grep -q "$HOME/bin" || echo "Add $HOME/bin to PATH"
```

If missing, add this to `~/.bashrc` or `~/.zshrc`:

``` bash
export PATH="$HOME/bin:$PATH"
```

Now `em file.txt` opens a new frame connected to your server.

## Understanding the Flags

**`-c` (create frame)**: Creates a new window frame. Without it, `emacsclient` tries to reuse an existing Emacs window—not what you want in terminal workflows. The `-c` flag ensures each invocation opens a fresh frame in your current terminal.

**`-a ""` (alternate editor)**: If no server is running, use the empty string as the fallback command. Emacs interprets this specially: start `emacs --daemon` and retry the connection. Other values like `-a vim` would launch that editor instead.

**`"$@"`**: Pass all command-line arguments (file paths, options) to the opened frame.

## Optimizing Startup Time

Even with server/client, your first invocation needs a reasonably fast init file.

### Use early-init.el (Emacs 27+)

Emacs 27 and later load `~/.emacs.d/early-init.el` before the graphical system initializes. Disable expensive UI features here:

```elisp
;; ~/.emacs.d/early-init.el
(setq package-enable-at-startup nil)
(setq frame-inhibit-implied-resize t)

(push '(menu-bar-lines . 0) default-frame-alist)
(push '(tool-bar-lines . 0) default-frame-alist)
(push '(vertical-scroll-bars) default-frame-alist)
```

This prevents loading the package system, menu bar, tool bar, and scroll bars before your main config runs.

### Lazy Load Heavy Packages

Don’t require packages at startup. Use `with-eval-after-load` to load them only when needed:

```elisp
(with-eval-after-load 'python
  (require 'lsp-mode)
  (require 'flycheck))

(with-eval-after-load 'rust-mode
  (add-hook 'rust-mode-hook #'lsp-deferred))
```

This defers loading `lsp-mode` until you open a Python or Rust file.

### Profile Your Init

If startup still feels sluggish, identify bottlenecks:

```elisp
(require 'benchmark-init)
(benchmark-init/activate)

;; ... rest of your init ...

;; At the end:
(add-hook 'after-init-hook #'benchmark-init/show-durations)
```

Restart Emacs and check the benchmark results. Remove or defer packages that contribute \>100ms.

Alternatively, use `emacs-startup-hook` to measure total time:

```elisp
(add-hook 'emacs-startup-hook
  (lambda ()
    (message "Emacs loaded in %.2fs"
      (float-time (time-subtract (current-time) before-init-time)))))
```

## Managing the Server

### Clean Shutdown

Define a safe shutdown function in your init file:

```elisp
(defun server-shutdown ()
  "Save buffers and shutdown the Emacs server"
  (interactive)
  (save-some-buffers)
  (kill-emacs))
```

Shut down cleanly with:

``` bash
emacsclient -e '(server-shutdown)'
```

This saves all modified buffers before killing the server—safer than `pkill emacs`.

### Shell Aliases

Add these to your shell config:

``` bash
alias e='em'
alias ek='emacsclient -e "(server-shutdown)"'
```

Now `e myfile.py` opens a file and `ek` cleanly exits the server.

## Remote Editing Over SSH

The server/client approach works seamlessly over SSH. When you SSH into a remote machine and run `em remotefile.txt`, it:

1.  Connects to that machine’s Emacs server (or starts one)
2.  Opens the file in a frame on your remote terminal
3.  Edits happen on the remote machine with all its packages and customizations

Each machine maintains its own independent server, so you never have cross-session confusion.

## Real-World Performance

Your editing workflow becomes:

``` bash
e myfile.py          # First call: 2-3 seconds (server starts)
e another.sh         # <100ms (connected to running server)
e config.json        # <100ms
ek                   # Clean shutdown
```

For frequent small edits, this is transformative. Emacs goes from “heavy IDE with startup tax” to “snappy terminal editor that retains full power when you need it.”

## Troubleshooting

**“emacsclient: can’t find socket”**: The server crashed or wasn’t started. Run `emacs --daemon` manually, or kill any stray `emacs` processes and try again.

**“Address already in use”**: The socket file exists but the server isn’t running. Remove `~/.emacs.d/server/server` and retry.

**“Can’t connect from remote SSH”**: By default, the socket is local-only. For remote connections, use `emacsclient -s /path/to/socket` or configure TCP access in your Emacs server (more complex; usually unnecessary).
