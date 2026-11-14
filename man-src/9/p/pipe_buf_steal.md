---
title: "pipe_buf_steal(9)"
name: "pipe_buf_steal"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pipe_buf_steal/"
---

pipe_buf_steal - attempt to take ownership of a pipe_buffer

<h2>Synopsis</h2>

<pre><code>int pipe_buf_steal(struct pipe_inode_info *pipe, struct pipe_buffer *buf);</code></pre>

<h2>Arguments</h2>

<i>pipe</i>
<dl><dd><dd>the pipe that the buffer belongs to</dl>
 

 <i>buf</i>
<dl><dd>the buffer to attempt to steal</dl>

<h2>Copyright</h2>


