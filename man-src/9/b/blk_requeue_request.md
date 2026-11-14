---
title: "blk_requeue_request(9)"
name: "blk_requeue_request"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_requeue_request/"
---

blk_requeue_request - put a request back on queue

<h2>Synopsis</h2>

<pre><code>void blk_requeue_request(struct request_queue *q, struct request *rq);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>request queue where request should be inserted</dl>
 

 <i>rq</i>
<dl><dd>request to be inserted</dl>

<h2>Description</h2>

Drivers often keep queueing requests until the hardware cannot accept more, when that condition happens we need to put the request back on the queue. Must be called with queue lock held.

<h2>Copyright</h2>


