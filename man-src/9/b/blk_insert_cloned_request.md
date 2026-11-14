---
title: "blk_insert_cloned_request(9)"
name: "blk_insert_cloned_request"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_insert_cloned_request/"
---

blk_insert_cloned_request - Helper for stacking drivers to submit a request

<h2>Synopsis</h2>

<pre><code>int blk_insert_cloned_request(struct request_queue *q, struct request *rq);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the queue to submit the request</dl>
 

 <i>rq</i>
<dl><dd>the request being queued</dl>

<h2>Copyright</h2>


