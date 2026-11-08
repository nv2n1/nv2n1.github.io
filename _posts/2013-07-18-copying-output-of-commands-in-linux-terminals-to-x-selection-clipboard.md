---
title: "Copy Command Output to Clipboard in Linux"
date: 2013-07-18 03:45:02 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/copying-output-of-commands-in-linux-terminals-to-x-selection-clipboard/
---

xclip is a utility that bridges the command line and X11 selections, letting you pipe command output directly to your clipboard. It’s indispensable for workflows where you’re generating content in the terminal and pasting it elsewhere—whether that’s a browser, text editor, or another application.

## Installation

On Fedora/RHEL-based systems:

``` bash
sudo dnf install xclip
```

On Debian/Ubuntu:

``` bash
sudo apt install xclip
```

On Arch:

``` bash
sudo pacman -S xclip
```

## Understanding X Selections

X11 maintains two separate clipboard buffers:

- **Primary selection**: What you highlight with your mouse. Paste with middle-click or Shift+Insert.
- **Clipboard selection**: What you copy with Ctrl+C. Paste with Ctrl+V.

By default, xclip uses primary selection. Use the `-selection clipboard` flag for the standard Ctrl+C/Ctrl+V clipboard.

## Copying File Content to Clipboard

To primary selection (middle-click paste):

``` bash
cat file.txt | xclip
```

Or without piping:

``` bash
xclip -i file.txt
```

To clipboard selection (Ctrl+V paste):

``` bash
cat file.txt | xclip -selection clipboard
```

## Copying Command Output to Clipboard

Pipe any command directly to xclip:

``` bash
# Copy your current IP address
hostname -I | xclip -selection clipboard

# Copy system information
uname -a | xclip -selection clipboard

# Copy SSH public key
cat ~/.ssh/id_rsa.pub | xclip -selection clipboard

# Copy the output of a long grep search
grep "pattern" largefile.txt | xclip -selection clipboard

# Copy Docker container IDs and names
docker ps --format "table {% raw %}{{{% endraw %}.ID}}\t{% raw %}{{{% endraw %}.Names}}" | xclip -selection clipboard

# Copy a systemctl status for pasting in reports
systemctl status nginx | xclip -selection clipboard

# Copy git log in a formatted way
git log --oneline -10 | xclip -selection clipboard
```

## Pasting Clipboard Content to a File

To write what’s currently in your clipboard to a file:

``` bash
xclip -selection clipboard -o > output.txt
```

To append instead of overwrite:

``` bash
xclip -selection clipboard -o >> output.txt
```

## Practical Workflows

Copy a command’s output and immediately use it in your editor:

``` bash
ps aux | grep nginx | xclip -selection clipboard
# Then Ctrl+V in your text editor or email
```

Backup your environment variables:

``` bash
env | xclip -selection clipboard
# Paste into a safe location
```

Generate and copy a hash without touching the clipboard manually:

``` bash
sha256sum file.iso | awk '{print $1}' | xclip -selection clipboard
```

Copy multiple lines of logs with filtering:

``` bash
journalctl -u nginx -n 50 --no-pager | xclip -selection clipboard
```

Extract JSON output from a command and copy it for parsing elsewhere:

``` bash
curl -s https://api.example.com/data | jq '.' | xclip -selection clipboard
```

## Checking What’s in Your Clipboard

View the current contents without saving to a file:

``` bash
xclip -selection clipboard -o
```

This is helpful for debugging or confirming what actually got copied. You can also pipe this to other commands:

``` bash
xclip -selection clipboard -o | wc -l  # Count lines
xclip -selection clipboard -o | grep pattern  # Search contents
```

## Useful Aliases

Add these to your `.bashrc` or `.zshrc` for faster workflows:

``` bash
alias cbcopy='xclip -selection clipboard -i'
alias cbpaste='xclip -selection clipboard -o'
```

Then use:

``` bash
cat file.txt | cbcopy
cbpaste > file.txt
```

You can also create an alias with visual feedback:

``` bash
alias cbcopy='xclip -selection clipboard -i && echo "Copied to clipboard"'
```

## Wayland Systems

If you’re on a newer system using Wayland instead of X11, xclip won’t work. Use `wl-copy` and `wl-paste` from the wl-clipboard package instead:

``` bash
# Install on Debian/Ubuntu
sudo apt install wl-clipboard

# Install on Fedora/RHEL
sudo dnf install wl-clipboard

# Wayland usage
cat file.txt | wl-copy
wl-paste > file.txt
```

## Detecting Your Session and Creating Portable Scripts

For systems where you might use both X11 and Wayland, or need to share scripts across environments, create a wrapper function:

``` bash
copy_to_clipboard() {
    if [ -n "$WAYLAND_DISPLAY" ]; then
        wl-copy
    elif [ -n "$DISPLAY" ]; then
        xclip -selection clipboard -i
    else
        echo "Error: Neither X11 nor Wayland session detected"
        return 1
    fi
}

paste_from_clipboard() {
    if [ -n "$WAYLAND_DISPLAY" ]; then
        wl-paste
    elif [ -n "$DISPLAY" ]; then
        xclip -selection clipboard -o
    else
        echo "Error: Neither X11 nor Wayland session detected"
        return 1
    fi
}
```

Add these functions to your shell configuration file and use them like:

``` bash
ps aux | copy_to_clipboard
paste_from_clipboard | less
```

## Troubleshooting

If xclip produces no output or doesn’t seem to work, verify your X11 session is running:

``` bash
echo $DISPLAY
```

If this returns nothing, X11 isn’t available. For remote SSH sessions, you need X11 forwarding enabled:

``` bash
ssh -X user@host
```

For very large outputs that might exceed clipboard limits, consider splitting the data or using temporary files instead. Most systems have practical limits around 50MB, though this varies by desktop environment.

If you’re piping binary data or non-UTF8 content, xclip may fail silently. Check what you’re working with:

``` bash
echo "test" | file -
```

On systems without an active X11 or Wayland session (like headless servers accessed via SSH without X forwarding), clipboard utilities won’t function. In these cases, rely on file redirection or temporary files for data transfer instead.
