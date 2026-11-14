---
title: "blk_fetch_request(9)"
name: "blk_fetch_request"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_fetch_request/"
---

blk_fetch_request - fetch a request from a request queue

<h2>Synopsis</h2>

<pre><code>struct request *blk_fetch_request(struct request_queue *q);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>request queue to fetch a request from</dl>

<h2>Description</h2>

Return the request at the top of <i>q</i>. The request is started on return and LLD can start processing it immediately.

<h2>Return</h2>

Pointer to the request at the top of <i>q</i> if available. Null otherwise.

<h2>Context</h2>

queue_lock must be held.

<h2>Copyright</h2>


