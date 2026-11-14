---
title: "rdma_destroy_qp(3)"
name: "rdma_destroy_qp"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_destroy_qp/"
---

rdma_destroy_qp - Deallocate a QP.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
void rdma_destroy_qp

    (struct rdma_cm_id *id);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.</dl>

<h2>Description</h2>

Destroy a QP allocated on the rdma_cm_id.

<h2>Notes</h2>

Users must destroy any QP associated with an rdma_cm_id before destroying the ID.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_create_qp/">rdma_create_qp</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_id/">rdma_destroy_id</a>(3), <a HREF="/docs/linux/man/3-ibv_destroy_qp/">ibv_destroy_qp</a>(3) 
