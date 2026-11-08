---
title: "Profiling Vim Startup and Runtime Performance"
date: 2015-03-29 04:51:52 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/profiling-vim-to-find-out-which-plugin-makes-vim-slow/
---

Vim is generally fast, but dozens of plugins can create noticeable slowdowns. Since Vim’s core remains single-threaded, any blocking operation in a loaded plugin will freeze your editor until it completes. Rather than disable plugins randomly, use Vim’s built-in profiling tools to identify the actual culprit.

## Profile Vim Startup Time

The fastest way to find slow plugins is to profile Vim’s startup sequence:

``` bash
vim --startuptime profile.log
```

After Vim opens, close it normally (`:q`). The `profile.log` file shows timing data for every file sourced during startup:

    times in msec
     clock   self+sourced   self:  sourced script
     clock   elapsed:              other lines

    000.018  000.018: --- VIM STARTING ---
    000.113  000.095: Allocated generic buffers
    000.188  000.075: locale set
    ...
    019.459  000.179  000.179: sourcing /home/user/.vim/bundle/Vundle.vim/autoload/vundle.vim
    019.660  000.137  000.137: sourcing /home/user/.vim/bundle/Vundle.vim/autoload/vundle/config.vim
    085.672  000.971  000.971: sourcing /home/user/.vim/bundle/YouCompleteMe/plugin/youcompleteme.vim
    100.023  014.292  014.292: sourcing /home/user/.vim/bundle/AutoTag/plugin/autotag.vim
    114.569  014.046  012.347: sourcing /home/user/.vim/bundle/Syntastic/plugin/syntastic.vim
    149.035  029.274  029.274: sourcing /home/user/.vim/bundle/LustyJuggler/plugin/lusty-juggler.vim

The columns mean:

- **clock**: Elapsed time since Vim started
- **self+sourced**: Time spent in this file plus everything it called
- **self**: Time spent only in this file (not in called files)
- **sourced script**: The file being processed

Sort by the `self+sourced` column to find the slowest plugins. Any single plugin taking more than 200-300ms is worth investigating.

## Interpreting Startup Results

Look for these red flags:

- Plugin initialization exceeding 500ms
- Repeated file sourcing (syntax highlighting, filetype detection running multiple times)
- Duplicate plugin paths (sign of misconfigured package managers)
- External tool invocations during startup (like linters or LSP servers)

If you use a modern plugin manager like vim-plug, lazy.nvim, or packer.nvim, defer or lazy-load problematic plugins. For example, with lazy.nvim in Neovim:

``` lua
{
  'preservim/nerdtree',
  cmd = 'NERDTreeToggle',  -- Only load when this command is run
  keys = { { '<C-n>', ':NERDTreeToggle<CR>' } }
}
```

With vim-plug:

```vim
Plug 'dense-analysis/ale', { 'on': ['ALEEnable'] }
```

This defers loading until the command is explicitly called or a mapped key is pressed.

## Profile Runtime Operations

Startup profiling only catches initialization costs. To find what slows Vim during actual use—like when saving files, switching buffers, or triggering completions—use runtime profiling:

```vim
:profile start profile.log
:profile func *
:profile file *
```

Now perform the slow action in Vim (save a file, switch buffers, trigger a linter, etc.) that reproduces the lag. When done, stop profiling:

```vim
:profile pause
```

Write and quit (`:wq`). The `profile.log` contains detailed function call timing. Jump to the end to see two summary tables.

## Reading Runtime Profile Output

Example output:

    FUNCTIONS SORTED ON TOTAL TIME
    count  total (s)   self (s)  function
        1 127.616234   0.000035  <SNR>27_BufWritePostHook()
        1 127.616184   0.000131  <SNR>27_UpdateErrors()
        1 127.615884   0.000138  <SNR>27_CacheErrors()
        1 127.585890   0.000054  SyntaxCheckers_scala_fsc_GetLocList()
        1 127.585429   0.000217  SyntasticMake()

    FUNCTIONS SORTED ON SELF TIME
    count  total (s)   self (s)  function
        1   0.029048   0.028209  85()
        2   0.002786   0.002718  <SNR>50_OnFileReadyToParse()
        1   0.001322   0.001322  <SNR>37_Highlight_Matching_Pair()
        6   0.000725   0.000672  Tlist_Get_Tagname_By_Line()

- **TOTAL TIME** shows which function chains consumed the most time overall (including nested calls).
- **SELF TIME** reveals where the CPU actually spent time without nested calls.

In this example, `SyntasticMake()` took 127 seconds—a linting plugin doing expensive work on save. The solution is to either disable it for that filetype or replace it with a faster async alternative.

## Practical Solutions

Once you’ve identified a slow plugin:

**Disable it entirely**: If you don’t use it often, remove it from your config entirely.

**Disable for specific filetypes**: Many plugins support per-filetype configuration:

```vim
let g:syntastic_scala_checkers = []  " Disable Syntastic for Scala
let g:prettier#autoformat_config_present = 0  " Disable Prettier auto-format
let g:ale_linters = { 'python': [] }  " No linters for Python files
```

**Lazy-load on demand**: Use your plugin manager to load only when needed. With vim-plug:

```vim
Plug 'dense-analysis/ale', { 'on': ['ALEEnable', 'ALEToggle'] }
Plug 'fatih/vim-go', { 'for': 'go' }  " Load only for Go files
```

With packer.nvim (Neovim):

``` lua
use {
  'dense-analysis/ale',
  cmd = 'ALEEnable'
}
```

**Replace with faster alternatives**: Some plugins have significantly faster successors:

| Old | New | Why |
|----|----|----|
| Syntastic | ALE or efm-langserver | Async, non-blocking |
| YouCompleteMe | Native LSP (nvim-cmp, coc.nvim) | Simpler, faster |
| ctags-based plugins | LSP-based alternatives | Real semantic understanding |
| vim-syntax-extra | Built-in treesitter (Neovim) | Incremental parsing |

## Neovim-Specific Profiling

Neovim’s async architecture makes blocking operations less common, but profiling works similarly. Use `:profile` the same way, but also check for plugin conflicts:

```vim
:checkhealth
```

This command verifies your LSP setup, treesitter parsers, and common configuration issues. For more granular profiling, consider using `nvim-dap` with a debugger or Neovim’s native profiling via `:profile debug` for startup-time analysis.

## Keep Performance in Check

- **Quarterly plugin audit**: Run `:scriptnames` to see every loaded script. Uninstall anything unused.
- **Monitor startup time**: Re-run `vim --startuptime` regularly after adding plugins.
- **Use minimal configs for quick sessions**: Keep a lightweight `.vimrc` for fast editing when performance matters.
- **Disable unnecessary visual features**: If using terminal Vim, `set lazyredraw` and disable unnecessary syntax highlighting in large files.
- **Consider filetype-specific configs**: Load expensive plugins only for filetypes where you actually need them.

Modern plugin managers make this much easier than in older Vim setups. Take advantage of lazy-loading and per-filetype configuration to keep Vim snappy even with a full plugin ecosystem.
