---
title: "blk_cloned_rq_check_limits(9)"
name: "blk_cloned_rq_check_limits"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_cloned_rq_check_limits/"
---

blk_cloned_rq_check_limits - Helper function to check a cloned request for new the queue limits

<h2>Synopsis</h2>

<pre><code>int blk_cloned_rq_check_limits(struct request_queue *q, struct request *rq);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the queue</dl>
 

 <i>rq</i>
<dl><dd>the request being checked</dl>

<h2>Description</h2>

<i>rq</i> may have been made based on weaker limitations of upper-level queues in request stacking drivers, and it may violate the limitation of <i>q</i>. Since the block layer and the underlying device driver trust <i>rq</i> after it is inserted to <i>q</i>, it should be checked against <i>q</i> before the insertion using this generic function. 

 Request stacking drivers like request-based dm may change the queue limits when retrying requests on other queues. Those requests need to be checked against the new queue limits again during dispatch.

<h2>Copyright</h2>


