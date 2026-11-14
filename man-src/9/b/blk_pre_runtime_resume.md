---
title: "blk_pre_runtime_resume(9)"
name: "blk_pre_runtime_resume"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_pre_runtime_resume/"
---

blk_pre_runtime_resume - Pre runtime resume processing

<h2>Synopsis</h2>

<pre><code>void blk_pre_runtime_resume(struct request_queue *q);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the queue of the device</dl>

<h2>Description</h2>

Update the queue's runtime status to RESUMING in preparation for the runtime resume of the device. 

 This function should be called near the start of the device's runtime_resume callback.

<h2>Copyright</h2>


