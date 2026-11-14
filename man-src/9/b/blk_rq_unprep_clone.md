---
title: "blk_rq_unprep_clone(9)"
name: "blk_rq_unprep_clone"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_rq_unprep_clone/"
---

blk_rq_unprep_clone - Helper function to free all bios in a cloned request

<h2>Synopsis</h2>

<pre><code>void blk_rq_unprep_clone(struct request *rq);</code></pre>

<h2>Arguments</h2>

<i>rq</i>
<dl><dd><dd>the clone request to be cleaned up</dl>

<h2>Description</h2>

Free all bios in <i>rq</i> for a cloned request.

<h2>Copyright</h2>


