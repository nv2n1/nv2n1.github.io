---
title: "blk_set_stacking_limits(9)"
name: "blk_set_stacking_limits"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_set_stacking_limits/"
---

blk_set_stacking_limits - set default limits for stacking devices

<h2>Synopsis</h2>

<pre><code>void blk_set_stacking_limits(struct queue_limits *lim);</code></pre>

<h2>Arguments</h2>

<i>lim</i>
<dl><dd><dd>the queue_limits structure to reset</dl>

<h2>Description</h2>

Returns a queue_limit struct to its default state. Should be used by stacking drivers like DM that have no internal limits.

<h2>Copyright</h2>


