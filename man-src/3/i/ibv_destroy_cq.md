---
title: "ibv_destroy_cq(3)"
name: "ibv_destroy_cq"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_destroy_cq/"
description: "ibv_create_cq, ibv_destroy_cq – create or destroy a completion queue (CQ)"
---

<h2 class="name">NAME</h2>
<p> ibv_create_cq, ibv_destroy_cq &#8211; create or destroy a completion queue (CQ) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_cq *ibv_create_cq(struct ibv_context *context, int cqe,
                             void *cq_context,
                             struct ibv_comp_channel *channel,
                             int comp_vector);
int ibv_destroy_cq(struct ibv_cq *cq);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_create_cq()</code> creates a completion queue (CQ) with at least <i>cqe</i> entries for the RDMA device context <i>context</i>. The pointer <i>cq_context</i> will be used to set user context pointer of the CQ structure. The argument <i>channel</i> is optional; if not NULL, the completion channel <i>channel</i> will be used to return completion events. The CQ will use the completion vector <i>comp_vector</i> for signaling completion events; it must be at least zero and less than <i>context</i>-&gt;num_comp_vectors. </p>
<p> <code>ibv_destroy_cq()</code> destroys the CQ <i>cq</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_create_cq()</code> returns a pointer to the CQ, or NULL if the request fails. </p>
<p> <code>ibv_destroy_cq()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> <code>ibv_create_cq()</code> may create a CQ with size greater than or equal to the requested size. Check the cqe attribute in the returned CQ for the actual size. </p>
<p> <code>ibv_destroy_cq()</code> fails if any queue pair is still associated with this CQ.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_resize_cq/">ibv_resize_cq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_req_notify_cq/">ibv_req_notify_cq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_ack_cq_events/">ibv_ack_cq_events</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_qp/">ibv_create_qp</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
