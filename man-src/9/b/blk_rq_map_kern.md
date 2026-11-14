---
title: "blk_rq_map_kern(9)"
name: "blk_rq_map_kern"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_rq_map_kern/"
---

blk_rq_map_kern - map kernel data to a request, for REQ_TYPE_BLOCK_PC usage

<h2>Synopsis</h2>

<pre><code>int blk_rq_map_kern(struct request_queue *q, struct request *rq, void *kbuf, unsigned int len, gfp_t gfp_mask);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>request queue where request should be inserted</dl>
 

 <i>rq</i>
<dl><dd>request to fill</dl>
 

 <i>kbuf</i>
<dl><dd>the kernel buffer</dl>
 

 <i>len</i>
<dl><dd>length of user data</dl>
 

 <i>gfp_mask</i>
<dl><dd>memory allocation flags</dl>

<h2>Description</h2>

Data will be mapped directly if possible. Otherwise a bounce buffer is used. Can be called multiple times to append multiple buffers.

<h2>Copyright</h2>


