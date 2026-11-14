---
title: "generic_pipe_buf_confirm(9)"
name: "generic_pipe_buf_confirm"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_pipe_buf_confirm/"
---

generic_pipe_buf_confirm - verify contents of the pipe buffer

<h2>Synopsis</h2>

<pre><code>int generic_pipe_buf_confirm(struct pipe_inode_info *info, struct pipe_buffer *buf);</code></pre>

<h2>Arguments</h2>

<i>info</i>
<dl><dd><dd>the pipe that the buffer belongs to</dl>
 

 <i>buf</i>
<dl><dd>the buffer to confirm</dl>

<h2>Description</h2>

This function does nothing, because the generic pipe code uses pages that are always good when inserted into the pipe.

<h2>Copyright</h2>


