---
title: "blk_cleanup_queue(9)"
name: "blk_cleanup_queue"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_cleanup_queue/"
---

blk_cleanup_queue - shutdown a request queue

<h2>Synopsis</h2>

<pre><code>void blk_cleanup_queue(struct request_queue *q);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>request queue to shutdown</dl>

<h2>Description</h2>

Mark <i>q</i> DYING, drain all pending requests, mark <i>q</i> DEAD, destroy and put it. All future requests will be failed immediately with -ENODEV.

<h2>Copyright</h2>


