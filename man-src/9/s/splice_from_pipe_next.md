---
title: "splice_from_pipe_next(9)"
name: "splice_from_pipe_next"
section: "9"
letter: "s"
url: "/docs/linux/man/9-splice_from_pipe_next/"
---

splice_from_pipe_next - wait for some data to splice from

<h2>Synopsis</h2>

<pre><code>int splice_from_pipe_next(struct pipe_inode_info *pipe, struct splice_desc *sd);</code></pre>

<h2>Arguments</h2>

<i>pipe</i>
<dl><dd><dd>pipe to splice from</dl>
 

 <i>sd</i>
<dl><dd>information about the splice operation</dl>

<h2>Description</h2>

This function will wait for some data and return a positive value (one) if pipe buffers are available. It will return zero or -errno if no more data needs to be spliced.

<h2>Copyright</h2>


