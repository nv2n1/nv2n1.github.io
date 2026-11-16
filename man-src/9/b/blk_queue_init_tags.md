---
title: "blk_queue_init_tags(9)"
name: "blk_queue_init_tags"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_init_tags/"
---

blk_queue_init_tags - initialize the queue tag info

<h2>Synopsis</h2>

<pre><code>int blk_queue_init_tags(struct request_queue *q, int depth, struct blk_queue_tag *tags, int alloc_policy);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd></dd><dd>the request queue for the device</dd></dl>
 

 <i>depth</i>
<dl><dd>the maximum queue depth supported</dd></dl>
 

 <i>tags</i>
<dl><dd>the tag to use</dd></dl>
 

 <i>alloc_policy</i>
<dl><dd>tag allocation policy</dd></dl>

<h2>Description</h2>

Queue lock must be held here if the function is called to resize an existing map.

<h2>Copyright</h2>


