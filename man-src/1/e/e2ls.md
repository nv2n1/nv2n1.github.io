---
title: "e2ls(1)"
name: "e2ls"
section: "1"
letter: "e"
url: "/docs/linux/man/1-e2ls/"
description: "e2ls – list files and directories on an ext2 filesystem"
---

<h2 class="name">NAME</h2>
<p> e2ls &#8211; list files and directories on an ext2 filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>e2ls</code> [<i>options</i>]<i> file_specification</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>e2ls</code> command is used to list files and directories on an ext2 filesystem. </p>
<p> Note: Files deleted via e2rm sometimes will show up even without the -D option. It is being investigated.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Show hidden directories.</p>
<dt><code>-c</code></p>
<dd> Sort by creation time (must include -t when using -l).</p>
<dt><code>-d </code><i>dir</i></p>
<dd> Open the ext2 filesystem specified by dir.</p>
<dt><code>-D</code></p>
<dd> Show deleted files bracketed with &gt;&lt;.</p>
<dt><code>-f</code></p>
<dd> No sorting of the file list.</p>
<dt><code>-i</code></p>
<dd> Show the inodes (very useful for the -l option).</p>
<dt><code>-l</code></p>
<dd> Long listing.</p>
<dt><code>-r</code></p>
<dd> Reverse the sort order.</p>
<dt><code>-t</code></p>
<dd> Sort by time.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-e2tools/">e2tools</a></code>(7), <code><a href="/docs/linux/man/1-e2ln/">e2ln</a></code>(1), <code><a href="/docs/linux/man/1-e2mv/">e2mv</a></code>(1), <code><a href="/docs/linux/man/1-e2mkdir/">e2mkdir</a></code>(1), <code><a href="/docs/linux/man/1-e2cp/">e2cp</a></code>(1), <code><a href="/docs/linux/man/1-e2rm/">e2rm</a></code>(1), <code><a href="/docs/linux/man/1-e2tail/">e2tail</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> The <code>e2tools</code> were written by Keith Sheffield &lt;sheff [at] pobox.com&gt;. </p>
<p> This manual page was written by Lucas Wall &lt;lwall [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
