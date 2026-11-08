---
title: "Vim: Performing Case-Insensitive Searches"
date: 2018-03-24 08:04:42 +0000
author: "Q A"
layout: post
categories: [algorithms-data-structures]
canonical: /vim-case-insensitive-search/
---

Vim performs case-sensitive searches by default. If you search for `error`, it won’t match `Error` or `ERROR`. Here are several ways to enable case-insensitive searching.

## Toggle Case Sensitivity During Search

The quickest method — append `\c` anywhere in your search pattern:

```wp-block-code
/error\c
```

This matches `error`, `Error`, `ERROR`, and any other casing. The `\c` flag applies only to the current search.

Conversely, use `\C` to force case-sensitive search when `ignorecase` is enabled:

```wp-block-code
/error\C
```

## Set ignorecase Globally

Make all searches case-insensitive by default:

```wp-block-code
:set ignorecase
```

Or the shorthand:

```wp-block-code
:set ic
```

Add it to your `~/.vimrc` for permanent effect:

```wp-block-code
set ignorecase
```

## Smart Case Sensitivity

The best option for most users — combine `ignorecase` with `smartcase`:

```wp-block-code
set ignorecase
set smartcase
```

With `smartcase`:

- Searching for `error` (all lowercase) — case-insensitive, matches `Error`, `ERROR`
- Searching for `Error` (contains uppercase) — case-sensitive, matches only `Error`

This gives you the best of both worlds: casual lowercase searches are flexible, while uppercase searches are precise.

## Toggle During a Session

Quick key mappings in your `~/.vimrc`:

```wp-block-code
" Toggle ignorecase with leader+i
nnoremap <leader>i :set ignorecase!<CR>

" Show current setting
nnoremap <leader>I :set ignorecase?<CR>
```

Or use the built-in toggle shortcut — press `/` to start search, then `Ctrl+C` to toggle case sensitivity (with some Vim configurations).

## Case-Insensitive Substitution

The `\c` flag also works with substitute commands:

```wp-block-code
:%s/error/issue/gc\c
```

Wait — the flag goes in the pattern, not after the flags:

```wp-block-code
:%s/error\c/issue/gc
```

This replaces all casings of “error” with “issue”, asking for confirmation on each match.

## Search With Very Magic Mode

For complex patterns with case-insensitivity:

```wp-block-code
/\v\cerror_\d+
```

The `\v` (very magic) makes special characters work without escaping, and `\c` enables case-insensitivity. The order doesn’t matter — `\c\v` works too.

## Search History and Case

Vim remembers search patterns with their case settings. Browse search history with `/` then arrow keys. Each pattern retains its `\c` or `\C` flag from the original search.

Clear search highlighting after a search:

```wp-block-code
:nohlsearch
```

Or map it to a convenient key:

```wp-block-code
nnoremap <Esc> :nohlsearch<CR>
```

## Quick Reference

- `/pattern\c` — Case-insensitive for this search only
- `/pattern\C` — Case-sensitive for this search only
- `:set ic` — Global case-insensitive
- `:set smartcase` — Smart case (use with ic)
- `:%s/old\c/new/g` — Case-insensitive substitution

## Case-Insensitive Search in Visual Mode

When searching for the visually selected text, add case-insensitivity:

```wp-block-code
" Search visual selection (case-insensitive)
vnoremap // y/\V<C-R>"\c<CR>
```

This yanks the selected text, then searches for it literally (\V very nomagic) with case-insensitivity (\c).

## Using \* and \# with Case-Insensitivity

The `*` and `#` keys search for the word under the cursor. With `ignorecase` set, they automatically become case-insensitive. Without it, make them case-insensitive with a mapping:

```wp-block-code
" Case-insensitive word search
nnoremap * /\<\=expand('<cword>')\>\c<CR>
nnoremap # ?\<\=expand('<cword>')\>\c<CR>
```

## Plugin: vim-slash

The `vim-slash` plugin improves search highlighting and automatically clears it after moving:

```wp-block-code
" Install with vim-plug
Plug 'junegunn/vim-slash'
```

It doesn’t affect case sensitivity directly, but it enhances the search experience by making highlights less intrusive.

## Neovim Differences

In Neovim, the same settings work identically:

```wp-block-code
set ignorecase
set smartcase
```

Neovim also supports the `/\c` and `/\C` inline flags the same way as Vim. The configuration goes in `~/.config/nvim/init.lua` (Lua) or `init.vim` (Vimscript).
