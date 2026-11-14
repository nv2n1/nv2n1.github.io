---
title: "calibre-debug(1)"
name: "calibre-debug"
section: "1"
letter: "c"
url: "/docs/linux/man/1-calibre-debug/"
description: "calibre-debug – run an embedded python interpreter for debug purposes"
---

<h2 class="name">NAME</h2>
<p> <code> calibre-debug </code>&#8211; run an embedded python interpreter for debug purposes </p>
<h2>USAGE</h2>
<p> calibre-debug [options]</p>
<h2>DESCRIPTION</h2>
<p> Run an embedded python interpreter. </p>
<p> Whenever you pass arguments to calibre-debug that have spaces in them, enclose the arguments in quotation marks.</p>
<h2>MAIN OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>&#8211;update-module</code>=UPDATE_MODULE</p>
<dd> Update the specified module in the frozen library. Module specifications are of the form full.name.of.module,path_to_module.py</p>
<dt><code>-c</code> COMMAND, <code>&#8211;command</code>=COMMAND</p>
<dd> Run python code.</p>
<dt><code>-g</code>, <code>&#8211;gui</code></p>
<dd> Run the GUI</p>
<dt><code>&#8211;migrate</code></p>
<dd> Migrate old database. Needs two arguments. Path to library1.db and path to new library folder.</dl>
<h2>AUTHOR</h2>
<p> Created by Kovid Goyal &lt;kovid [at] kovidgoyal.net&gt; </p>
<h2>Index</h2>
