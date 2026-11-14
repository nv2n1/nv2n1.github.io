---
title: "splice_from_pipe_end(9)"
name: "splice_from_pipe_end"
section: "9"
letter: "s"
url: "/docs/linux/man/9-splice_from_pipe_end/"
description: "splice_from_pipe_end – finish splicing from pipe"
---

<p>splice_from_pipe_end &#8211; finish splicing from pipe</p>
<h2>Synopsis</h2>
<pre><code>void splice_from_pipe_end(struct pipe_inode_info *pipe, struct splice_desc *sd);</code></pre>
<h2>Arguments</h2>
<p><i>pipe</i></p>
<dl>
<dd>
<dd>pipe to splice from</dl>
<p> <i>sd</i></p>
<dl>
<dd>information about the splice operation</dl>
<h2>Description</h2>
<p>This function will wake up pipe writers if necessary. It should be called after a loop containing <code>splice_from_pipe_next</code> and <code>splice_from_pipe_feed</code>.</p>
<h2>Copyright</h2>
