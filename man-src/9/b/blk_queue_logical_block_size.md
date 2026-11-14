---
title: "blk_queue_logical_block_size(9)"
name: "blk_queue_logical_block_size"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_logical_block_size/"
---

blk_queue_logical_block_size - set logical block size for the queue

<h2>Synopsis</h2>

<pre><code>void blk_queue_logical_block_size(struct request_queue *q, unsigned short size);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>size</i>
<dl><dd>the logical block size, in bytes</dl>

<h2>Description</h2>

This should be set to the lowest possible block size that the storage device can address. The default of 512 covers most hardware.

<h2>Copyright</h2>


