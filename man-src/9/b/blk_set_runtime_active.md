---
title: "blk_set_runtime_active(9)"
name: "blk_set_runtime_active"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_set_runtime_active/"
---

blk_set_runtime_active - Force runtime status of the queue to be active

<h2>Synopsis</h2>

<pre><code>void blk_set_runtime_active(struct request_queue *q);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the queue of the device</dl>

<h2>Description</h2>

If the device is left runtime suspended during system suspend the resume hook typically resumes the device and corrects runtime status accordingly. However, that does not affect the queue runtime PM status which is still "suspended". This prevents processing requests from the queue. 

 This function can be used in driver's resume hook to correct queue runtime PM status and re-enable peeking requests from the queue. It should be called before first request is added to the queue.

<h2>Copyright</h2>


