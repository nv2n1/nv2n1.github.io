---
title: "blk_sync_queue(9)"
name: "blk_sync_queue"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_sync_queue/"
description: "blk_sync_queue – cancel any pending callbacks on a queue"
---

<p>blk_sync_queue &#8211; cancel any pending callbacks on a queue</p>
<h2>Synopsis</h2>
<pre><code>void blk_sync_queue(struct request_queue *q);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>the queue</dl>
<h2>Description</h2>
<p>The block layer may perform asynchronous callback activity on a queue, such as calling the unplug function after a timeout. A block device may call blk_sync_queue to ensure that any such activity is cancelled, thus allowing it to release resources that the callbacks might use. The caller must already have made sure that its -&gt;make_request_fn will not re-add plugging prior to calling this function. </p>
<p> This function does not cancel any asynchronous activity arising out of elevator or throttling code. That would require <code>elevator_exit</code> and <code>blkcg_exit_queue</code> to be called with queue lock initialized.</p>
<h2>Copyright</h2>
