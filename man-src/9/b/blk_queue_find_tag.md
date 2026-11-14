---
title: "blk_queue_find_tag(9)"
name: "blk_queue_find_tag"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_find_tag/"
---

blk_queue_find_tag - find a request by its tag and queue

<h2>Synopsis</h2>

<pre><code>struct request *blk_queue_find_tag(struct request_queue *q, int tag);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>The request queue for the device</dl>
 

 <i>tag</i>
<dl><dd>The tag of the request</dl>

<h2>Notes</h2>

Should be used when a device returns a tag and you want to match it with a request. 

 no locks need be held.

<h2>Copyright</h2>


