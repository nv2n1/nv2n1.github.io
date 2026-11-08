---
title: "How to Manually Set Vim\u2019s Filetype"
date: 2018-03-24 11:49:47 +0000
modified: 2026-04-12 10:58:22 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-manually-set-vims-filetype/
---

Vim’s filetype detection usually works automatically, but sometimes you need to manually override or set the filetype for a specific buffer. This guide covers manual filetype setting, debugging detection issues, and creating custom filetype definitions.

## Set Filetype Manually

```wp-block-code
:set filetype=python
```

Or use the shorthand:

```wp-block-code
:set ft=python
```

This immediately applies the syntax highlighting, indentation rules, and plugin settings for the specified filetype to the current buffer. The change is instant and affects only the current file.

## Check Current Filetype

```wp-block-code
:set filetype?
```

This displays the current filetype. If it shows `filetype=` (empty), Vim hasn’t detected a type for this file.

## Why Detection Fails

Common reasons Vim doesn’t detect the filetype:

- The file has an uncommon or missing extension
- The file is empty (no content for heuristic analysis)
- Filetype detection is disabled in your configuration
- Multiple detection rules conflict and the wrong one wins
- The file uses a non-standard encoding that confuses detection

## Ensure Filetype Detection Is Enabled

The most common issue — add this to your `~/.vimrc`:

```wp-block-code
filetype plugin indent on
```

This single line enables three things: filetype detection (figuring out what type a file is), plugin loading (running filetype-specific scripts), and indentation (applying filetype-specific indent rules). Without it, Vim treats every file as plain text.

## Debug Filetype Detection

See which script set the filetype:

```wp-block-code
:verbose set filetype?
```

This shows the filetype and the script that last modified it. Very useful for finding conflicting detection rules.

List all loaded scripts to see the detection order:

```wp-block-code
:scriptnames
```

Look for entries in `ftdetect/` directories to find which scripts are competing.

## Force Filetype on Specific Files

Add an autocommand for files that Vim consistently misidentifies:

```wp-block-code
" In ~/.vimrc
autocmd BufRead,BufNewFile *.conf set filetype=dosini
autocmd BufRead,BufNewFile *.env set filetype=sh
autocmd BufRead,BufNewFile *.jsx set filetype=javascript.jsx
autocmd BufRead,BufNewFile *.tsx set filetype=typescript.tsx
```

For a cleaner setup, put these rules in a separate ftdetect file:

```wp-block-code
" ~/.vim/ftdetect/custom.vim
au BufRead,BufNewFile *.conf set filetype=dosini
au BufRead,BufNewFile *.env set filetype=sh
```

Or use a modeline in the file itself — this works regardless of extension:

```wp-block-code
# vim: set filetype=yaml :
```

## Filetype Detection Order

Vim checks multiple sources to determine filetype, in this order:

1.  **Modeline** — Inline comments in the file itself (highest priority)
2.  **ftdetect scripts** — `~/.vim/ftdetect/*.vim` and system-wide scripts
3.  **filetype.vim** — Global extension-to-filetype mappings
4.  **Scripts in \$VIMRUNTIME** — Built-in detection rules shipped with Vim

The last matching rule wins. If you have conflicting rules, the load order determines which takes effect.

## Common Filetypes Reference

Quick lookup for frequently used filetypes:

- `c` — C source files (.c, .h)
- `cpp` — C++ source files (.cpp, .hpp, .cc)
- `python` — Python (.py)
- `javascript` — JavaScript (.js, .mjs)
- `typescript` — TypeScript (.ts)
- `sh` — Shell scripts (.sh, .bash, .zsh)
- `yaml` — YAML (.yml, .yaml)
- `json` — JSON (.json)
- `markdown` — Markdown (.md)
- `html` — HTML (.html, .htm)
- `css` — CSS (.css)
- `go` — Go (.go)
- `rust` — Rust (.rs)
- `java` — Java (.java)
- `tex` — LaTeX (.tex)
- `dockerfile` — Dockerfile (Dockerfile\*)
- `toml` — TOML (.toml)

## Creating a Custom Filetype

If you have a completely custom file format, create three files:

**Detection rule** (`~/.vim/ftdetect/myformat.vim`):

```wp-block-code
au BufRead,BufNewFile *.myf set filetype=myformat
```

**Syntax highlighting** (`~/.vim/syntax/myformat.vim`):

```wp-block-code
if exists("b:current_syntax")
    finish
endif
syntax keyword myKeyword function return if else while for
syntax keyword myType int string bool float
syntax match myComment "#.*$"
highlight def link myKeyword Keyword
highlight def link myType Type
highlight def link myComment Comment
let b:current_syntax = "myformat"
```

**Indentation rules** (`~/.vim/indent/myformat.vim`):

```wp-block-code
setlocal autoindent
setlocal indentexpr=
setlocal nocindent
```

After creating these files, restart Vim and any `.myf` file will have proper syntax highlighting and indentation.

## Neovim Filetype Configuration

In Neovim, use Lua for filetype configuration:

```wp-block-code
-- ~/.config/nvim/init.lua
vim.filetype.add({
    extension = {
        myf = "myformat",
        env = "sh",
    },
    filename = {
        [".env.local"] = "sh",
        ["Makefile"] = "make",
    },
    pattern = {
        [".*%.conf"] = "dosini",
    },
})
```

Neovim’s approach is more structured than Vim’s autocommand method and handles complex patterns like double extensions more reliably.

## Quick Reference

- `:set ft=python` — Set filetype manually
- `:set ft?` — Check current filetype
- `:verbose set ft?` — Debug which script set it
- `filetype plugin indent on` — Enable all filetype features
- Modeline: `# vim: set filetype=yaml :`
- `~/.vim/ftdetect/` — Custom detection rules directory
