---
title: "blk_queue_bypass_end(9)"
name: "blk_queue_bypass_end"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_bypass_end/"
---

blk_queue_bypass_end - leave queue bypass mode

<h2>Synopsis</h2>

<pre><code>void blk_queue_bypass_end(struct request_queue *q);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>queue of interest</dl>

<h2>Description</h2>

Leave bypass mode and restore the normal queueing behavior.

<h2>Copyright</h2>


