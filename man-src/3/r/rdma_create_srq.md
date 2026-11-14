---
title: "rdma_create_srq(3)"
name: "rdma_create_srq"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_create_srq/"
---

rdma_create_srq - Allocate a shared receive queue.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_verbs.h&gt;
int rdma_create_srq

    (struct rdma_cm_id *id,

     struct ibv_pd *pd,

     struct ibv_srq_init_attr *attr);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.
<dt>pd
<dd>Optional protection domain for the SRQ.
<dt>attr
<dd>Initial SRQ attributes.</dl>

<h2>Description</h2>

Allocate a SRQ associated with the specified rdma_cm_id.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

The rdma_cm_id must be bound to a local RDMA device before calling this function, and the protection domain, if provided, must be for that same device. After being allocated, the SRQ will be ready to handle posting of receives. 

 If a protection domain is not given - pd parameter is NULL - then the rdma_cm_id will be created using a default protection domain. One default protection domain is allocated per RDMA device. 

 The initial SRQ attributes are specified by the attr parameter. The ext.xrc.cq fields in the ibv_srq_init_attr is optional. If a completion queue is not specified for an XRC SRQ, then a CQ will be allocated by the rdma_cm for the SRQ, along with corresponding completion channels. Completion channels and CQ data created by the rdma_cm are exposed to the user through the rdma_cm_id structure. 

 The actual capabilities and properties of the created SRQ will be returned to the user through the attr parameter. An rdma_cm_id may only be associated with a single SRQ.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_bind_addr/">rdma_bind_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_resolve_addr/">rdma_resolve_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_create_ep/">rdma_create_ep</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_srq/">rdma_destroy_srq</a>(3), <a HREF="/docs/linux/man/3-ibv_create_srq/">ibv_create_srq</a>(3), <a HREF="/docs/linux/man/3-ibv_create_xsrq/">ibv_create_xsrq</a>(3) 
