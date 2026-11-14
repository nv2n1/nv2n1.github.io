---
title: "disk_stack_limits(9)"
name: "disk_stack_limits"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_stack_limits/"
---

disk_stack_limits - adjust queue limits for stacked drivers

<h2>Synopsis</h2>

<pre><code>void disk_stack_limits(struct gendisk *disk, struct block_device *bdev, sector_t offset);</code></pre>

<h2>Arguments</h2>

<i>disk</i>
<dl><dd><dd>MD/DM gendisk (top)</dl>
 

 <i>bdev</i>
<dl><dd>the underlying block device (bottom)</dl>
 

 <i>offset</i>
<dl><dd>offset to beginning of data within component device</dl>

<h2>Description</h2>

Merges the limits for a top level gendisk and a bottom level block_device.

<h2>Copyright</h2>


