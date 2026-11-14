---
title: "rdma_create_qp(3)"
name: "rdma_create_qp"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_create_qp/"
---

rdma_create_qp - Allocate a QP.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_create_qp

    (struct rdma_cm_id *id,

     struct ibv_pd *pd,

     struct ibv_qp_init_attr *qp_init_attr);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.
<dt>pd
<dd>Optional protection domain for the QP.
<dt>qp_init_attr
<dd>Initial QP attributes.</dl>

<h2>Description</h2>

Allocate a QP associated with the specified rdma_cm_id and transition it for sending and receiving.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

The rdma_cm_id must be bound to a local RDMA device before calling this function, and the protection domain must be for that same device. QPs allocated to an rdma_cm_id are automatically transitioned by the librdmacm through their states. After being allocated, the QP will be ready to handle posting of receives. If the QP is unconnected, it will be ready to post sends. 

 If a protection domain is not given - pd parameter is NULL - then the rdma_cm_id will be created using a default protection domain. One default protection domain is allocated per RDMA device. 

 The initial QP attributes are specified by the qp_init_attr parameter. The send_cq and recv_cq fields in the ibv_qp_init_attr are optional. If a send or receive completion queue is not specified, then a CQ will be allocated by the rdma_cm for the QP, along with corresponding completion channels. Completion channels and CQ data created by the rdma_cm are exposed to the user through the rdma_cm_id structure. 

 The actual capabilities and properties of the created QP will be returned to the user through the qp_init_attr parameter. An rdma_cm_id may only be associated with a single QP.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_bind_addr/">rdma_bind_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_resolve_addr/">rdma_resolve_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_qp/">rdma_destroy_qp</a>(3), <a HREF="/docs/linux/man/3-ibv_create_qp/">ibv_create_qp</a>(3), <a HREF="/docs/linux/man/3-ibv_modify_qp/">ibv_modify_qp</a>(3) 
