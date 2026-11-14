---
title: "rdma_dereg_mr(3)"
name: "rdma_dereg_mr"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_dereg_mr/"
---

rdma_dereg_mr - deregisters a registered memory region.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_verbs.h&gt;
struct ibv_mr *rdma_dereg_mr

    (struct ibv_mr *mr);</code></pre>

<h2>Arguments</h2>

<dl><dt>mr
<dd>A reference to a registered memory buffer.</dl>

<h2>Description</h2>

Deregisters a memory buffer that had been registered for RDMA or message operations. A user should call rdma_dereg_mr for all registered memory associated with an rdma_cm_id before destroying the rdma_cm_id.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

All memory registered with an rdma_cm_id is associated with the protection domain associated with the id. Users must deregister all registered memory before the protection domain can be destroyed.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3), <a HREF="/docs/linux/man/3-rdma_create_ep/">rdma_create_ep</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_id/">rdma_destroy_id</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_ep/">rdma_destroy_ep</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_msgs/">rdma_reg_msgs</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_read/">rdma_reg_read</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_write/">rdma_reg_write</a>(3), <a HREF="/docs/linux/man/3-ibv_reg_mr/">ibv_reg_mr</a>(3), <a HREF="/docs/linux/man/3-ibv_dereg_mr/">ibv_dereg_mr</a>(3) 
