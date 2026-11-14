---
title: "blk_post_runtime_resume(9)"
name: "blk_post_runtime_resume"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_post_runtime_resume/"
---

blk_post_runtime_resume - Post runtime resume processing

<h2>Synopsis</h2>

<pre><code>void blk_post_runtime_resume(struct request_queue *q, int err);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the queue of the device</dl>
 

 <i>err</i>
<dl><dd>return value of the device's runtime_resume function</dl>

<h2>Description</h2>

Update the queue's runtime status according to the return value of the device's runtime_resume function. If it is successfully resumed, process the requests that are queued into the device's queue when it is resuming and then mark last busy and initiate autosuspend for it. 

 This function should be called near the end of the device's runtime_resume callback.

<h2>Copyright</h2>


