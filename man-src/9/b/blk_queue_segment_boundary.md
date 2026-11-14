---
title: "blk_queue_segment_boundary(9)"
name: "blk_queue_segment_boundary"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_segment_boundary/"
---

blk_queue_segment_boundary - set boundary rules for segment merging

<h2>Synopsis</h2>

<pre><code>void blk_queue_segment_boundary(struct request_queue *q, unsigned long mask);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>mask</i>
<dl><dd>the memory boundary mask</dl>

<h2>Copyright</h2>


