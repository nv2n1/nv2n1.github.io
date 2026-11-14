---
title: "stest(1)"
name: "stest"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stest/"
description: "stest – filter a list of files by properties"
---

<h2>NAME</h2>
<p> stest &#8211; filter a list of files by properties</p>
<h2>SYNOPSIS</h2>
<p> <code>stest</code> [<code>-abcdefghlpqrsuwx</code>] [<code>-n</code> <i>file</i>] [<code>-o</code> <i>file</i>] [<i>file</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>stest</code> takes a list of files and filters by the files&#8217; properties, analogous to <i><a href="/docs/linux/man/1-test/">test</a></i>(1). Files which pass all tests are printed to stdout. If no files are given, stest reads files from stdin.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Test hidden files.</p>
<dt><code>-b</code></p>
<dd> Test that files are block specials.</p>
<dt><code>-c</code></p>
<dd> Test that files are character specials.</p>
<dt><code>-d</code></p>
<dd> Test that files are directories.</p>
<dt><code>-e</code></p>
<dd> Test that files exist.</p>
<dt><code>-f</code></p>
<dd> Test that files are regular files.</p>
<dt><code>-g</code></p>
<dd> Test that files have their set-group-ID flag set.</p>
<dt><code>-h</code></p>
<dd> Test that files are symbolic links.</p>
<dt><code>-l</code></p>
<dd> Test the contents of a directory given as an argument.</p>
<dt><code>-n</code><i> file</i></p>
<dd> Test that files are newer than <i>file</i>.</p>
<dt><code>-o</code><i> file</i></p>
<dd> Test that files are older than <i>file</i>.</p>
<dt><code>-p</code></p>
<dd> Test that files are named pipes.</p>
<dt><code>-q</code></p>
<dd> No files are printed, only the exit status is returned.</p>
<dt><code>-r</code></p>
<dd> Test that files are readable.</p>
<dt><code>-s</code></p>
<dd> Test that files are not empty.</p>
<dt><code>-u</code></p>
<dd> Test that files have their set-user-ID flag set.</p>
<dt><code>-v</code></p>
<dd> Invert the sense of tests, only failing files pass.</p>
<dt><code>-w</code></p>
<dd> Test that files are writable.</p>
<dt><code>-x</code></p>
<dd> Test that files are executable.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> At least one file passed all tests.</p>
<dt><code>1</code></p>
<dd> No files passed all tests.</p>
<dt><code>2</code></p>
<dd> An error occurred.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dmenu/">dmenu</a></i>(1), <i><a href="/docs/linux/man/1-test/">test</a></i>(1) </p>
<h2>Index</h2>
