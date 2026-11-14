---
title: "seq_read(9)"
name: "seq_read"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_read/"
description: "seq_read – ->read method for sequential files."
---

<p>seq_read &#8211; -&gt;<code>read</code> method for sequential files.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t seq_read(struct file&nbsp;<wbr>*&nbsp;<wbr></code><i>file</i><code>, char&nbsp;<wbr>__user&nbsp;<wbr>*&nbsp;<wbr></code><i>buf</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>, loff_t&nbsp;<wbr>*&nbsp;<wbr></code><i>ppos</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>file</i></p>
<dl>
<dd>
<dd>the file to read from</dl>
<p> <i>buf</i></p>
<dl>
<dd>the buffer to read to</dl>
<p> <i>size</i></p>
<dl>
<dd>the maximum number of bytes to read</dl>
<p> <i>ppos</i></p>
<dl>
<dd>the current position in the file</dl>
<h2>Description</h2>
<p>Ready-made -&gt;f_op-&gt;<code>read</code></p>
<h2>Copyright</h2>
