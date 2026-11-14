---
title: "blk_queue_max_segment_size(9)"
name: "blk_queue_max_segment_size"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_max_segment_size/"
---

blk_queue_max_segment_size - set max segment size for blk_rq_map_sg

<h2>Synopsis</h2>

<pre><code>void blk_queue_max_segment_size(struct request_queue *q, unsigned int max_size);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>max_size</i>
<dl><dd>max size of segment in bytes</dl>

<h2>Description</h2>

Enables a low level driver to set an upper limit on the size of a coalesced segment

<h2>Copyright</h2>


