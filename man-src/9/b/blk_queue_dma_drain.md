---
title: "blk_queue_dma_drain(9)"
name: "blk_queue_dma_drain"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_dma_drain/"
description: "blk_queue_dma_drain – Set up a drain buffer for excess dma."
---

<p>blk_queue_dma_drain &#8211; Set up a drain buffer for excess dma.</p>
<h2>Synopsis</h2>
<pre><code>int blk_queue_dma_drain(struct request_queue *q, dma_drain_needed_fn *dma_drain_needed, void *buf, unsigned int size);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>the request queue for the device</dl>
<p> <i>dma_drain_needed</i></p>
<dl>
<dd>fn which returns non-zero if drain is necessary</dl>
<p> <i>buf</i></p>
<dl>
<dd>physically contiguous buffer</dl>
<p> <i>size</i></p>
<dl>
<dd>size of the buffer in bytes</dl>
<h2>Description</h2>
<p>Some devices have excess DMA problems and can&#8217;t simply discard (or zero fill) the unwanted piece of the transfer. They have to have a real area of memory to transfer it into. The use case for this is ATAPI devices in DMA mode. If the packet command causes a transfer bigger than the transfer size some HBAs will lock up if there aren&#8217;t DMA elements to contain the excess transfer. What this API does is adjust the queue so that the buf is always appended silently to the scatterlist.</p>
<h2>Note</h2>
<p>This routine adjusts max_hw_segments to make room for appending the drain buffer. If you call <code>blk_queue_max_segments</code> after calling this routine, you must set the limit to one fewer than your device can support otherwise there won&#8217;t be room for the drain buffer.</p>
<h2>Copyright</h2>
