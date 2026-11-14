---
title: "blk_limits_io_min(9)"
name: "blk_limits_io_min"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_limits_io_min/"
---

blk_limits_io_min - set minimum request size for a device

<h2>Synopsis</h2>

<pre><code>void blk_limits_io_min(struct queue_limits *limits, unsigned int min);</code></pre>

<h2>Arguments</h2>

<i>limits</i>
<dl><dd><dd>the queue limits</dl>
 

 <i>min</i>
<dl><dd>smallest I/O size in bytes</dl>

<h2>Description</h2>

Some devices have an internal block size bigger than the reported hardware sector size. This function can be used to signal the smallest I/O the device can perform without incurring a performance penalty.

<h2>Copyright</h2>


