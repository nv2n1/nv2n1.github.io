---
title: "calibre(1)"
name: "calibre"
section: "1"
letter: "c"
url: "/docs/linux/man/1-calibre/"
description: "calibre – launch Calibre Graphical User Interface"
---

<h2 class="name">NAME</h2>
<p> <code> calibre </code>&#8211; launch Calibre Graphical User Interface </p>
<h2>USAGE</h2>
<p> calibre [opts] [path_to_ebook]</p>
<h2>DESCRIPTION</h2>
<p> Launch the main calibre Graphical User Interface and optionally add the ebook at path_to_ebook to the database. </p>
<p> Whenever you pass arguments to calibre that have spaces in them, enclose the arguments in quotation marks.</p>
<h2>MAIN OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>&#8211;redirect-console-output</code></dt>
<dd> Redirect console output to a dialog window (both stdout and stderr). Useful on windows where GUI apps do not have a output streams.</dd>
<dt><code>&#8211;with-library</code>=WITH_LIBRARY</dt>
<dd> Use the library located at the specified path.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Log debugging information to console</dd></dl>
<h2>AUTHOR</h2>
<p> Created by Kovid Goyal &lt;kovid [at] kovidgoyal.net&gt; </p>
