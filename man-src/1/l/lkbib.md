---
title: "lkbib(1)"
name: "lkbib"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lkbib/"
description: "lkbib – search bibliographic databases"
---

<h2 class="name">NAME</h2>
<p> lkbib &#8211; search bibliographic databases </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-n</code> ] [ <code>-i </code><i>fields</i> ] [ <code>-p </code><i>filename</i> ] [ <code>-t </code><i>n</i> ] <i>key</i> &#8230; <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <i>lkbib</i> searches bibliographic databases for references that contain the keys <i>key</i> &#8230; and prints any references found on the standard output. <i>lkbib</i> will search any databases given by <code>-p</code> options, and then a default database. The default database is taken from the <i>REFER</i> environment variable if it is set, otherwise it is <i>/usr/:dict/:papers/:Ind</i>. For each database <i>filename</i> to be searched, if an index filename<i>.i</i> created by <i><a href="/docs/linux/man/1-indxbib/">indxbib</a></i>(1) exists, then it will be searched instead; each index can cover multiple databases.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display a usage message and exit.</p>
<dt><code>-i</code><i>string</i></p>
<dd> When searching files for which no index exists, ignore the contents of fields whose names are in <i>string</i>.</p>
<dt><code>-p</code><i>filename</i></p>
<dd> Search <i>filename</i>. Multiple <code>-p</code> options can be used.</p>
<dt><code>-t</code><i>n</i></p>
<dd> Only require the first <i>n</i> characters of keys to be given. Initially <i>n</i> is~6.</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;version</code> Display version information and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>REFER</i></p>
<dd> Default database.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/:dict/:papers/:Ind</i></p>
<dd> Default database to be used if the <i>REFER</i> environment variable is not set.</p>
<dt>filename<i>.i</i></p>
<dd> Index files.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-refer/">refer</a></i>(1), <i><a href="/docs/linux/man/1-lookbib/">lookbib</a></i>(1), <i><a href="/docs/linux/man/1-indxbib/">indxbib</a></i>(1) </p>
<h2>Index</h2>
