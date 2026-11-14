---
title: "blk_start_queue_async(9)"
name: "blk_start_queue_async"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_start_queue_async/"
description: "blk_start_queue_async – asynchronously restart a previously stopped queue"
---

<p>blk_start_queue_async &#8211; asynchronously restart a previously stopped queue</p>
<h2>Synopsis</h2>
<pre><code>void blk_start_queue_async(struct request_queue *q);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>The struct request_queue in question</dl>
<h2>Description</h2>
<p><code>blk_start_queue_async</code> will clear the stop flag on the queue, and ensure that the request_fn for the queue is run from an async context.</p>
<h2>Copyright</h2>
