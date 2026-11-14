---
title: "splice_from_pipe(9)"
name: "splice_from_pipe"
section: "9"
letter: "s"
url: "/docs/linux/man/9-splice_from_pipe/"
description: "splice_from_pipe – splice data from a pipe to a file"
---

<p>splice_from_pipe &#8211; splice data from a pipe to a file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t splice_from_pipe(struct pipe_inode_info&nbsp;<wbr>*&nbsp;<wbr></code><i>pipe</i><code>, struct file&nbsp;<wbr>*&nbsp;<wbr></code><i>out</i><code>, loff_t&nbsp;<wbr>*&nbsp;<wbr></code><i>ppos</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>, unsigned int&nbsp;<wbr></code><i>flags</i><code>, splice_actor&nbsp;<wbr>*&nbsp;<wbr></code><i>actor</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>pipe</i></p>
<dl>
<dd>
<dd>pipe to splice from</dl>
<p> <i>out</i></p>
<dl>
<dd>file to splice to</dl>
<p> <i>ppos</i></p>
<dl>
<dd>position in <i>out</i></dl>
<p> <i>len</i></p>
<dl>
<dd>how many bytes to splice</dl>
<p> <i>flags</i></p>
<dl>
<dd>splice modifier flags</dl>
<p> <i>actor</i></p>
<dl>
<dd>handler that splices the data</dl>
<h2>Description</h2>
<p>See __splice_from_pipe. This function locks the pipe inode, otherwise it&#8217;s identical to <code>__splice_from_pipe</code>.</p>
<h2>Copyright</h2>
