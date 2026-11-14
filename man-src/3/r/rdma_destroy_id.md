---
title: "rdma_destroy_id(3)"
name: "rdma_destroy_id"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_destroy_id/"
---

rdma_destroy_id - Release a communication identifier.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_destroy_id

    (struct rdma_cm_id *id);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>The communication identifier to destroy.</dl>

<h2>Description</h2>

Destroys the specified rdma_cm_id and cancels any outstanding asynchronous operation.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Users must free any associated QP with the rdma_cm_id before calling this routine and ack all related events.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_qp/">rdma_destroy_qp</a>(3), <a HREF="/docs/linux/man/3-rdma_ack_cm_event/">rdma_ack_cm_event</a>(3) 
