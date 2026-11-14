---
title: "blk_queue_invalidate_tags(9)"
name: "blk_queue_invalidate_tags"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_invalidate_tags/"
---

blk_queue_invalidate_tags - invalidate all pending tags

<h2>Synopsis</h2>

<pre><code>void blk_queue_invalidate_tags(struct request_queue *q);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>

<h2>Description</h2>

Hardware conditions may dictate a need to stop all pending requests. In this case, we will safely clear the block side of the tag queue and readd all requests to the request queue in the right order.

<h2>Notes</h2>

queue lock must be held.

<h2>Copyright</h2>


