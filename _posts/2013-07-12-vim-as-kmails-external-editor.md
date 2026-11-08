---
title: "Using Vim as an External Editor in KMail"
date: 2013-07-12 16:32:29 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/vim-as-kmails-external-editor/
---

Vim is an excellent choice for email composition, and KMail makes it straightforward to use as your external editor. This setup is particularly useful if you already live in Vim and want consistent keybindings across your workflow.

## KMail’s External Editor Configuration

KMail has built-in support for external editors. Navigate to **Settings → Configure KMail → Composing → General** and enable **“Use external editor instead of composer”**. You’ll specify the editor command here, where `%f` is replaced with the temporary email file path.

While you could configure KWrite with Vi input mode, running Vim in a terminal gives you the full power of your custom configuration and plugins.

## Wrapper Script for Vim in Konsole

Since Vim is a terminal application, you need a wrapper to launch it within KDE. Konsole handles the terminal window, and `--nofork` ensures KMail blocks until you finish editing.

Create a script called `kcallvim`:

``` bash
#!/bin/bash

# Email file with .eml extension for proper syntax highlighting
email="${1}.eml"
cp "$1" "$email"

# --nofork keeps the process running until vim exits
# This allows KMail to detect when editing is complete
konsole --nofork --geometry 1000x600 -e vim "$email"

# Copy edited content back and clean up
cp "$email" "$1" && rm -f "$email"
```

Key points:

- The `--nofork` flag is critical—without it, Konsole returns immediately and KMail won’t wait for your edits
- Adding `.eml` extension enables Vim’s email syntax highlighting automatically
- The script uses proper quoting around `$1` and `$email` to handle filenames with spaces
- `--geometry 1000x600` sets a reasonable window size; adjust to your preference

Make the script executable:

``` bash
chmod +x kcallvim
```

Place it in a directory in your `$PATH` (like `~/.local/bin/` or `/usr/local/bin`), or use the full path when configuring KMail.

## Configuring KMail

In the KMail external editor field, enter:

    kcallvim %f

That’s the entire command. KMail will pass the temporary email file as the first argument.

## In Practice

When you compose or reply to a message, KMail opens a dialog. Triggering the external editor (usually a button or menu option) launches Konsole with Vim. Edit normally—your full Vim configuration applies, including custom mappings, abbreviations, and filetype plugins. When you `:wq` or `:x` Vim, Konsole closes automatically, KMail reads the modified file, and you’re back in the composer with your text ready to send.

## Alternative: Direct Terminal Usage

If you prefer not to depend on Konsole, you can use a simpler approach with `$TERMINAL`:

``` bash
#!/bin/bash

email="${1}.eml"
cp "$1" "$email"

# Uses your default terminal (GNOME Terminal, xterm, etc.)
${TERMINAL:-xterm} -e vim "$email"

cp "$email" "$1" && rm -f "$email"
```

This is more portable across desktop environments, though it may not block properly on all terminals. Test before relying on it.

## Syntax Highlighting and Settings

Since emails are plain text, Vim won’t apply special syntax highlighting by default. You can force email syntax by adding this to your `~/.vim/filetype.vim`:

```vim
au BufNewFile,BufRead *.eml setfiletype mail
```

Or in your `~/.vimrc`, auto-detect based on the temporary file location that KMail uses (typically in `/tmp`). Consider adding these settings for email composition:

```vim
autocmd FileType mail setlocal textwidth=72 spell spelllang=en_us
```

Setting `textwidth=72` maintains the traditional email width limit for better compatibility.
