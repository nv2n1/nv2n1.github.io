---
title: "pipe_buf_get(9)"
name: "pipe_buf_get"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pipe_buf_get/"
---

pipe_buf_get - get a reference to a pipe_buffer

<h2>Synopsis</h2>

<pre><code>void pipe_buf_get(struct pipe_inode_info *pipe, struct pipe_buffer *buf);</code></pre>

<h2>Arguments</h2>

<i>pipe</i>
<dl><dd><dd>the pipe that the buffer belongs to</dl>
 

 <i>buf</i>
<dl><dd>the buffer to get a reference to</dl>

<h2>Copyright</h2>


