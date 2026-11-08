---
title: "Xterm Color Codes in Vim: A Complete Guide"
date: 2018-03-24 11:47:22 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /xterm-color-codes-for-vim-on-linux/
---

Vim supports Xterm 256-color codes on Linux and modern terminals. Understanding the color palette and how to use it in your configuration is essential for building readable syntax highlighting schemes and custom colorschemes.

## The 256-Color Palette

Xterm’s 256-color mode consists of:

- **Colors 0-15**: Standard ANSI colors (black, red, green, yellow, blue, magenta, cyan, white, and bright variants)
- **Colors 16-231**: 216 RGB colors arranged in a 6×6×6 cube
- **Colors 232-255**: 24 grayscale colors from near-black to near-white

The RGB cube (colors 16-231) uses the formula: `16 + 36 × r + 6 × g + b`, where r, g, and b range from 0 to 5.

For example:

- Color 16: `16 + 36(0) + 6(0) + 0` = black
- Color 114: `16 + 36(3) + 6(1) + 2` = a specific shade of green
- Color 231: `16 + 36(5) + 6(5) + 5` = white

## Standard ANSI Colors (0-15)

These are commonly used in Vim colorschemes:

    0 = Black
    1 = Maroon/Red
    2 = Green
    3 = Olive/Yellow
    4 = Navy/Blue
    5 = Purple
    6 = Teal/Cyan
    7 = Silver/Light Gray
    8 = Gray/Dark Gray
    9 = Bright Red
    10 = Lime/Bright Green
    11 = Yellow
    12 = Blue
    13 = Fuchsia
    14 = Aqua/Bright Cyan
    15 = White

## Using Xterm Colors in Vim

Set colors in your `.vimrc` using the `ctermfg` (foreground) and `ctermbg` (background) attributes:

```vim
highlight Normal ctermfg=7 ctermbg=0
highlight String ctermfg=10
highlight Comment ctermfg=8
highlight Keyword ctermfg=5 ctermbg=NONE
```

For the RGB cube (colors 16-231), specify the decimal code directly:

```vim
highlight CustomHighlight ctermfg=114 ctermbg=232
```

## RGB Cube Quick Reference

The 216 RGB colors (16-231) follow a predictable pattern. To find a color code from RGB values:

- Convert each RGB component (0-255) to a 0-5 scale: divide by 51 and round
- Use the formula: `16 + 36 × r + 6 × g + b`

Example: For RGB(255, 128, 0):

- r = 255 ÷ 51 = 5
- g = 128 ÷ 51 ≈ 2.5 → 3
- b = 0 ÷ 51 = 0
- Color code = `16 + 36(5) + 6(3) + 0` = **214** (orange)

## Grayscale Colors (232-255)

Colors 232-255 provide a grayscale gradient:

    232 = Near black (darkest)
    233-254 = Progressive shades of gray
    255 = Near white (lightest)

Use these for neutral backgrounds and subtle highlights:

```vim
highlight LineNr ctermfg=240 ctermbg=NONE
highlight StatusLine ctermfg=15 ctermbg=238
```

## Testing Your Terminal’s Colors

To see all 256 colors in your terminal, use this command:

``` bash
for i in {0..255}; do printf "\x1b[38;5;${i}mColor ${i}\x1b[0m  "; done | column
```

Or display them in a grid format with a simpler script:

``` bash
for i in {0..255}; do
    printf "\x1b[48;5;${i}m   \x1b[0m"
    [ $((($i + 1) % 16)) -eq 0 ] && printf "\n"
done
```

## Checking Your Terminal’s Capabilities

Verify your terminal supports 256 colors:

``` bash
echo $TERM
```

Should output something like `xterm-256color`, `tmux-256color`, or `screen-256color`. If not, update your terminal configuration:

``` bash
export TERM=xterm-256color
```

Add this to your shell’s RC file (`.bashrc`, `.zshrc`, etc.) to persist it.

## Creating a Custom Colorscheme

Combine your knowledge of the color palette to build coherent schemes:

```vim
" Custom dark theme
highlight Normal ctermfg=15 ctermbg=0
highlight String ctermfg=114 ctermbg=NONE
highlight Number ctermfg=180 ctermbg=NONE
highlight Comment ctermfg=244 ctermbg=NONE
highlight Keyword ctermfg=169 ctermbg=NONE
highlight Function ctermfg=117 ctermbg=NONE
highlight Operator ctermfg=208 ctermbg=NONE
```

Vim also supports true color (24-bit RGB) in modern terminals using `set termguicolors`, which lets you use hex colors directly (`#RRGGBB`), but the 256-color palette remains widely compatible and is often preferable for remote SSH sessions and tmux environments.
