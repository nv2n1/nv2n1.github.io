---
title: "lookbib(1)"
name: "lookbib"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lookbib/"
description: "lookbib – search bibliographic databases"
---

<h2 class="name">NAME</h2>
<p> lookbib &#8211; search bibliographic databases </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-i </code><i>string</i> ] [ <code>-t </code><i>n</i> ] <i>filename</i> &#8230; <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <i>lookbib</i> prints a prompt on the standard error (unless the standard input is not a terminal), reads from the standard input a line containing a set of keywords, searches the bibliographic databases <i>filename</i> &#8230; for references containing those keywords, prints any references found on the standard output, and repeats this process until the end of input. For each database <i>filename</i> to be searched, if an index filename<i>.i</i> created by <i><a href="/docs/linux/man/1-indxbib/">indxbib</a></i>(1) exists, then it will be searched instead; each index can cover multiple databases.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display a usage message and exit.</p>
<dt><code>-i</code><i>string</i></p>
<dd> When searching files for which no index exists, ignore the contents of fields whose names are in <i>string</i>.</p>
<dt><code>-t</code><i>n</i></p>
<dd> Only require the first <i>n</i> characters of keys to be given. Initially <i>n</i> is~6.</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;version</code> Display version information and exit.</dl>
<h2>FILES</h2>
<dl>
<dt>filename<i>.i</i></p>
<dd> Index files.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-refer/">refer</a></i>(1), <i><a href="/docs/linux/man/1-lkbib/">lkbib</a></i>(1), <i><a href="/docs/linux/man/1-indxbib/">indxbib</a></i>(1) </p>
<h2>Index</h2>
