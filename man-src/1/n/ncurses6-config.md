---
title: "ncurses6-config(1)"
name: "ncurses6-config"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncurses6-config/"
description: "ncurses6-config – helper script for ncurses libraries"
---

<h2 class="name">NAME</h2>
<p> ncurses6-config &#8211; helper script for ncurses libraries </p>
<h2>SYNOPSIS</h2>
<p> <code>ncurses6-config</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> This is a shell script which simplifies configuring applications against a particular set of ncurses libraries.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;prefix</code></dt>
<dd> echos the package-prefix of ncurses</dd>
<dt><code>&#8211;exec-prefix</code></dt>
<dd> echos the executable-prefix of ncurses</dd>
<dt><code>&#8211;cflags</code></dt>
<dd> echos the C compiler flags needed to compile with ncurses</dd>
<dt><code>&#8211;libs</code></dt>
<dd> echos the libraries needed to link with ncurses</dd>
<dt><code>&#8211;version</code></dt>
<dd> echos the release+patchdate version of ncurses</dd>
<dt><code>&#8211;abi-version</code></dt>
<dd> echos the ABI version of ncurses</dd>
<dt><code>&#8211;mouse-version</code></dt>
<dd> echos the mouse-interface version of ncurses</dd>
<dt><code>&#8211;bindir</code></dt>
<dd> echos the directory containing ncurses programs</dd>
<dt><code>&#8211;datadir</code></dt>
<dd> echos the directory containing ncurses data</dd>
<dt><code>&#8211;includedir</code></dt>
<dd> echos the directory containing ncurses header files</dd>
<dt><code>&#8211;libdir</code></dt>
<dd> echos the directory containing ncurses libraries</dd>
<dt><code>&#8211;mandir</code></dt>
<dd> echos the directory containing ncurses manpages</dd>
<dt><code>&#8211;terminfo</code></dt>
<dd> echos the $TERMINFO terminfo database path, e.g.,</dd>
<dl>
<dt>
</dt><dd> /etc/terminfo</dd></dl>
<dt><code>&#8211;terminfo-dirs</code></dt>
<dd> echos the $TERMINFO_DIRS directory list, e.g.,</dd>
<dl>
<dt>
</dt><dd> /etc/terminfo:/lib/terminfo:/usr/share/terminfo</dd></dl>
<dt><code>&#8211;termpath</code></dt>
<dd> echos the $TERMPATH termcap list, if support for termcap is configured.</dd>
<dt><code>&#8211;help</code></dt>
<dd> prints this message</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>curses</code>(3X) </p>
<p> This describes <code>ncurses</code> version 6.3 (patch 20211021). </p>
<h2>Index</h2>
