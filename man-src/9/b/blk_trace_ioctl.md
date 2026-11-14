---
title: "blk_trace_ioctl(9)"
name: "blk_trace_ioctl"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_trace_ioctl/"
---

blk_trace_ioctl - handle the ioctls associated with tracing

<h2>Synopsis</h2>

<pre><code>int blk_trace_ioctl(struct block_device *bdev, unsigned cmd, char __user *arg);</code></pre>

<h2>Arguments</h2>

<i>bdev</i>
<dl><dd><dd>the block device</dl>
 

 <i>cmd</i>
<dl><dd>the ioctl cmd</dl>
 

 <i>arg</i>
<dl><dd>the argument data, if any</dl>

<h2>Copyright</h2>


