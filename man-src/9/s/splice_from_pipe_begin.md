---
title: "splice_from_pipe_begin(9)"
name: "splice_from_pipe_begin"
section: "9"
letter: "s"
url: "/docs/linux/man/9-splice_from_pipe_begin/"
description: "splice_from_pipe_begin – start splicing from pipe"
---

<p>splice_from_pipe_begin &#8211; start splicing from pipe</p>
<h2>Synopsis</h2>
<pre><code>void splice_from_pipe_begin(struct splice_desc *sd);</code></pre>
<h2>Arguments</h2>
<p><i>sd</i></p>
<dl>
<dd>
<dd>information about the splice operation</dl>
<h2>Description</h2>
<p>This function should be called before a loop containing <code>splice_from_pipe_next</code> and <code>splice_from_pipe_feed</code> to initialize the necessary fields of <i>sd</i>.</p>
<h2>Copyright</h2>
