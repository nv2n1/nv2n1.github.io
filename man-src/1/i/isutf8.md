---
title: "isutf8(1)"
name: "isutf8"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isutf8/"
description: "isutf8 – check whether files are valid UTF-8"
---

<h2 class="name">NAME</h2>
<p> isutf8 &#8211; check whether files are valid UTF-8 </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>isutf8</code> [<code>-hqliv</code>] [<code>&#8211;help</code>] [<code>&#8211;quiet</code>] [<code>&#8211;list</code>] [<code>&#8211;invert</code>] [<code>&#8211;verbose</code>] [[<i>file</i>&#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> <code>isutf8</code></p>
<dd>checks whether files are syntactically valid UTF-8. Input is either files named on the command line, or the standard input. Notices about files with invalid UTF-8 are printed to standard output.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print out a help summary.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Don&#8217;t print messages telling which files are invalid UTF-8, merely indicate it with the exit status.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
<dd> Print only the names of files containing invalid UTF-8.</dl>
<p> <code>-i</code>, <code>&#8211;invert</code></p>
<dl>
<dt>
<dd> Invert the selection: list UTF-8 compatible files.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Also print an hexdump-like view of the error and some context.</dl>
<h2>EXIT STATUS</h2>
<p> If the file is valid UTF-8, the exit status is zero. If the file is not valid UTF-8, or there is some error, the exit status is non-zero.</p>
<h2>AUTHOR</h2>
<p> Lars Wirzenius, Julien Palard</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-utf8/">utf8</a></code>(7) </p>
<h2>Index</h2>
