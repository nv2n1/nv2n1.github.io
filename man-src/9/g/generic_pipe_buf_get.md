---
title: "generic_pipe_buf_get(9)"
name: "generic_pipe_buf_get"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_pipe_buf_get/"
description: "generic_pipe_buf_get – get a reference to a struct pipe_buffer"
---

<p>generic_pipe_buf_get &#8211; get a reference to a struct pipe_buffer</p>
<h2>Synopsis</h2>
<pre><code>void generic_pipe_buf_get(struct pipe_inode_info *pipe, struct pipe_buffer *buf);</code></pre>
<h2>Arguments</h2>
<p><i>pipe</i></p>
<dl>
<dd>
<dd>the pipe that the buffer belongs to</dl>
<p> <i>buf</i></p>
<dl>
<dd>the buffer to get a reference to</dl>
<h2>Description</h2>
<p>This function grabs an extra reference to <i>buf</i>. It&#8217;s used in in the <code>tee</code> system call, when we duplicate the buffers in one pipe into another.</p>
<h2>Copyright</h2>
