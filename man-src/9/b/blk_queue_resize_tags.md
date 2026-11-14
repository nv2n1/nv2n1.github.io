---
title: "blk_queue_resize_tags(9)"
name: "blk_queue_resize_tags"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_resize_tags/"
---

blk_queue_resize_tags - change the queueing depth

<h2>Synopsis</h2>

<pre><code>int blk_queue_resize_tags(struct request_queue *q, int new_depth);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>new_depth</i>
<dl><dd>the new max command queueing depth</dl>

<h2>Notes</h2>

Must be called with the queue lock held.

<h2>Copyright</h2>


