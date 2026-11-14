---
title: "blk_stack_limits(9)"
name: "blk_stack_limits"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_stack_limits/"
---

blk_stack_limits - adjust queue_limits for stacked devices

<h2>Synopsis</h2>

<pre><code>int blk_stack_limits(struct queue_limits *t, struct queue_limits *b, sector_t start);</code></pre>

<h2>Arguments</h2>

<i>t</i>
<dl><dd><dd>the stacking driver limits (top device)</dl>
 

 <i>b</i>
<dl><dd>the underlying queue limits (bottom, component device)</dl>
 

 <i>start</i>
<dl><dd>first data sector within component device</dl>

<h2>Description</h2>

This function is used by stacking drivers like MD and DM to ensure that all component devices have compatible block sizes and alignments. The stacking driver must provide a queue_limits struct (top) and then iteratively call the stacking function for all component (bottom) devices. The stacking function will attempt to combine the values and ensure proper alignment. 

 Returns 0 if the top and bottom queue_limits are compatible. The top device's block sizes and alignment offsets may be adjusted to ensure alignment with the bottom device. If no compatible sizes and alignments exist, -1 is returned and the resulting top queue_limits will have the misaligned flag set to indicate that the alignment_offset is undefined.

<h2>Copyright</h2>


