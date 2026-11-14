---
title: "ibv_destroy_wq(3)"
name: "ibv_destroy_wq"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_destroy_wq/"
description: "ibv_create_wq, ibv_destroy_wq – create or destroy a Work Queue (WQ)."
---

<h2 class="name">NAME</h2>
<p> ibv_create_wq, ibv_destroy_wq &#8211; create or destroy a Work Queue (WQ). </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs_exp.h&gt;
struct ibv_wq *ibv_create_wq(struct ibv_context *context,
                             struct ibv_wq_init_attr *wq_init_attr);
int ibv_destroy_wq(struct ibv_wq *wq);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_create_wq()</code> creates a WQ associated with the ibv_context <i>context</i>. The argument <i>wq_init_attr</i> is an ibv_wq_init_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_wq_init_attr {
    void *wq_context;         /* Associated context of the WQ */
    enum ibv_wq_type wq_type; /* WQ type */
    uint32_t max_wr;          /* Requested max number of outstanding WRs in the WQ */
    uint32_t max_sge;         /* Requested max number of scatter/gather (s/g) elements per WR in the WQ */
    struct ibv_pd *pd;        /* PD to be associated with the WQ */
    struct ibv_cq *cq;        /* CQ to be associated with the WQ */
    uint32_t comp_mask;       /* Identifies valid fields. Use ibv_wq_init_attr_mask */
    uint32_t create_flags     /* Creation flags for this WQ, use enum ibv_wq_flags */
};
enum ibv_wq_flags {
    IBV_WQ_FLAGS_CVLAN_STRIPPING = 1 &lt;&lt; 0,       /* CVLAN field will be stripped from incoming packets */
    IBV_WQ_FLAGS_SCATTER_FCS = 1 &lt;&lt; 1,           /* FCS field will be scattered to host memory */
    IBV_WQ_FLAGS_DELAY_DROP = 1 &lt;&lt; 2,            /* Packets won't be dropped immediately if no receive WQEs */
    IBV_WQ_FLAGS_PCI_WRITE_END_PADDING = 1 &lt;&lt; 3, /* Incoming packets will be padded to cacheline size */
    IBV_WQ_FLAGS_RESERVED = 1 &lt;&lt; 4,
};
</code></pre>
<p> The function <code>ibv_create_wq()</code> will update the <i>wq_init_attr</i>-&gt;max_wr and <i>wq_init_attr</i>-&gt;max_sge fields with the actual <font SIZE="-1">WQ</font> values of the WQ that was created; the values will be greater than or equal to the values requested. </p>
<p> <code>ibv_destroy_wq()</code> destroys the WQ <i>wq</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_create_wq()</code> returns a pointer to the created WQ, or NULL if the request fails. </p>
<p> <code>ibv_destroy_wq()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_modify_wq/">ibv_modify_wq</a></code>(3),</p>
<h2>AUTHORS</h2>
<dl>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
