---
title: "generic_pipe_buf_release(9)"
name: "generic_pipe_buf_release"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_pipe_buf_release/"
---

generic_pipe_buf_release - put a reference to a struct pipe_buffer

<h2>Synopsis</h2>

<pre><code>void generic_pipe_buf_release(struct pipe_inode_info *pipe, struct pipe_buffer *buf);</code></pre>

<h2>Arguments</h2>

<i>pipe</i>
<dl><dd><dd>the pipe that the buffer belongs to</dl>
 

 <i>buf</i>
<dl><dd>the buffer to put a reference to</dl>

<h2>Description</h2>

This function releases a reference to <i>buf</i>.

<h2>Copyright</h2>


