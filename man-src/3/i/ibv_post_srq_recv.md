---
title: "ibv_post_srq_recv(3)"
name: "ibv_post_srq_recv"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_post_srq_recv/"
description: "ibv_post_srq_recv – post a list of work requests (WRs) to a shared receive queue (SRQ)"
---

<h2 class="name">NAME</h2>
<p> ibv_post_srq_recv &#8211; post a list of work requests (WRs) to a shared receive queue (SRQ) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_post_srq_recv(struct ibv_srq *srq, struct ibv_recv_wr *wr,
                      struct ibv_recv_wr **bad_wr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_post_srq_recv()</code> posts the linked list of work requests (WRs) starting with <i>wr</i> to the shared receive queue (SRQ) <i>srq</i>. It stops processing WRs from this list at the first failure (that can be detected immediately while requests are being posted), and returns this failing WR through <i>bad_wr</i>. </p>
<p> The argument <i>wr</i> is an ibv_recv_wr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_recv_wr {
    uint64_t wr_id;           /* User defined WR ID */
    struct ibv_recv_wr *next; /* Pointer to next WR in list, NULL if last WR */
    struct ibv_sge *sg_list;  /* Pointer to the s/g array */
    int num_sge;              /* Size of the s/g array */
};
struct ibv_sge {
    uint64_t addr;   /* Start address of the local memory buffer */
    uint32_t length; /* Length of the buffer */
    uint32_t lkey;   /* Key of the local Memory Region */
};
</code></pre>
<h2>RETURN VALUE</h2>
<p> <code>ibv_post_srq_recv()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> The buffers used by a WR can only be safely reused after WR the request is fully executed and a work completion has been retrieved from the corresponding completion queue (CQ). </p>
<p> If a WR is being posted to a UD QP, the Global Routing Header (GRH) of the incoming message will be placed in the first 40 bytes of the buffer(s) in the scatter list. If no GRH is present in the incoming message, then the first bytes will be undefined. This means that in all cases, the actual data of the incoming message will start at an offset of 40 bytes into the buffer(s) in the scatter list.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_qp/">ibv_create_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_post_send/">ibv_post_send</a></code>(3), <code><a href="/docs/linux/man/3-ibv_post_recv/">ibv_post_recv</a></code>(3), <code><a href="/docs/linux/man/3-ibv_poll_cq/">ibv_poll_cq</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
