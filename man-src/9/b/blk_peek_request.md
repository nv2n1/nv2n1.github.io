---
title: "blk_peek_request(9)"
name: "blk_peek_request"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_peek_request/"
description: "blk_peek_request – peek at the top of a request queue"
---

<p>blk_peek_request &#8211; peek at the top of a request queue</p>
<h2>Synopsis</h2>
<pre><code>struct request *blk_peek_request(struct request_queue *q);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>request queue to peek at</dl>
<h2>Description</h2>
<p>Return the request at the top of <i>q</i>. The returned request should be started using <code>blk_start_request</code> before LLD starts processing it.</p>
<h2>Return</h2>
<p>Pointer to the request at the top of <i>q</i> if available. Null otherwise.</p>
<h2>Context</h2>
<p>queue_lock must be held.</p>
<h2>Copyright</h2>
