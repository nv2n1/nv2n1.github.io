---
title: "blk_execute_rq_nowait(9)"
name: "blk_execute_rq_nowait"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_execute_rq_nowait/"
---

blk_execute_rq_nowait - insert a request into queue for execution

<h2>Synopsis</h2>

<pre><code>void blk_execute_rq_nowait(struct request_queue *q, struct gendisk *bd_disk, struct request *rq, int at_head, rq_end_io_fn *done);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>queue to insert the request in</dl>
 

 <i>bd_disk</i>
<dl><dd>matching gendisk</dl>
 

 <i>rq</i>
<dl><dd>request to insert</dl>
 

 <i>at_head</i>
<dl><dd>insert request at head or tail of queue</dl>
 

 <i>done</i>
<dl><dd>I/O completion handler</dl>

<h2>Description</h2>

Insert a fully prepared request at the back of the I/O scheduler queue for execution. Don't wait for completion.

<h2>Note</h2>

This function will invoke <i>done</i> directly if the queue is dead.

<h2>Copyright</h2>


