---
title: "blk_rq_map_user_iov(9)"
name: "blk_rq_map_user_iov"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_rq_map_user_iov/"
description: "blk_rq_map_user_iov – map user data to a request, for REQ_TYPE_BLOCK_PC usage"
---

<p>blk_rq_map_user_iov &#8211; map user data to a request, for REQ_TYPE_BLOCK_PC usage</p>
<h2>Synopsis</h2>
<pre><code>int blk_rq_map_user_iov(struct request_queue *q, struct request *rq, struct rq_map_data *map_data, const struct iov_iter *iter, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>request queue where request should be inserted</dl>
<p> <i>rq</i></p>
<dl>
<dd>request to map data to</dl>
<p> <i>map_data</i></p>
<dl>
<dd>pointer to the rq_map_data holding pages (if necessary)</dl>
<p> <i>iter</i></p>
<dl>
<dd>iovec iterator</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>memory allocation flags</dl>
<h2>Description</h2>
<p>Data will be mapped directly for zero copy I/O, if possible. Otherwise a kernel bounce buffer is used. </p>
<p> A matching <code>blk_rq_unmap_user</code> must be issued at the end of I/O, while still in process context.</p>
<h2>Note</h2>
<p>The mapped bio may need to be bounced through <code>blk_queue_bounce</code> before being submitted to the device, as pages mapped may be out of reach. It&#8217;s the callers responsibility to make sure this happens. The original bio must be passed back in to <code>blk_rq_unmap_user</code> for proper unmapping.</p>
<h2>Copyright</h2>
