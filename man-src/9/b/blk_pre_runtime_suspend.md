---
title: "blk_pre_runtime_suspend(9)"
name: "blk_pre_runtime_suspend"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_pre_runtime_suspend/"
---

blk_pre_runtime_suspend - Pre runtime suspend check

<h2>Synopsis</h2>

<pre><code>int blk_pre_runtime_suspend(struct request_queue *q);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the queue of the device</dl>

<h2>Description</h2>

This function will check if runtime suspend is allowed for the device by examining if there are any requests pending in the queue. If there are requests pending, the device can not be runtime suspended; otherwise, the queue's status will be updated to SUSPENDING and the driver can proceed to suspend the device. 

 For the not allowed case, we mark last busy for the device so that runtime PM core will try to autosuspend it some time later. 

 This function should be called near the start of the device's runtime_suspend callback.

<h2>Return</h2>

0 - OK to runtime suspend the device -EBUSY - Device should not be runtime suspended

<h2>Copyright</h2>


