---
title: "generic_file_splice_read(9)"
name: "generic_file_splice_read"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_file_splice_read/"
description: "generic_file_splice_read – splice data from file to a pipe"
---

<p>generic_file_splice_read &#8211; splice data from file to a pipe</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t generic_file_splice_read(struct file&nbsp;<wbr>*&nbsp;<wbr></code><i>in</i><code>, loff_t&nbsp;<wbr>*&nbsp;<wbr></code><i>ppos</i><code>, struct pipe_inode_info&nbsp;<wbr>*&nbsp;<wbr></code><i>pipe</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>, unsigned int&nbsp;<wbr></code><i>flags</i><code>);</code></dt></dl>
<h2>Arguments</h2>
<p><i>in</i></p>
<dl>
<dd>
</dd><dd>file to splice from</dd></dl>
<p> <i>ppos</i></p>
<dl>
<dd>position in <i>in</i></dd></dl>
<p> <i>pipe</i></p>
<dl>
<dd>pipe to splice to</dd></dl>
<p> <i>len</i></p>
<dl>
<dd>number of bytes to splice</dd></dl>
<p> <i>flags</i></p>
<dl>
<dd>splice modifier flags</dd></dl>
<h2>Description</h2>
<p>Will read pages from given file and fill them into a pipe. Can be used as long as it has more or less sane -&gt;<code>read_iter</code>.</p>
<h2>Copyright</h2>
