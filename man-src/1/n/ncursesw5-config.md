---
title: "ncursesw5-config(1)"
name: "ncursesw5-config"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncursesw5-config/"
description: "ncursesw6-config – helper script for ncurses libraries"
---

<h2 class="name">NAME</h2>
<p> ncursesw6-config &#8211; helper script for ncurses libraries </p>
<h2>SYNOPSIS</h2>
<p> <code>ncursesw6-config</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> This is a shell script which simplifies configuring applications against a particular set of ncurses libraries.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;prefix</code></p>
<dd> echos the package-prefix of ncurses</p>
<dt><code>&#8211;exec-prefix</code></p>
<dd> echos the executable-prefix of ncurses</p>
<dt><code>&#8211;cflags</code></p>
<dd> echos the C compiler flags needed to compile with ncurses</p>
<dt><code>&#8211;libs</code></p>
<dd> echos the libraries needed to link with ncurses</p>
<dt><code>&#8211;version</code></p>
<dd> echos the release+patchdate version of ncurses</p>
<dt><code>&#8211;abi-version</code></p>
<dd> echos the ABI version of ncurses</p>
<dt><code>&#8211;mouse-version</code></p>
<dd> echos the mouse-interface version of ncurses</p>
<dt><code>&#8211;bindir</code></p>
<dd> echos the directory containing ncurses programs</p>
<dt><code>&#8211;datadir</code></p>
<dd> echos the directory containing ncurses data</p>
<dt><code>&#8211;includedir</code></p>
<dd> echos the directory containing ncurses header files</p>
<dt><code>&#8211;libdir</code></p>
<dd> echos the directory containing ncurses libraries</p>
<dt><code>&#8211;mandir</code></p>
<dd> echos the directory containing ncurses manpages</p>
<dt><code>&#8211;terminfo</code></p>
<dd> echos the $TERMINFO terminfo database path, e.g.,</p>
<dl>
<dt>
<dd> /etc/terminfo</dl>
<dt><code>&#8211;terminfo-dirs</code></p>
<dd> echos the $TERMINFO_DIRS directory list, e.g.,</p>
<dl>
<dt>
<dd> /etc/terminfo:/lib/terminfo:/usr/share/terminfo</dl>
<dt><code>&#8211;termpath</code></p>
<dd> echos the $TERMPATH termcap list, if support for termcap is configured.</p>
<dt><code>&#8211;help</code></p>
<dd> prints this message</dl>
<h2>SEE ALSO</h2>
<p> <code>ncurses</code>(3NCURSES) </p>
<p> This describes <code>ncurses</code> version 6.3 (patch 20211021). </p>
<h2>Index</h2>
