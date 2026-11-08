---
title: "Remapping Keyboard Keys in Emacs: Evil Mode and System-Level Options"
date: 2014-07-30 09:11:36 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/keyboard-key-mapping-for-emacs-evil-mode-and-rearranging-alt-ctrl-and-win-keys/
---

Emacs keybindings rely heavily on Ctrl because the editor was designed for Lisp machines in the 1970s—machines where Ctrl sat near the spacebar. Modern PC keyboards moved it to the corner, making constant reaches painful. Once millions of users built muscle memory around these bindings, changing them became impractical.

If modern keyboard ergonomics matter to you, several practical solutions exist.

## Evil Mode for Vim-Like Keybindings

If you’re comfortable with Vim, Evil mode brings modal editing and home-row-friendly key mappings into Emacs while keeping Emacs’ power and extensibility. Your hands stay on the home row for cursor movement and editing—no constant Ctrl reaches.

Install Evil with `use-package`:

```elisp
(use-package evil
  :ensure t
  :init
  (setq evil-want-integration t
        evil-want-keybinding nil)
  :config
  (evil-mode 1))
```

Add `evil-collection` for comprehensive keybinding coverage across Emacs modes:

```elisp
(use-package evil-collection
  :ensure t
  :after evil
  :config
  (evil-collection-init))
```

Map Ctrl-\[ to Escape so you don’t reach for the Esc key:

```elisp
(define-key evil-insert-state-map (kbd "C-[") 'evil-normal-state)
```

## OS-Level Key Remapping

### Linux (X11)

Use `xmodmap` for system-wide remapping. Create `~/.Xmodmap`:

    ! Swap Ctrl and Alt
    clear control
    clear mod1
    keycode 37 = alt_L Alt_L
    keycode 108 = alt_R Alt_R
    keycode 64 = control_L
    keycode 109 = control_L
    add control = Control_L Control_R
    add mod1 = Alt_L Alt_R

Apply it immediately:

``` bash
xmodmap ~/.Xmodmap
```

Persist across sessions by adding to `~/.xinitrc` or `~/.xsessionrc`:

``` bash
[[ -f ~/.Xmodmap ]] && xmodmap ~/.Xmodmap
```

### Linux (Wayland)

`xmodmap` doesn’t work on Wayland. Configure remapping in your compositor instead.

For GNOME/Wayland:

``` bash
gsettings set org.gnome.desktop.input-sources xkb-options "['ctrl:swap_lalt_lctrl']"
```

For generic XKB-based systems:

``` bash
localectl set-x11-keymap us "" "" ctrl:swap_lalt_lctrl
```

### Caps Lock as Control

Caps Lock is rarely used and sits in an accessible position. Remap it universally.

X11:

``` bash
xmodmap -e "clear Lock" -e "keycode 66 = Control_L"
xmodmap -e "add Control = Control_L"
```

Wayland (GNOME):

``` bash
gsettings set org.gnome.desktop.input-sources xkb-options "['caps:ctrl_modifier']"
```

Persistent systemd-localed approach:

``` bash
localectl set-x11-keymap us "" "" caps:ctrl_modifier
```

### Space as Control (Advanced)

Some users map space to Control when held, and space when tapped. This requires `xcape` on X11:

``` bash
xcape -e 'Control_L=space'
```

This remaps left Control to space on release. Useful combined with Control when held. Be aware: some editors intercept keys before `xcape` processes them, breaking this technique.

### Win/Super Key Remaps

Map Super/Win to Alt or Control:

``` bash
xmodmap -e "keycode 115 = alt_L" -e "add mod1 = alt_L"
```

Or use `setxkbmap`:

``` bash
setxkbmap -option altwin:swap_alt_win
```

## Hardware Solutions

Software remapping can feel fragile if you work across multiple machines. Programmable keyboards provide system-independent remapping.

Ergonomic split keyboards (Kinesis, ErgoDox, Lily58) let you customize key placement natively. Mechanical keyboards with QMK or VIA firmware (\$100–\$200) give you remapping that works everywhere—operating system independent.

A cost-effective approach: remap Caps Lock to Control (OS-level) plus a \$30 mechanical keyboard. This combination addresses most strain issues.

## Combining Approaches

The most effective setup stacks solutions:

- Remap Caps Lock to Control at the OS level (applies system-wide)
- Use Evil mode in Emacs for modal editing
- Optionally swap Alt and Control if it matches your muscle memory
- Consider an ergonomic keyboard if you code 8+ hours daily

This reduces hand strain without forcing a complete Emacs workflow redesign. Start with Caps Lock remapping and Evil mode; upgrade your hardware only if strain persists.
