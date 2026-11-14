---
title: "blk_queue_end_tag(9)"
name: "blk_queue_end_tag"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_end_tag/"
description: "blk_queue_end_tag – end tag operations for a request"
---

<p>blk_queue_end_tag &#8211; end tag operations for a request</p>
<h2>Synopsis</h2>
<pre><code>void blk_queue_end_tag(struct request_queue *q, struct request *rq);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>the request queue for the device</dl>
<p> <i>rq</i></p>
<dl>
<dd>the request that has completed</dl>
<h2>Description</h2>
<p>Typically called when <code>end_that_request_first</code> returns <code>0</code>, meaning all transfers have been done for a request. It&#8217;s important to call this function before <code>end_that_request_last</code>, as that will put the request back on the free list thus corrupting the internal tag list.</p>
<h2>Notes</h2>
<p>queue lock must be held.</p>
<h2>Copyright</h2>
