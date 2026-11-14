---
title: "rdma_destroy_ep(3)"
name: "rdma_destroy_ep"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_destroy_ep/"
---

rdma_destroy_ep - Release a communication identifier.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
void rdma_destroy_ep

    (struct rdma_cm_id *id);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>The communication identifier to destroy.</dl>

<h2>Description</h2>

Destroys the specified rdma_cm_id and all associated resources

<h2>Notes</h2>

rdma_destroy_ep will automatically destroy any QP and SRQ associated with the rdma_cm_id.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_create_ep/">rdma_create_ep</a>(3) 
