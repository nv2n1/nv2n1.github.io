---
title: "blk_queue_start_tag(9)"
name: "blk_queue_start_tag"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_start_tag/"
---

blk_queue_start_tag - find a free tag and assign it

<h2>Synopsis</h2>

<pre><code>int blk_queue_start_tag(struct request_queue *q, struct request *rq);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>rq</i>
<dl><dd>the block request that needs tagging</dl>

<h2>Description</h2>

This can either be used as a stand-alone helper, or possibly be assigned as the queue prep_rq_fn (in which case struct request automagically gets a tag assigned). Note that this function assumes that any type of request can be queued! if this is not true for your device, you must check the request type before calling this function. The request will also be removed from the request queue, so it's the drivers responsibility to readd it if it should need to be restarted for some reason.

<h2>Notes</h2>

queue lock must be held.

<h2>Copyright</h2>


