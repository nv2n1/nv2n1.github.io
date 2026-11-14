---
title: "blk_queue_stack_limits(9)"
name: "blk_queue_stack_limits"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_stack_limits/"
---

blk_queue_stack_limits - inherit underlying queue limits for stacked drivers

<h2>Synopsis</h2>

<pre><code>void blk_queue_stack_limits(struct request_queue *t, struct request_queue *b);</code></pre>

<h2>Arguments</h2>

<i>t</i>
<dl><dd><dd>the stacking driver (top)</dl>
 

 <i>b</i>
<dl><dd>the underlying device (bottom)</dl>

<h2>Copyright</h2>


