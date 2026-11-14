---
title: "blk_add_trace_bio(9)"
name: "blk_add_trace_bio"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_add_trace_bio/"
---

blk_add_trace_bio - Add a trace for a bio oriented action

<h2>Synopsis</h2>

<pre><code>void blk_add_trace_bio(struct request_queue *q, struct bio *bio, u32 what, int error);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>queue the io is for</dl>
 

 <i>bio</i>
<dl><dd>the source bio</dl>
 

 <i>what</i>
<dl><dd>the action</dl>
 

 <i>error</i>
<dl><dd>error, if any</dl>

<h2>Description</h2>

Records an action against a bio. Will log the bio offset + size.

<h2>Copyright</h2>


