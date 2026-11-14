---
title: "blk_queue_unprep_rq(9)"
name: "blk_queue_unprep_rq"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_unprep_rq/"
---

blk_queue_unprep_rq - set an unprepare_request function for queue

<h2>Synopsis</h2>

<pre><code>void blk_queue_unprep_rq(struct request_queue *q, unprep_rq_fn *ufn);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>queue</dl>
 

 <i>ufn</i>
<dl><dd>unprepare_request function</dl>

<h2>Description</h2>

It's possible for a queue to register an unprepare_request callback which is invoked before the request is finally completed. The goal of the function is to deallocate any data that was allocated in the prepare_request callback.

<h2>Copyright</h2>


