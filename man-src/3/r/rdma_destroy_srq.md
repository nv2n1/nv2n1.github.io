---
title: "rdma_destroy_srq(3)"
name: "rdma_destroy_srq"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_destroy_srq/"
---

rdma_destroy_srq - Deallocate a SRQ.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_verbs.h&gt;
void rdma_destroy_srq

    (struct rdma_cm_id *id);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.</dl>

<h2>Description</h2>

Destroy an SRQ allocated on the rdma_cm_id.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Users should destroy any SRQ associated with an rdma_cm_id before destroying the ID.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_create_srq/">rdma_create_srq</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_id/">rdma_destroy_id</a>(3), <a HREF="/docs/linux/man/3-ibv_destroy_srq/">ibv_destroy_srq</a>(3) 
