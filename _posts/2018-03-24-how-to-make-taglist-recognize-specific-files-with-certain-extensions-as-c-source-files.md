---
title: "Making Vim Recognize Custom File Extensions as C"
date: 2018-03-24 11:44:15 +0000
modified: 2026-04-12 10:43:34 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /how-to-make-taglist-recognize-specific-files-with-certain-extensions-as-c-source-files/
---

Vim determines file types by extension to apply syntax highlighting and indentation. If you have custom file extensions that should be treated as C files, you need to configure Vim to recognize them.

## Using autocommand in .vimrc

Add an autocommand to your `~/.vimrc`:

```wp-block-code
" Treat .h and .c files in a custom directory as C
autocmd BufRead,BufNewFile *.myc set filetype=c
autocmd BufRead,BufNewFile *.h set filetype=c
```

For multiple extensions:

```wp-block-code
" Multiple custom extensions as C
autocmd BufRead,BufNewFile *.c.in,*.h.in,*.ec set filetype=c
```

## Using filetype.vim

For a cleaner setup, create a filetype detection rule:

```wp-block-code
" ~/.vim/ftdetect/my_c_files.vim
au BufRead,BufNewFile *.myc,*.ec,*.c.in set filetype=c
```

Vim automatically loads files from `~/.vim/ftdetect/` on startup. Each file can define detection rules for related file types.

## Using Modelines

For per-file configuration, add a modeline comment inside the file itself:

```wp-block-code
// vim: set filetype=c :
```

Or for more settings:

```wp-block-code
/* vim: set ft=c ts=4 sw=4 expandtab: */
```

Modelines work regardless of the file extension, making them useful for files shared across different systems.

## Checking the Current Filetype

```wp-block-code
" Check what filetype Vim detected
:set filetype?

" Force a filetype
:set filetype=c
```

## Complete C Development Setup

For a good C editing experience in Vim, combine filetype detection with proper indentation and syntax:

```wp-block-code
" ~/.vimrc - C development setup
filetype plugin indent on
syntax on

" C-specific indentation
autocmd FileType c setlocal tabstop=4 shiftwidth=4 expandtab
autocmd FileType c setlocal cindent
autocmd FileType c setlocal cinoptions=(0,l1,g0,t0,Ls,Ws

" Auto-format with clang-format
autocmd FileType c nnoremap <buffer> <F5> :%!clang-format<CR>
autocmd FileType c vnoremap <buffer> <F5> :!clang-format<CR>

" Compile and run
autocmd FileType c nnoremap <buffer> <F9> :w<CR>:!gcc % -o %:r -Wall -Wextra && ./%:r<CR>
```

## Neovim Configuration

In Neovim, use Lua for configuration:

```wp-block-code
-- ~/.config/nvim/init.lua
vim.filetype.add({
    extension = {
        myc = "c",
        ec = "c",
        ["c.in"] = "c",
    },
    filename = {
        ["config.h.in"] = "c",
    },
})
```

Neovim’s `vim.filetype.add()` is more structured than Vim’s autocommand approach and handles edge cases like double extensions (e.g., `.c.in`) better.

## Indentation and Formatting

Once Vim recognizes your files as C, configure indentation style:

```wp-block-code
" K&R style (default)
set cindent
set cinoptions=(0,l1,g0,t0,Ls,Ws

" Linux kernel style
set tabstop=8
set shiftwidth=8
set noexpandtab

" GNU style
set tabstop=2
set shiftwidth=2
set expandtab
```

## Quick Reference

- `autocmd BufRead,BufNewFile *.ext set filetype=c` — .vimrc method
- `~/.vim/ftdetect/*.vim` — Clean detection rules
- `/* vim: set ft=c: */` — Per-file modeline
- `:set filetype?` — Check current filetype
- `vim.filetype.add()` — Neovim Lua method

## Debugging Filetype Detection

If Vim isn’t detecting your file type correctly, debug the detection chain:

```wp-block-code
" Show what scripts ran for filetype detection
:verbose set filetype?

" Show all loaded ftdetect scripts
:scriptnames | grep ftdetect

" Test a pattern manually
:echo matchstr('myfile.ec', '\\.ec$')
```

Common issues:

- Multiple rules conflict — last loaded rule wins. Check script load order with `:scriptnames`
- Modelines are disabled — ensure `set modeline` is in your config
- The file extension matches a different filetype rule built into Vim

To force detection order, load your ftdetect file after the default rules by naming it to sort last alphabetically (e.g., `zz_my_c.vim`).

## Custom Syntax for Extended C

If your custom file extension adds keywords or syntax beyond standard C:

```wp-block-code
" ~/.vim/after/syntax/c.vim
" Add custom keywords
syntax keyword cType uint8 uint16 uint32 uint64
syntax keyword cType int8 int16 int32 int64
syntax keyword cConstant TRUE FALSE NULL
highlight def link cType Type
highlight def link cConstant Constant
```

Files in `~/.vim/after/syntax/` are loaded after the default syntax files, allowing you to extend without overriding.
