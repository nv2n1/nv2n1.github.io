---
title: "Configuring Indentation in Vim for C and C++"
date: 2013-07-12 16:47:45 +0000
layout: post
canonical: https://www.systutorials.com/vim-formatting-cc-code/
---

Vim’s indentation system provides multiple approaches for formatting C/C++ code, from built-in operators to external formatters. The native tools work reliably for most tasks, while external formatters enforce stricter style rules when needed.

## The Indentation Operator and Text Objects

The `=` operator re-indents text. It requires a motion or text object to specify what to format:

    =       indentation operator (requires motion/text object)
    i{      inner block (content between braces, excluding braces)
    a{      entire block (content plus braces)

Apply indentation with these common patterns:

```vim
==          format current line
=i{         format inner block
=a{         format block including braces
=2i{        format inner block and its outer block
gg=G        format entire file
=ap         format paragraph
=}          format from cursor to next closing brace
=5j         format current line plus next 4 lines
```

## Visual Mode for Irregular Regions

When you need to format code that doesn’t align cleanly with blocks, use visual selection:

1.  Position cursor at the start
2.  Enter visual mode: `v` (character), `V` (line-based), or `Ctrl-v` (block)
3.  Navigate to end point with motions (`j`, `k`, `G`, `}`, etc.)
4.  Press `=` to indent

This handles edge cases like partial function definitions or complex conditional structures.

## Configuring C/C++ Indentation

Configure Vim’s indentation behavior for your project’s style. In `~/.vimrc` or `~/.config/nvim/init.vim`:

```vim
autocmd FileType c,cpp setlocal cindent
autocmd FileType c,cpp setlocal cinoptions=:0,l1,t0,g0
autocmd FileType c,cpp setlocal shiftwidth=4
autocmd FileType c,cpp setlocal tabstop=4
autocmd FileType c,cpp setlocal expandtab
```

Key options explained:

- `cindent` — C-style indentation (context-aware, superior to `autoindent`)
- `cinoptions` — fine-tune behavior (`:0` aligns case labels, `l1` aligns continuation lines, `t0` preserves return type indentation, `g0` aligns C++ scope declarations)
- `shiftwidth` — spaces per indent level (used by `<<` and `>>`)
- `tabstop` — display width of tab characters
- `expandtab` — insert spaces instead of tabs

For stricter control, add `cindent` options like `(0,W2s` to control parameter alignment in function calls.

## Using External Formatters

External formatters enforce project-wide style consistency. Integrate `clang-format` (LLVM’s formatter):

```vim
autocmd FileType c,cpp setlocal formatprg=clang-format
```

Then format selection or file with:

```vim
gq          format selected region
gg!Gclang-format<CR>    format entire file (alternative method)
```

Common alternatives:

- **clang-format** — LLVM project standard, reads `.clang-format` config files
- **astyle** — flexible, good for legacy codebases
- **uncrustify** — highly configurable, supports many languages

Check your project for `.clang-format`, `.astylerc`, or similar config files to ensure Vim matches team standards. If your project uses a formatter, configure it in `formatprg` to avoid style conflicts.

## Visualizing Whitespace and Indentation

Enable whitespace visualization to spot indentation problems:

```vim
set list
set listchars=tab:→\ ,trail:·,extends:»,precedes:«
```

This shows tabs as `→`, trailing spaces as `·`, and overflow indicators. For more sophisticated highlighting, install `vim-indent-guides` or `indent-blankline.nvim` (Neovim).

## Neovim Configuration

Neovim users have identical indentation commands. For Lua configuration in `init.lua`:

``` lua
vim.opt.cindent = true
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4
vim.opt.expandtab = true
```

Neovim’s built-in LSP support integrates formatters directly into the editor. If your language server provides formatting (clangd for C/C++), configure it:

``` lua
vim.lsp.buf.format({ async = true })
```

This replaces manual indentation in many workflows, but the native `=` operator remains essential when LSP isn’t available.

## Debugging Indentation Issues

If indentation behaves unexpectedly, check active settings:

```vim
:set cindent?
:set cinoptions?
:set formatprg?
```

The `?` suffix displays the current value. If a formatter is set, it overrides native indentation. Temporarily disable it to test native behavior:

```vim
:set formatprg=
```

For complex scenarios, test indentation on a small code snippet before applying it to entire files.
