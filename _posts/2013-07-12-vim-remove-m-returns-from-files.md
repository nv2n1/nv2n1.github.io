---
title: "Removing ^M Line Endings in Vim"
date: 2013-07-12 16:31:47 +0000
modified: 2026-04-12 16:08:37 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /vim-remove-m-returns-from-files/
---

When you open a Windows file in Vim (or Neovim), you’ll often see `^M` characters at the end of lines. These are carriage returns (`\r`) from Windows line endings (CRLF), which don’t display properly on Unix-like systems that expect LF-only line endings.

## Quick Fix

The fastest way to remove these characters is with a substitution command:

```vim
:1,$s/^M//g
```

To enter the literal `^M`, type `Ctrl+V` followed by `Ctrl+M` in command mode. The `Ctrl+V` tells Vim to insert the next character literally instead of interpreting it as a command.

Breaking down the command:

- `:` — enter ex command mode
- `1,$` — range from line 1 to the last line (you can use `%` as shorthand)
- `s/pattern/replacement/flags` — substitution command
- `^M` — the carriage return character (entered as `Ctrl+V` + `Ctrl+M`)
- `g` — replace all occurrences on each line

So the equivalent shorthand version:

```vim
:%s/^M//g
```

## Better Approach: Fix the File Format

Rather than removing characters after the fact, it’s better to convert the file format. Vim has a `fileformat` option for this:

```vim
:set fileformat=unix
:wq
```

This converts CRLF to LF and writes the file. Check your current file format with:

```vim
:set fileformat?
```

Output will show `fileformat=dos` (Windows), `fileformat=unix` (Linux/Mac), or `fileformat=mac` (old Mac, rarely used).

## Automatic Detection and Conversion

If you’re frequently working with cross-platform files, configure Vim to handle this automatically. Add this to your `~/.vimrc` or `~/.config/nvim/init.vim`:

```vim
set fileformats=unix,dos,mac
```

Vim will detect the file format when opening and use the first matching format from the list. You can also force detection on a specific file:

```vim
:e ++fileformat=dos
```

Then immediately convert and save:

```vim
:set fileformat=unix
:wq
```

## Using dos2unix Command

For bulk conversion outside of Vim, use the `dos2unix` utility:

``` bash
dos2unix file.txt
```

Or without installing extra tools, use sed:

``` bash
sed -i 's/\r$//' file.txt
```

The `\r` matches the carriage return character, and `$` anchors it to the end of the line.

## Checking for Hidden Line Endings

If you’re unsure whether a file has mixed line endings, use `cat -A`:

``` bash
cat -A file.txt
```

Lines ending with `$` have Unix line endings. Lines ending with `^M$` have Windows line endings.

In Vim, you can also check by looking at the status line (rightmost corner), which displays the file format. Or use:

```vim
:set list
```

This shows whitespace characters — `$` marks line ends, and you’ll see `^M` if carriage returns are present.

## Essential Editor Configuration

A well-configured editor dramatically improves productivity. For Vim users, invest time in crafting a solid vimrc. For Emacs users, use use-package for cleaner configuration management. Both editors support extensive plugin ecosystems that can transform them into full IDEs.

Learn the navigation commands thoroughly before adding plugins. Mastery of core movement commands (word, paragraph, search motions in Vim; mark, isearch, ace-jump in Emacs) provides more productivity gains than any single plugin.

## Performance Tips

Large files can slow down both editors. For Vim, set lazyredraw and disable syntax highlighting for files over a certain size. For Emacs, use so-long-mode for files with long lines. Both editors benefit from disabling line numbers on very large files to improve scrolling performance.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
