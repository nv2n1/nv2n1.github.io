---
title: "splice_to_pipe(9)"
name: "splice_to_pipe"
section: "9"
letter: "s"
url: "/docs/linux/man/9-splice_to_pipe/"
description: "splice_to_pipe – fill passed data into a pipe"
---

<p>splice_to_pipe &#8211; fill passed data into a pipe</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t splice_to_pipe(struct pipe_inode_info&nbsp;<wbr>*&nbsp;<wbr></code><i>pipe</i><code>, struct splice_pipe_desc&nbsp;<wbr>*&nbsp;<wbr></code><i>spd</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>pipe</i></p>
<dl>
<dd>
<dd>pipe to fill</dl>
<p> <i>spd</i></p>
<dl>
<dd>data to fill</dl>
<h2>Description</h2>
<p><i>spd</i> contains a map of pages and len/offset tuples, along with the struct pipe_buf_operations associated with these pages. This function will link that data to the pipe.</p>
<h2>Copyright</h2>
