---
title: "generic_splice_sendpage(9)"
name: "generic_splice_sendpage"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_splice_sendpage/"
description: "generic_splice_sendpage – splice data from a pipe to a socket"
---

<p>generic_splice_sendpage &#8211; splice data from a pipe to a socket</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t generic_splice_sendpage(struct pipe_inode_info&nbsp;<wbr>*&nbsp;<wbr></code><i>pipe</i><code>, struct file&nbsp;<wbr>*&nbsp;<wbr></code><i>out</i><code>, loff_t&nbsp;<wbr>*&nbsp;<wbr></code><i>ppos</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>, unsigned int&nbsp;<wbr></code><i>flags</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>pipe</i></p>
<dl>
<dd>
<dd>pipe to splice from</dl>
<p> <i>out</i></p>
<dl>
<dd>socket to write to</dl>
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
<p>Will send <i>len</i> bytes from the pipe to a network socket. No data copying is involved.</p>
<h2>Copyright</h2>
