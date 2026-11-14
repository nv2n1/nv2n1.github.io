---
title: "rdma_get_recv_comp(3)"
name: "rdma_get_recv_comp"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_get_recv_comp/"
---

rdma_get_recv_comp - retrieves a completed receive request.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_verbs.h&gt;
int rdma_get_recv_comp

    (struct rdma_cm_id *id,

     struct ibv_wc *wc);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>A reference to a communication identifier to check for completions.
<dt>wc
<dd>A reference to a work completion structure to fill in.</dl>

<h2>Description</h2>

Retrieves a completed work request for a receive operation. Information about the completed request is returned through the wc parameter, with the wr_id set to the context of the request. For details on the work completion structure, see ibv_poll_cq.

<h2>Return Value</h2>

Returns the number of returned completions (0 or 1) on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

This calls polls the receive completion queue associated with an rdma_cm_id. If a completion is not found, the call blocks until a request completes. This call should only be used on rdma_cm_id's that do not share CQs with other rdma_cm_id's, and maintain separate CQs for sends and receive completions.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-ibv_poll_cq/">ibv_poll_cq</a>(3), <a HREF="/docs/linux/man/3-rdma_get_send_comp/">rdma_get_send_comp</a>(3), <a HREF="/docs/linux/man/3-rdma_post_send/">rdma_post_send</a>(3), <a HREF="/docs/linux/man/3-rdma_post_read/">rdma_post_read</a>(3), <a HREF="/docs/linux/man/3-rdma_post_write/">rdma_post_write</a>(3) 
