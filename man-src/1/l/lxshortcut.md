---
title: "lxshortcut(1)"
name: "lxshortcut"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxshortcut/"
description: "lxshortcut – desktop entry file editor"
---

<h2>NAME</h2>
<p> lxshortcut &#8211; desktop entry file editor</p>
<h2>SYNOPSIS</h2>
<p> <code>lxshortcut</code> [ -i <i>input-file</i> ] [ -o <i>output-file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> lxshortcut is a simple application that uses LibFM file properties dialog window to change properties of a desktop entry &#8211; icon, display name, path and arguments of execution, etc.</p>
<h2>OPTIONS</h2>
<p> At least one option should be specified and if <i>output-file</i> isn&#8217;t specified then <i>input-file</i> will be used to make a result &#8211; either full path or path in XDG specified user data directory for menu entries.</p>
<dl>
<dt><code>-i</code><i> input-file</i>, &#8211;input=<i>input-file</i></p>
<dd> use <i>input-file</i> as source for editing, it may be some XDG menu entry if no full path is specified or custom path to some file</p>
<dt><code>-o</code><i> output-file</i>, &#8211;output=<i>output-file</i></p>
<dd> write result into <i>output-file</i></dl>
<h2>SEE ALSO</h2>
<p> XDG Desktop Entry Specification</p>
<h2>AUTHOR</h2>
<p> lxshortcut was written by Hong Jen Yee &lt;pcman.tw [at] gmail.com&gt; and modified by Andriy Grytsenko &lt;andrej [at] rep.kiev.ua&gt;. </p>
<p> This manual page was written by Andriy Grytsenko &lt;andrej [at] rep.kiev.ua&gt;. </p>
<h2>Index</h2>
