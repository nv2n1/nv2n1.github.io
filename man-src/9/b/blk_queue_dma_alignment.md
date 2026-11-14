---
title: "blk_queue_dma_alignment(9)"
name: "blk_queue_dma_alignment"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_dma_alignment/"
---

blk_queue_dma_alignment - set dma length and memory alignment

<h2>Synopsis</h2>

<pre><code>void blk_queue_dma_alignment(struct request_queue *q, int mask);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>mask</i>
<dl><dd>alignment mask</dl>

<h2>Description</h2>

set required memory and length alignment for direct dma transactions. this is used when building direct io requests for the queue.

<h2>Copyright</h2>


