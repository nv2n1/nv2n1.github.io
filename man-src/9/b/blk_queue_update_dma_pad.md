---
title: "blk_queue_update_dma_pad(9)"
name: "blk_queue_update_dma_pad"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_update_dma_pad/"
---

blk_queue_update_dma_pad - update pad mask

<h2>Synopsis</h2>

<pre><code>void blk_queue_update_dma_pad(struct request_queue *q, unsigned int mask);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>mask</i>
<dl><dd>pad mask</dl>

<h2>Description</h2>

Update dma pad mask. 

 Appending pad buffer to a request modifies the last entry of a scatter list such that it includes the pad buffer.

<h2>Copyright</h2>


