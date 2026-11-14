---
title: "seq_lseek(9)"
name: "seq_lseek"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_lseek/"
description: "seq_lseek – ->llseek method for sequential files."
---

<p>seq_lseek &#8211; -&gt;<code>llseek</code> method for sequential files.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>loff_t seq_lseek(struct file&nbsp;<wbr>*&nbsp;<wbr></code><i>file</i><code>, loff_t&nbsp;<wbr></code><i>offset</i><code>, int&nbsp;<wbr></code><i>whence</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>file</i></p>
<dl>
<dd>
<dd>the file in question</dl>
<p> <i>offset</i></p>
<dl>
<dd>new position</dl>
<p> <i>whence</i></p>
<dl>
<dd>0 for absolute, 1 for relative position</dl>
<h2>Description</h2>
<p>Ready-made -&gt;f_op-&gt;<code>llseek</code></p>
<h2>Copyright</h2>
