---
title: "blk_execute_rq(9)"
name: "blk_execute_rq"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_execute_rq/"
---

blk_execute_rq - insert a request into queue for execution

<h2>Synopsis</h2>

<pre><code>int blk_execute_rq(struct request_queue *q, struct gendisk *bd_disk, struct request *rq, int at_head);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>queue to insert the request in</dl>
 

 <i>bd_disk</i>
<dl><dd>matching gendisk</dl>
 

 <i>rq</i>
<dl><dd>request to insert</dl>
 

 <i>at_head</i>
<dl><dd>insert request at head or tail of queue</dl>

<h2>Description</h2>

Insert a fully prepared request at the back of the I/O scheduler queue for execution and wait for completion.

<h2>Copyright</h2>


