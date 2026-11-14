---
title: "blk_init_queue(9)"
name: "blk_init_queue"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_init_queue/"
description: "blk_init_queue – prepare a request queue for use with a block device"
---

<p>blk_init_queue &#8211; prepare a request queue for use with a block device</p>
<h2>Synopsis</h2>
<pre><code>struct request_queue *blk_init_queue(request_fn_proc *rfn, spinlock_t *lock);</code></pre>
<h2>Arguments</h2>
<p><i>rfn</i></p>
<dl>
<dd>
<dd>The function to be called to process requests that have been placed on the queue.</dl>
<p> <i>lock</i></p>
<dl>
<dd>Request queue spin lock</dl>
<h2>Description</h2>
<p>If a block device wishes to use the standard request handling procedures, which sorts requests and coalesces adjacent requests, then it must call <code>blk_init_queue</code>. The function <i>rfn</i> will be called when there are requests on the queue that need to be processed. If the device supports plugging, then <i>rfn</i> may not be called immediately when requests are available on the queue, but may be called at some time later instead. Plugged queues are generally unplugged when a buffer belonging to one of the requests on the queue is needed, or due to memory pressure. </p>
<p> <i>rfn</i> is not required, or even expected, to remove all requests off the queue, but only as many as it can handle at a time. If it does leave requests on the queue, it is responsible for arranging that the requests get dealt with eventually. </p>
<p> The queue spin lock must be held while manipulating the requests on the request queue; this lock will be taken also from interrupt context, so irq disabling is needed for it. </p>
<p> Function returns a pointer to the initialized request queue, or <code>NULL</code> if it didn&#8217;t succeed.</p>
<h2>Note</h2>
<p><code>blk_init_queue</code> must be paired with a <code>blk_cleanup_queue</code> call when the block device is deactivated (such as at module unload).</p>
<h2>Copyright</h2>
