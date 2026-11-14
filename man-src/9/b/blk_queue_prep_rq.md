---
title: "blk_queue_prep_rq(9)"
name: "blk_queue_prep_rq"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_prep_rq/"
---

blk_queue_prep_rq - set a prepare_request function for queue

<h2>Synopsis</h2>

<pre><code>void blk_queue_prep_rq(struct request_queue *q, prep_rq_fn *pfn);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>queue</dl>
 

 <i>pfn</i>
<dl><dd>prepare_request function</dl>

<h2>Description</h2>

It's possible for a queue to register a prepare_request callback which is invoked before the request is handed to the request_fn. The goal of the function is to prepare a request for I/O, it can be used to build a cdb from the request data for instance.

<h2>Copyright</h2>


