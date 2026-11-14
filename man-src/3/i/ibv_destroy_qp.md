---
title: "ibv_destroy_qp(3)"
name: "ibv_destroy_qp"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_destroy_qp/"
description: "ibv_create_qp, ibv_destroy_qp – create or destroy a queue pair (QP)"
---

<h2 class="name">NAME</h2>
<p> ibv_create_qp, ibv_destroy_qp &#8211; create or destroy a queue pair (QP) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_qp *ibv_create_qp(struct ibv_pd *pd,
                             struct ibv_qp_init_attr *qp_init_attr);
int ibv_destroy_qp(struct ibv_qp *qp);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_create_qp()</code> creates a queue pair (QP) associated with the protection domain <i>pd</i>. The argument <i>qp_init_attr</i> is an ibv_qp_init_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_qp_init_attr {
    void *qp_context;         /* Associated context of the QP */
    struct ibv_cq *send_cq;   /* CQ to be associated with the Send Queue (SQ) */
    struct ibv_cq *recv_cq;   /* CQ to be associated with the Receive Queue (RQ) */
    struct ibv_srq *srq;      /* SRQ handle if QP is to be associated with an SRQ, otherwise NULL */
    struct ibv_qp_cap cap;    /* QP capabilities */
    enum ibv_qp_type qp_type; /* QP Transport Service Type: IBV_QPT_RC, IBV_QPT_UC, IBV_QPT_UD, IBV_QPT_RAW_PACKET or IBV_QPT_DRIVER */
    int sq_sig_all;           /* If set, each Work Request (WR) submitted to the SQ generates a completion entry */
};
struct ibv_qp_cap {
    uint32_t max_send_wr;     /* Requested max number of outstanding WRs in the SQ */
    uint32_t max_recv_wr;     /* Requested max number of outstanding WRs in the RQ */
    uint32_t max_send_sge;    /* Requested max number of scatter/gather (s/g) elements in a WR in the SQ */
    uint32_t max_recv_sge;    /* Requested max number of s/g elements in a WR in the SQ */
    uint32_t max_inline_data; /* Requested max number of data (bytes) that can be posted inline to the SQ, otherwise 0 */
};
</code></pre>
<p> The function <code>ibv_create_qp()</code> will update the <i>qp_init_attr</i>-&gt;cap struct with the actual <font SIZE="-1">QP</font> values of the QP that was created; the values will be greater than or equal to the values requested. </p>
<p> <code>ibv_destroy_qp()</code> destroys the QP <i>qp</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_create_qp()</code> returns a pointer to the created QP, or NULL if the request fails. Check the QP number (<code>qp_num</code>) in the returned QP. </p>
<p> <code>ibv_destroy_qp()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> <code>ibv_create_qp()</code> will fail if a it is asked to create QP of a type other than <code>IBV_QPT_RC</code> or <code>IBV_QPT_UD</code> associated with an SRQ. </p>
<p> The attributes max_recv_wr and max_recv_sge are ignored by <code>ibv_create_qp()</code> if the QP is to be associated with an SRQ. </p>
<p> <code>ibv_destroy_qp()</code> fails if the QP is attached to a multicast group. </p>
<p> <code>IBV_QPT_DRIVER</code> does not represent a specific service and is used for vendor specific QP logic.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_alloc_pd/">ibv_alloc_pd</a></code>(3), <code><a href="/docs/linux/man/3-ibv_modify_qp/">ibv_modify_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_qp/">ibv_query_qp</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
