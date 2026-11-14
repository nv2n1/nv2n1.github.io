---
title: "blk_queue_io_min(9)"
name: "blk_queue_io_min"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_io_min/"
---

blk_queue_io_min - set minimum request size for the queue

<h2>Synopsis</h2>

<pre><code>void blk_queue_io_min(struct request_queue *q, unsigned int min);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>min</i>
<dl><dd>smallest I/O size in bytes</dl>

<h2>Description</h2>

Storage devices may report a granularity or preferred minimum I/O size which is the smallest request the device can perform without incurring a performance penalty. For disk drives this is often the physical block size. For RAID arrays it is often the stripe chunk size. A properly aligned multiple of minimum_io_size is the preferred request size for workloads where a high number of I/O operations is desired.

<h2>Copyright</h2>


