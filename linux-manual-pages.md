---
title: Linux Man Pages
layout: home
permalink: /linux-manual-pages/
---

## Linux man pages support has been deprecated

The Linux man pages section of SysTutorials is no longer available. Every Linux system ships its own manuals: here is how to install and read them on a Linux box.

### Reading man pages

To read the manual for a command, library call, or file format, run `man`:

``` shell
man ls
```

Manuals are organized in sections: 1 is user commands, 2 system calls, 3 library functions, 5 file formats, and 8 administration commands. When a name appears in several sections, pass the section first:

``` shell
man 5 passwd
```

Search manuals by keyword with `apropos` (equivalent to `man -k`), and get a one-line summary with `whatis`:

``` shell
apropos "copy files"
whatis ls
```

### Installing man pages

Most distributions include the `man` reader (`man-db`) and the core manuals by default. If they are missing:

- Debian/Ubuntu: `sudo apt install man-db manpages manpages-dev`
- Fedora/RHEL: `sudo dnf install man-db man-pages`
- Arch Linux: `sudo pacman -S man-db man-pages`

After installing, build the keyword database once:

``` shell
sudo mandb
```

[Browse all posts](/)
