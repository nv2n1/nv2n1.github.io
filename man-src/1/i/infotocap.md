---
title: "infotocap(1)"
name: "infotocap"
section: "1"
letter: "i"
url: "/docs/linux/man/1-infotocap/"
description: "infotocap – convert a terminfo description into a termcap description"
---

<h2 class="name">NAME</h2>
<p> <code>infotocap</code> &#8211; convert a <i>terminfo</i> description into a <i>termcap</i> description </p>
<h2>SYNOPSIS</h2>
<p> <code>infotocap</code> [<code>-v</code><i>n</i> <i>width</i>] [<code>-V</code>] [<code>-1</code>] [<code>-w</code> <i>width</i>] <i>file</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>infotocap</code> looks in each given text <i>file</i> for <code>terminfo</code> descriptions. For each terminfo description found, an equivalent <code>termcap</code> description is written to standard output. Terminfo <code>use</code> capabilities are translated directly to termcap <code>tc</code> capabilities.</p>
<dl>
<dt><code>-v</code></p>
<dd> print out tracing information on standard error as the program runs.</p>
<dt><code>-V</code></p>
<dd> print out the version of the program in use on standard error and exit.</p>
<dt><code>-1</code></p>
<dd> cause the fields to print out one to a line. Otherwise, the fields will be printed several to a line to a maximum width of 60 characters.</p>
<dt><code>-w</code></p>
<dd> change the output to <i>width</i> characters.</dl>
<h2>FILES</h2>
<dl>
<dt>/etc/terminfo</p>
<dd> Compiled terminal description database.</dl>
<h2>NOTES</h2>
<p> This utility is actually a link to <code>tic</code>, running in <i>-C</i> mode. You can use other <code>tic</code> options such as <code>-f</code> and <code>-x</code>.</p>
<h2>PORTABILITY</h2>
<p> None of X/Open Curses, Issue 7 (2009), SVr4 or NetBSD document this application.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-infocmp/">infocmp</a></code>(1), <code><a href="/docs/linux/man/1-tic/">tic</a></code>(1), <code>ncurses</code>(3NCURSES), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) </p>
<p> This describes <code>ncurses</code> version 6.3 (patch 20211021).</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] snark.thyrsus.com&gt; and<br />
 Thomas E. Dickey &lt;dickey [at] invisible-island.net&gt; </p>
<h2>Index</h2>
