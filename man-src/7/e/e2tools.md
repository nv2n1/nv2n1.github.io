---
title: "e2tools(7)"
name: "e2tools"
section: "7"
letter: "e"
url: "/docs/linux/man/7-e2tools/"
description: "e2tools – utilities to manipulate files in an ext2/ext3 filesystem"
---

<p>e2tools &#8211; utilities to manipulate files in an ext2/ext3 filesystem</p>
<h2>Description</h2>
<p>E2tools is a simple set of GPL&#8217;ed utilities to read, write, and manipulate files in an ext2/ext3 filesystem. These utilities access a filesystem directly using the ext2fs library. I wrote these tools in order to copy files into a linux filesystem on a machine that does not have ext2 support. Of course, they can also be used on a linux machine to read/write to disk images or floppies without having to mount them or have root access. </p>
<p> Supported functionality:</p>
<dl>
<dt><code>e2cp</code></p>
<dd>copy files</p>
<dt><code>e2mv</code></p>
<dd>move files</p>
<dt><code>e2rm</code></p>
<dd>remove files</p>
<dt><code>e2mkdir</code></p>
<dd>create directory</p>
<dt><code>e2ln</code></p>
<dd>create hard links</p>
<dt><code>e2ls</code></p>
<dd>list files/directories</p>
<dt><code>e2tail</code></p>
<dd>output the last part of a file</dl>
<p> In general, to specify a directory or file on an ext2 filesystem for the e2tools utilities, use the following form:</p>
<dl>
<dd>filesystem:directory_path</dl>
<p> The filesystem can be an unmounted partition or a regular file that&#8217;s been formatted to contain an ext2 filesystem. In general, if a command takes multiple file names on the command line, if the first one contains an ext2 file specification, the rest of the files are assumed to be on the same filesystem until another one is explicitly stated:</p>
<dl>
<dd>/tmp/boot.img:/tmp/file1</p>
<dd>/tmp/file2</p>
<dd>/tmp/file3</p>
<dd>/tmp/boot2.img:/tmp/file4</dl>
<p> Files 1-3 are on /tmp/boot.img and the last file is on /tmp/boot2.img</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-e2cp/">e2cp</a></code>(1), <code><a href="/docs/linux/man/1-e2ln/">e2ln</a></code>(1), <code><a href="/docs/linux/man/1-e2ls/">e2ls</a></code>(1), <code><a href="/docs/linux/man/1-e2mkdir/">e2mkdir</a></code>(1), <code><a href="/docs/linux/man/1-e2mv/">e2mv</a></code>(1), <code><a href="/docs/linux/man/1-e2rm/">e2rm</a></code>(1), <code><a href="/docs/linux/man/1-e2tail/">e2tail</a></code>(1).</p>
<h2>Author</h2>
<p>The <code>e2tools</code> were written by Keith Sheffield &lt;sheff [at] pobox.com&gt;. </p>
<p> This manual page was written by Lucas Wall &lt;lwall [at] debian.org&gt;, for the Debian project (but may be used by others).</p>
