---
title: "iter_file_splice_write(9)"
name: "iter_file_splice_write"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iter_file_splice_write/"
description: "iter_file_splice_write – splice data from a pipe to a file"
---

<p>iter_file_splice_write &#8211; splice data from a pipe to a file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t iter_file_splice_write(struct pipe_inode_info&nbsp;<wbr>*&nbsp;<wbr></code><i>pipe</i><code>, struct file&nbsp;<wbr>*&nbsp;<wbr></code><i>out</i><code>, loff_t&nbsp;<wbr>*&nbsp;<wbr></code><i>ppos</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>, unsigned int&nbsp;<wbr></code><i>flags</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>pipe</i></p>
<dl>
<dd>
<dd>pipe info</dl>
<p> <i>out</i></p>
<dl>
<dd>file to write to</dl>
<p> <i>ppos</i></p>
<dl>
<dd>position in <i>out</i></dl>
<p> <i>len</i></p>
<dl>
<dd>number of bytes to splice</dl>
<p> <i>flags</i></p>
<dl>
<dd>splice modifier flags</dl>
<h2>Description</h2>
<p>Will either move or copy pages (determined by <i>flags</i> options) from the given pipe inode to the given file. This one is -&gt;write_iter-based.</p>
<h2>Copyright</h2>
