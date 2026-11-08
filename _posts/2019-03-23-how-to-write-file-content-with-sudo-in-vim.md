---
title: "How to Save a File in Vim Without Restarting with sudo"
date: 2019-03-23 11:20:41 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-write-file-content-with-sudo-in-vim/
---

You opened a system config file in Vim without sudo, made changes, and hit `:w` to save. Permission denied. Retyping everything isn’t happening.

## The Solution: `:w !sudo tee %`

From Vim’s normal mode, type:

```vim
:w !sudo tee %
```

This pipes your buffer through `tee` running as root:

- `:w` — write the current buffer
- `!` — pipe to an external command
- `sudo tee` — execute tee with root privileges
- `%` — current filename

Vim sends your buffer to `tee` via stdin, `tee` writes it to disk as root, and you’re done. You’ll be prompted for your sudo password if needed.

## Handling the Reload Prompt

After the write succeeds, Vim detects that the file changed on disk:

    WARNING: The file has been changed since reading it!!!
    Do you really want to write to it anyway? (y/n)

Press `y` to proceed. Then:

    [O]k, (L)oad File, (I)gnore:

- `L` — reload the file from disk (recommended)
- `I` — keep your buffer without reloading (use if you want to verify before reloading)

Your undo history stays intact. You don’t lose your edits or have to reopen the file.

## Why Not Just Quit and Reopen?

Some people suggest `:q!`, then `sudo vim file`, then retypng everything. Don’t do that. Using `:w !sudo tee %` keeps your undo history, avoids reopening the file entirely, and handles the permission issue transparently.

## Practical Example

You’re editing `/etc/hosts`:

``` bash
$ vim /etc/hosts
```

You add a local hostname entry and try to save. Vim blocks you:

    E45: 'readonly' option is set (add ! to override)

Instead of forcing a write with `:w!` (which still fails without privileges), use:

```vim
:w !sudo tee %
```

Enter your sudo password at the prompt. Vim asks if you want to reload the file from disk. Press `L` to confirm the write succeeded.

## Preserving File Permissions and Ownership

The `tee` command writes with your shell’s umask, which may not match the original file’s permissions. Check before you start:

``` bash
ls -l /etc/hosts
```

After saving with `tee`, restore permissions if needed:

``` bash
sudo chmod 644 /etc/hosts
sudo chown root:root /etc/hosts
```

For repeated edits to the same file, it’s cleaner to just start with `sudo vim` from the beginning.

## Binary Files

The `:w !sudo tee %` method works for text files. For binary files, use `sudo vim` from the start, or write with `dd` instead:

```vim
:w !sudo dd of=%
```

## Troubleshooting

**“sudo: no password available”**

You need sudoers access and a terminal that can receive password prompts. SSH sessions sometimes don’t allocate a TTY. Use `ssh -t user@host` to force TTY allocation. Verify sudoers access with `sudo -v` before opening Vim.

**Wrong permissions after saving**

`tee` creates files with default umask permissions. Check the result:

``` bash
ls -l /etc/hosts
```

Use `sudo chmod` to fix if needed.

**“E492: Not an editor command: w”**

You’re in insert mode. Press `Escape` first, then type the command.

**Binary file corruption**

Use `sudo vim` from the start for binary files, not this method.

## Modern Alternatives

**sudoedit**

The standard tool designed for exactly this scenario:

``` bash
sudoedit /etc/hosts
```

It handles permissions transparently and opens your `$EDITOR` automatically. The downside: it creates a temporary copy, which can cause issues with tools that monitor the original file.

**Neovim with suda.vim**

Neovim users often prefer the suda.vim plugin:

```vim
:e suda://%
:w
```

This handles the reload automatically and feels more native to the workflow.

**eunuchs.vim**

If you use the eunuchs.vim plugin:

```vim
:e sudo:/etc/hosts
```

It transparently handles sudo writes without manual tee commands. For one-off edits, the built-in approach is faster.

**Just start with sudo**

For repeated edits to system files, the simplest approach is standard:

``` bash
sudo vim /path/to/file
```

This avoids the whole permission dance. It’s what sysadmins do when editing multiple config files in a session.

## Why Vim for System Administration

Vim and Neovim remain essential for sysadmin work because they work everywhere SSH reaches, require no heavy dependencies, and integrate seamlessly with shell commands and scripting. The ability to pipe buffers to external commands (`:w !cmd`) and read command output (`:read !cmd`) enables workflows that graphical editors make difficult. Modern Neovim adds LSP support for infrastructure-as-code, competitive with VS Code, while staying lightweight over high-latency connections.

The `:w !sudo tee %` trick is simple, but it exemplifies Vim’s design philosophy: composability, external command integration, and minimal overhead.
