---
title: "Setting Tab Widths in Vim: 2 and 4 Space Options"
date: 2018-03-24 11:50:45 +0000
layout: post
canonical: https://www.systutorials.com/in-vim-are-there-shortcuts-to-set-tab-widths-to-2-and-4/
---

Different projects and languages have different indentation conventions. Rather than manually adjusting settings each time you switch contexts, you can define custom commands in Vim to toggle between common tab widths quickly.

## Using Custom Functions and Mappings

Add these functions to your `~/.vimrc`:

```vim
function SetTab2()
  set shiftwidth=2
  set tabstop=2
  set softtabstop=2
  echo "Set tab to 2 spaces"
endfunction

function SetTab4()
  set shiftwidth=4
  set tabstop=4
  set softtabstop=4
  echo "Set tab to 4 spaces"
endfunction

nnoremap <leader>t2 :call SetTab2()<CR>
nnoremap <leader>t4 :call SetTab4()<CR>
```

Now you can press `<leader>t2` or `<leader>t4` (where `<leader>` is typically backslash by default) to switch between 2 and 4 space indentation. The `echo` statement confirms which width was applied.

## Understanding the Tab Settings

- **tabstop**: Number of spaces a tab character represents when viewing a file
- **shiftwidth**: Spaces used for auto-indentation (when Vim indents automatically)
- **softtabstop**: Spaces inserted when you press Tab in insert mode

Setting all three to the same value ensures consistent behavior across insertion, indentation, and viewing.

## Alternative: Using Commands Instead of Mappings

If you prefer calling commands by name rather than key sequences, use this approach:

```vim
function SetTab2()
  set shiftwidth=2 tabstop=2 softtabstop=2
  echo "Set tab to 2 spaces"
endfunction

function SetTab4()
  set shiftwidth=4 tabstop=4 softtabstop=4
  echo "Set tab to 4 spaces"
endfunction

command Tab2 call SetTab2()
command Tab4 call SetTab4()
```

Then type `:Tab2` or `:Tab4` in normal mode.

## Project-Specific Configuration with EditorConfig

For a more robust solution, use `.editorconfig` files in your project root:

    root = true

    [*]
    indent_style = space
    indent_size = 4

    [*.js]
    indent_size = 2

    [*.py]
    indent_size = 4

Install the `editorconfig-vim` plugin (via your package manager), and Vim will automatically apply these settings when opening files. This approach scales better across teams and projects.

## Detecting Existing Indentation

You can also create a function that detects the indentation used in an already-formatted file:

```vim
function DetectIndent()
  let save_cursor = getcurpos()
  " Check first 1000 lines for indentation patterns
  let indent_2 = len(filter(getline(1, 1000), 'v:val =~ "^  [^ ]"'))
  let indent_4 = len(filter(getline(1, 1000), 'v:val =~ "^    [^ ]"'))
  let indent_8 = len(filter(getline(1, 1000), 'v:val =~ "^\t"'))

  if indent_8 > indent_2 && indent_8 > indent_4
    call SetTab8()
  elseif indent_2 > indent_4
    call SetTab2()
  else
    call SetTab4()
  endif
  call setpos('.', save_cursor)
endfunction

command DetectIndent call DetectIndent()
```

This is particularly useful when opening legacy code or files from unknown sources.

## Essential Editor Configuration

A well-configured editor dramatically improves productivity. For Vim users, invest time in crafting a solid vimrc. For Emacs users, use use-package for cleaner configuration management. Both editors support extensive plugin ecosystems that can transform them into full IDEs.

Learn the navigation commands thoroughly before adding plugins. Mastery of core movement commands (word, paragraph, search motions in Vim; mark, isearch, ace-jump in Emacs) provides more productivity gains than any single plugin.

## Performance Tips

Large files can slow down both editors. For Vim, set lazyredraw and disable syntax highlighting for files over a certain size. For Emacs, use so-long-mode for files with long lines. Both editors benefit from disabling line numbers on very large files to improve scrolling performance.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
