---
title: "ibv_destroy_srq(3)"
name: "ibv_destroy_srq"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_destroy_srq/"
description: "ibv_create_srq, ibv_destroy_srq – create or destroy a shared receive queue (SRQ)"
---

<h2 class="name">NAME</h2>
<p> ibv_create_srq, ibv_destroy_srq &#8211; create or destroy a shared receive queue (SRQ) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_srq *ibv_create_srq(struct ibv_pd *pd, struct
                               ibv_srq_init_attr *srq_init_attr);
int ibv_destroy_srq(struct ibv_srq *srq);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_create_srq()</code> creates a shared receive queue (SRQ) associated with the protection domain <i>pd</i>. The argument <i>srq_init_attr</i> is an ibv_srq_init_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_srq_init_attr {
    void *srq_context;        /* Associated context of the SRQ */
    struct ibv_srq_attr attr; /* SRQ attributes */
};
struct ibv_srq_attr {
    uint32_t max_wr;    /* Requested max number of outstanding work requests (WRs) in the SRQ */
    uint32_t max_sge;   /* Requested max number of scatter elements per WR */
    uint32_t srq_limit; /* The limit value of the SRQ (irrelevant for ibv_create_srq) */
};
</code></pre>
<p> The function <code>ibv_create_srq()</code> will update the <i>srq_init_attr</i> struct with the original values of the SRQ that was created; the values of max_wr and max_sge will be greater than or equal to the values requested. </p>
<p> <code>ibv_destroy_srq()</code> destroys the SRQ <i>srq</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_create_srq()</code> returns a pointer to the created SRQ, or NULL if the request fails. </p>
<p> <code>ibv_destroy_srq()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> <code>ibv_destroy_srq()</code> fails if any queue pair is still associated with this SRQ.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_alloc_pd/">ibv_alloc_pd</a></code>(3), <code><a href="/docs/linux/man/3-ibv_modify_srq/">ibv_modify_srq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_srq/">ibv_query_srq</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
