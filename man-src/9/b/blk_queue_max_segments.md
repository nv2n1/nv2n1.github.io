---
title: "blk_queue_max_segments(9)"
name: "blk_queue_max_segments"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_max_segments/"
---

blk_queue_max_segments - set max hw segments for a request for this queue

<h2>Synopsis</h2>

<pre><code>void blk_queue_max_segments(struct request_queue *q, unsigned short max_segments);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>max_segments</i>
<dl><dd>max number of segments</dl>

<h2>Description</h2>

Enables a low level driver to set an upper limit on the number of hw data segments in a request.

<h2>Copyright</h2>


