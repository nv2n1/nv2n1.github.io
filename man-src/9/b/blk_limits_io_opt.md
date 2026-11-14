---
title: "blk_limits_io_opt(9)"
name: "blk_limits_io_opt"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_limits_io_opt/"
---

blk_limits_io_opt - set optimal request size for a device

<h2>Synopsis</h2>

<pre><code>void blk_limits_io_opt(struct queue_limits *limits, unsigned int opt);</code></pre>

<h2>Arguments</h2>

<i>limits</i>
<dl><dd><dd>the queue limits</dl>
 

 <i>opt</i>
<dl><dd>smallest I/O size in bytes</dl>

<h2>Description</h2>

Storage devices may report an optimal I/O size, which is the device's preferred unit for sustained I/O. This is rarely reported for disk drives. For RAID arrays it is usually the stripe width or the internal track size. A properly aligned multiple of optimal_io_size is the preferred request size for workloads where sustained throughput is desired.

<h2>Copyright</h2>


