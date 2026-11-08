---
title: "Configuring Auto-Indentation for OCaml in Vim"
date: 2018-03-24 08:19:23 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/auto-indenting-for-ocaml-code-in-vim/
---

Vim’s default OCaml indentation is limited and doesn’t handle the language’s syntax well. You’ll want to use `ocp-indent`, a dedicated indentation tool built specifically for OCaml that understands the language’s scoping and structure rules.

## Installing ocp-indent

First, install the tool via OPAM (OCaml Package Manager):

``` bash
opam install ocp-indent
```

If you don’t have OPAM installed, install it first:

``` bash
# On Ubuntu/Debian
sudo apt-get install opam

# On macOS
brew install opam

# Initialize OPAM (first time only)
opam init
eval $(opam env)
```

Verify the installation:

``` bash
which ocp-indent
ocp-indent --version
```

## Configuring Vim

Create or edit your `~/.vimrc` file and add:

```vim
" OCaml indentation with ocp-indent
let g:formatprg="ocp-indent"
autocmd FileType ocaml setlocal formatprg=ocp-indent
autocmd FileType ocaml setlocal shiftwidth=2 softtabstop=2 tabstop=2 expandtab
```

The `shiftwidth` settings match OCaml’s standard 2-space indentation convention.

## Using ocp-indent in Vim

Once configured, you have several ways to apply indentation:

**Indent the current line:**

```vim
:!ocp-indent
```

**Indent a range (for example, lines 10 to 20):**

```vim
:10,20!ocp-indent
```

**Indent the entire file:**

```vim
:%!ocp-indent
```

Or use the standard Vim motion commands:

```vim
gg=G    " Indent from start to end of file
=ip     " Indent current paragraph
```

## Better integration with vim-plug

For a more modern setup using vim-plug, add this to your `~/.vimrc`:

```vim
Plug 'ocaml/vim-ocaml'

autocmd FileType ocaml setlocal formatprg=ocp-indent
autocmd FileType ocaml setlocal shiftwidth=2 softtabstop=2 tabstop=2 expandtab
```

Install the plugin:

```vim
:PlugInstall
```

## Neovim users

If you’re using Neovim with a modern config, you can set this in `~/.config/nvim/init.lua`:

``` lua
vim.api.nvim_create_autocmd("FileType", {
  pattern = "ocaml",
  callback = function()
    vim.opt_local.formatprg = "ocp-indent"
    vim.opt_local.shiftwidth = 2
    vim.opt_local.softtabstop = 2
    vim.opt_local.tabstop = 2
    vim.opt_local.expandtab = true
  end,
})
```

## LSP-based indentation (modern approach)

For OCaml 5.0+, consider using an OCaml language server with Neovim or VS Code. The `ocaml-lsp-server` provides better indentation and formatting:

``` bash
opam install ocaml-lsp-server
```

This gives you real-time indentation feedback and integrates with modern editor configurations.

## Common issues

**ocp-indent not found:** Ensure the OPAM environment is sourced. Add this to your shell profile if needed:

``` bash
eval $(opam env)
```

**Wrong indentation after paste:** After pasting OCaml code, reapply indentation with `:%!ocp-indent` to fix formatting.

**Conflicts with other formatters:** If you use formatters like `ocamlformat`, choose one primary tool to avoid conflicts. `ocamlformat` is more aggressive about style; `ocp-indent` focuses on indentation alone.

## Essential Editor Configuration

A well-configured editor dramatically improves productivity. For Vim users, invest time in crafting a solid vimrc. For Emacs users, use use-package for cleaner configuration management. Both editors support extensive plugin ecosystems that can transform them into full IDEs.

Learn the navigation commands thoroughly before adding plugins. Mastery of core movement commands (word, paragraph, search motions in Vim; mark, isearch, ace-jump in Emacs) provides more productivity gains than any single plugin.

## Performance Tips

Large files can slow down both editors. For Vim, set lazyredraw and disable syntax highlighting for files over a certain size. For Emacs, use so-long-mode for files with long lines. Both editors benefit from disabling line numbers on very large files to improve scrolling performance.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
