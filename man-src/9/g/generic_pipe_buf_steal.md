---
title: "generic_pipe_buf_steal(9)"
name: "generic_pipe_buf_steal"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_pipe_buf_steal/"
---

generic_pipe_buf_steal - attempt to take ownership of a pipe_buffer

<h2>Synopsis</h2>

<pre><code>int generic_pipe_buf_steal(struct pipe_inode_info *pipe, struct pipe_buffer *buf);</code></pre>

<h2>Arguments</h2>

<i>pipe</i>
<dl><dd><dd>the pipe that the buffer belongs to</dl>
 

 <i>buf</i>
<dl><dd>the buffer to attempt to steal</dl>

<h2>Description</h2>

This function attempts to steal the struct page attached to <i>buf</i>. If successful, this function returns 0 and returns with the page locked. The caller may then reuse the page for whatever he wishes; the typical use is insertion into a different file page cache.

<h2>Copyright</h2>


