---
title: "blk_queue_update_dma_alignment(9)"
name: "blk_queue_update_dma_alignment"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_update_dma_alignment/"
---

blk_queue_update_dma_alignment - update dma length and memory alignment

<h2>Synopsis</h2>

<pre><code>void blk_queue_update_dma_alignment(struct request_queue *q, int mask);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>mask</i>
<dl><dd>alignment mask</dl>

<h2>Description</h2>

update required memory and length alignment for direct dma transactions. If the requested alignment is larger than the current alignment, then the current queue alignment is updated to the new value, otherwise it is left alone. The design of this is to allow multiple objects (driver, device, transport etc) to set their respective alignments without having them interfere.

<h2>Copyright</h2>


