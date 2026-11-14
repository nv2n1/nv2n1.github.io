---
title: "blk_rq_err_bytes(9)"
name: "blk_rq_err_bytes"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_rq_err_bytes/"
---

blk_rq_err_bytes - determine number of bytes till the next failure boundary

<h2>Synopsis</h2>

<pre><code>unsigned int blk_rq_err_bytes(const struct request *rq);</code></pre>

<h2>Arguments</h2>

<i>rq</i>
<dl><dd><dd>request to examine</dl>

<h2>Description</h2>

A request could be merge of IOs which require different failure handling. This function determines the number of bytes which can be failed from the beginning of the request without crossing into area which need to be retried further.

<h2>Return</h2>

The number of bytes to fail.

<h2>Context</h2>

queue_lock must be held.

<h2>Copyright</h2>


