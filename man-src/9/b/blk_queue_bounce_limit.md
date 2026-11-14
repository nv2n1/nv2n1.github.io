---
title: "blk_queue_bounce_limit(9)"
name: "blk_queue_bounce_limit"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_bounce_limit/"
---

blk_queue_bounce_limit - set bounce buffer limit for queue

<h2>Synopsis</h2>

<pre><code>void blk_queue_bounce_limit(struct request_queue *q, u64 max_addr);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the request queue for the device</dl>
 

 <i>max_addr</i>
<dl><dd>the maximum address the device can handle</dl>

<h2>Description</h2>

Different hardware can have different requirements as to what pages it can do I/O directly to. A low level driver can call blk_queue_bounce_limit to have lower memory pages allocated as bounce buffers for doing I/O to pages residing above <i>max_addr</i>.

<h2>Copyright</h2>


