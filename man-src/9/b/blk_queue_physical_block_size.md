---
title: "blk_queue_physical_block_size(9)"
name: "blk_queue_physical_block_size"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_physical_block_size/"
---

blk_queue_physical_block_size - set physical block size for the queue

<h2>Synopsis</h2>

<pre><code>void blk_queue_physical_block_size(struct request_queue *q, unsigned int size);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>size</i>
<dl><dd>the physical block size, in bytes</dl>

<h2>Description</h2>

This should be set to the lowest possible sector size that the hardware can operate on without reverting to read-modify-write operations.

<h2>Copyright</h2>


