---
title: "blk_queue_free_tags(9)"
name: "blk_queue_free_tags"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_free_tags/"
---

blk_queue_free_tags - release tag maintenance info

<h2>Synopsis</h2>

<pre><code>void blk_queue_free_tags(struct request_queue *q);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>

<h2>Notes</h2>

This is used to disable tagged queuing to a device, yet leave queue in function.

<h2>Copyright</h2>


