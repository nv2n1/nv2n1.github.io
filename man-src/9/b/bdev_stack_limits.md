---
title: "bdev_stack_limits(9)"
name: "bdev_stack_limits"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bdev_stack_limits/"
---

bdev_stack_limits - adjust queue limits for stacked drivers

<h2>Synopsis</h2>

<pre><code>int bdev_stack_limits(struct queue_limits *t, struct block_device *bdev, sector_t start);</code></pre>

<h2>Arguments</h2>

<i>t</i>
<dl><dd><dd>the stacking driver limits (top device)</dl>
 

 <i>bdev</i>
<dl><dd>the component block_device (bottom)</dl>
 

 <i>start</i>
<dl><dd>first data sector within component device</dl>

<h2>Description</h2>

Merges queue limits for a top device and a block_device. Returns 0 if alignment didn't change. Returns -1 if adding the bottom device caused misalignment.

<h2>Copyright</h2>


