---
title: "Using Vim as Thunderbird\u2019s External Editor on Linux"
date: 2013-07-12 16:32:24 +0000
modified: 2026-04-11 16:42:26 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /vim-as-thunderbirds-external-editor-in-linux/
---

Thunderbird’s built-in compose window is functional but limited. Using Vim as an external editor gives you the full power of modal editing and your customizations for email composition.

## Prerequisites

You need Thunderbird with the **External Editor** extension installed. As of 2026, this extension continues to work with current Thunderbird versions. Install it from the Thunderbird add-ons repository.

## Setting up the external editor

You have two main approaches: use a graphical Vim variant, or invoke Vim in a terminal.

### Option 1: Using gvim (simpler)

If you have gvim installed, configuration is straightforward. In External Editor’s preferences, set the text editor command to:

    gvim -f

The `-f` flag keeps gvim in the foreground, blocking Thunderbird until you save and exit.

### Option 2: Using Vim in a terminal (recommended)

If you prefer the terminal version, you’ll need a wrapper script since Vim alone won’t work reliably with Thunderbird’s IPC mechanism.

Create a script called `callvim` in a directory on your PATH (e.g., `~/bin/`):

``` bash
#!/bin/bash
# Wrapper to launch Vim in a terminal for Thunderbird's External Editor
# Works with xterm, but modern terminals like Alacritty or foot also work

if command -v xterm &> /dev/null; then
    xterm -e vim "$@"
elif command -v alacritty &> /dev/null; then
    alacritty -e vim "$@"
else
    # Fallback - adjust based on your system's available terminals
    urxvt -e vim "$@"
fi
```

Make it executable:

``` bash
chmod +x ~/bin/callvim
```

Then in External Editor’s preferences, set the text editor command to:

    callvim

The script uses `xterm` by default (widely available), but you can replace it with `alacritty`, `foot`, or your preferred terminal if it’s faster or better integrated with your desktop.

## Using Vim in Thunderbird

Once configured, press **Ctrl+E** while composing a new message or replying to open your external editor. Edit the message in Vim, save it (`:wq`), and exit. Thunderbird immediately updates the compose window with your changes.

## Optimizing Vim for email

Add email-specific configuration to your `~/.vimrc` to tailor Vim for message composition:

```vim
augroup email
  autocmd!
  autocmd FileType mail call SetupMailOptions()
augroup END

function! SetupMailOptions()
  setlocal textwidth=72
  setlocal spell spelllang=en
  setlocal wrap
  setlocal linebreak
  setlocal noautoindent
  setlocal nocindent

  " Auto-format quoted text (lines starting with >)
  setlocal formatoptions=aw

  " Abbreviations for common phrases
  iabbrev <buffer> gd Good day!
  iabbrev <buffer> regards Best regards,
  iabbrev <buffer> thx Thank you!
endfunction
```

Key settings explained:

- `textwidth=72`: Standard email width for better readability and compatibility with quoted text
- `spell spelllang=en`: Enable spell checking
- `wrap` and `linebreak`: Wrap long lines without breaking words
- `formatoptions=aw`: Auto-format paragraphs and preserve existing formatting
- `iabbrev <buffer>`: Buffer-local abbreviations that expand as you type

## Advanced customization

You can detect Thunderbird-specific mail files (typically temporary files) and apply settings automatically:

```vim
" Detect Thunderbird's temporary mail files
autocmd BufRead,BufNewFile /tmp/nscopy*,/tmp/mutt* setfiletype mail
```

For signature handling, add this to skip signatures during spell checking:

```vim
function! SetupMailOptions()
  " ... existing settings ...
  " Skip lines starting with -- (signature delimiter)
  setlocal spellcapcheck=[.?!]\\_[\\]\\ ]\\+
  syntax match mailSignature /^-- $/ nextgroup=mailSignatureBody
  syntax match mailSignatureBody /.*/ contained
  highlight mailSignatureBody ctermfg=gray
endfunction
```

## Troubleshooting

**Editor doesn’t open**: Verify the command path is correct by running it directly in a terminal with a test file.

**Thunderbird hangs**: Make sure your wrapper script blocks until Vim exits. Avoid background processes or detached terminals.

**Character encoding issues**: Thunderbird defaults to UTF-8 for modern email. Vim’s default settings handle this, but if you see garbled text, check your locale and Vim’s `fileencoding` setting.

**Terminal doesn’t appear**: On some X11 systems, use `gnome-terminal -- vim "$@"` instead of xterm, or switch to a lightweight terminal like Alacritty for better startup time.
