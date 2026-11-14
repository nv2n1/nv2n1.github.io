---
title: "get_request(9)"
name: "get_request"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_request/"
description: "get_request – get a free request"
---

<p>get_request &#8211; get a free request</p>
<h2>Synopsis</h2>
<pre><code>struct request *get_request(struct request_queue *q, int op, int op_flags, struct bio *bio, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>request_queue to allocate request from</dl>
<p> <i>op</i></p>
<dl>
<dd>REQ_OP_READ/REQ_OP_WRITE</dl>
<p> <i>op_flags</i></p>
<dl>
<dd>rq_flag_bits</dl>
<p> <i>bio</i></p>
<dl>
<dd>bio to allocate request for (can be <code>NULL</code>)</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>allocation mask</dl>
<h2>Description</h2>
<p>Get a free request from <i>q</i>. If <code>__GFP_DIRECT_RECLAIM</code> is set in <i>gfp_mask</i>, this function keeps retrying under memory pressure and fails iff <i>q</i> is dead. </p>
<p> Must be called with <i>q</i>-&gt;queue_lock held and, Returns ERR_PTR on failure, with <i>q</i>-&gt;queue_lock held. Returns request pointer on success, with <i>q</i>-&gt;queue_lock *not held*.</p>
<h2>Copyright</h2>
