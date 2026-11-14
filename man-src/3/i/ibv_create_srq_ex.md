---
title: "ibv_create_srq_ex(3)"
name: "ibv_create_srq_ex"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_create_srq_ex/"
description: "ibv_create_srq_ex, ibv_destroy_srq – create or destroy a shared receive queue (SRQ)"
---

<h2 class="name">NAME</h2>
<p> ibv_create_srq_ex, ibv_destroy_srq &#8211; create or destroy a shared receive queue (SRQ) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_srq *ibv_create_srq_ex(struct ibv_context *context, struct
                                  ibv_srq_init_attr_ex *srq_init_attr_ex);
int ibv_destroy_srq(struct ibv_srq *srq);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_create_srq_ex()</code> creates a shared receive queue (SRQ) supporting both basic and xrc modes. The argument <i>srq_init_attr_ex</i> is an ibv_srq_init_attr_ex struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_srq_init_attr_ex {
    void *srq_context;          /* Associated context of the SRQ */
    struct ibv_srq_attr attr;   /* SRQ attributes */
    uint32_t comp_mask;         /* Identifies valid fields */
    enum ibv_srq_type srq_type; /* Basic / XRC / tag matching */
    struct ibv_pd *pd;          /* PD associated with the SRQ */
    struct ibv_xrcd *xrcd;      /* XRC domain to associate with the SRQ */
    struct ibv_cq *cq;          /* CQ to associate with the SRQ for XRC mode */
    struct ibv_tm_cap tm_cap;   /* Tag matching attributes */
};
struct ibv_srq_attr {
    uint32_t max_wr;    /* Requested max number of outstanding work requests (WRs) in the SRQ */
    uint32_t max_sge;   /* Requested max number of scatter elements per WR */
    uint32_t srq_limit; /* The limit value of the SRQ */
};
struct ibv_tm_cap {
    uint32_t max_num_tags; /* Tag matching list size */
    uint32_t max_ops;      /* Number of outstanding tag list operations */
};
</code></pre>
<p> The function <code>ibv_create_srq_ex()</code> will update the <i>srq_init_attr_ex</i> struct with the original values of the SRQ that was created; the values of max_wr and max_sge will be greater than or equal to the values requested. </p>
<p> <code>ibv_destroy_srq()</code> destroys the SRQ <i>srq</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_create_srq_ex()</code> returns a pointer to the created SRQ, or NULL if the request fails. </p>
<p> <code>ibv_destroy_srq()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> <code>ibv_destroy_srq()</code> fails if any queue pair is still associated with this SRQ.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_alloc_pd/">ibv_alloc_pd</a></code>(3), <code><a href="/docs/linux/man/3-ibv_modify_srq/">ibv_modify_srq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_srq/">ibv_query_srq</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
