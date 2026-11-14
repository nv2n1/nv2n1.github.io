---
title: "splice_from_pipe_feed(9)"
name: "splice_from_pipe_feed"
section: "9"
letter: "s"
url: "/docs/linux/man/9-splice_from_pipe_feed/"
description: "splice_from_pipe_feed – feed available data from a pipe to a file"
---

<p>splice_from_pipe_feed &#8211; feed available data from a pipe to a file</p>
<h2>Synopsis</h2>
<pre><code>int splice_from_pipe_feed(struct pipe_inode_info *pipe, struct splice_desc *sd, splice_actor *actor);</code></pre>
<h2>Arguments</h2>
<p><i>pipe</i></p>
<dl>
<dd>
<dd>pipe to splice from</dl>
<p> <i>sd</i></p>
<dl>
<dd>information to <i>actor</i></dl>
<p> <i>actor</i></p>
<dl>
<dd>handler that splices the data</dl>
<h2>Description</h2>
<p>This function loops over the pipe and calls <i>actor</i> to do the actual moving of a single struct pipe_buffer to the desired destination. It returns when there&#8217;s no more buffers left in the pipe or if the requested number of bytes (<i>sd</i>-&gt;total_len) have been copied. It returns a positive number (one) if the pipe needs to be filled with more data, zero if the required number of bytes have been copied and -errno on error. </p>
<p> This, together with splice_from_pipe_{begin,end,next}, may be used to implement the functionality of <code>__splice_from_pipe</code> when locking is required around copying the pipe buffers to the destination.</p>
<h2>Copyright</h2>
