---
title: "blk_run_queue_async(9)"
name: "blk_run_queue_async"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_run_queue_async/"
---

blk_run_queue_async - run a single device queue in workqueue context

<h2>Synopsis</h2>

<pre><code>void blk_run_queue_async(struct request_queue *q);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>The queue to run</dl>

<h2>Description</h2>

Tells kblockd to perform the equivalent of <i>blk_run_queue</i> on behalf of us. The caller must hold the queue lock.

<h2>Copyright</h2>


