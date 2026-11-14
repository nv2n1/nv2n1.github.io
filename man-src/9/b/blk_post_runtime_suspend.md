---
title: "blk_post_runtime_suspend(9)"
name: "blk_post_runtime_suspend"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_post_runtime_suspend/"
---

blk_post_runtime_suspend - Post runtime suspend processing

<h2>Synopsis</h2>

<pre><code>void blk_post_runtime_suspend(struct request_queue *q, int err);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the queue of the device</dl>
 

 <i>err</i>
<dl><dd>return value of the device's runtime_suspend function</dl>

<h2>Description</h2>

Update the queue's runtime status according to the return value of the device's runtime suspend function and mark last busy for the device so that PM core will try to auto suspend the device at a later time. 

 This function should be called near the end of the device's runtime_suspend callback.

<h2>Copyright</h2>


