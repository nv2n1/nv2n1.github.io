---
title: "blk_queue_io_opt(9)"
name: "blk_queue_io_opt"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_io_opt/"
---

blk_queue_io_opt - set optimal request size for the queue

<h2>Synopsis</h2>

<pre><code>void blk_queue_io_opt(struct request_queue *q, unsigned int opt);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>opt</i>
<dl><dd>optimal request size in bytes</dl>

<h2>Description</h2>

Storage devices may report an optimal I/O size, which is the device's preferred unit for sustained I/O. This is rarely reported for disk drives. For RAID arrays it is usually the stripe width or the internal track size. A properly aligned multiple of optimal_io_size is the preferred request size for workloads where sustained throughput is desired.

<h2>Copyright</h2>


