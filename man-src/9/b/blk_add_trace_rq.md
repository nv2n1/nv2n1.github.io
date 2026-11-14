---
title: "blk_add_trace_rq(9)"
name: "blk_add_trace_rq"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_add_trace_rq/"
---

blk_add_trace_rq - Add a trace for a request oriented action

<h2>Synopsis</h2>

<pre><code>void blk_add_trace_rq(struct request_queue *q, struct request *rq, unsigned int nr_bytes, u32 what);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>queue the io is for</dl>
 

 <i>rq</i>
<dl><dd>the source request</dl>
 

 <i>nr_bytes</i>
<dl><dd>number of completed bytes</dl>
 

 <i>what</i>
<dl><dd>the action</dl>

<h2>Description</h2>

Records an action against a request. Will log the bio offset + size.

<h2>Copyright</h2>


