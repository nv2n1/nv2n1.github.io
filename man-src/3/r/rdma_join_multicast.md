---
title: "rdma_join_multicast(3)"
name: "rdma_join_multicast"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_join_multicast/"
---

rdma_join_multicast - Joins a multicast group.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_join_multicast

    (struct rdma_cm_id *id,

     struct sockaddr *addr,

     void *context);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>Communication identifier associated with the request.
<dt>addr
<dd>Multicast address identifying the group to join.
<dt>context
<dd>User-defined context associated with the join request.</dl>

<h2>Description</h2>

Joins a multicast group and attaches an associated QP to the group.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Before joining a multicast group, the rdma_cm_id must be bound to an RDMA device by calling rdma_bind_addr or rdma_resolve_addr. Use of rdma_resolve_addr requires the local routing tables to resolve the multicast address to an RDMA device, unless a specific source address is provided. The user must call rdma_leave_multicast to leave the multicast group and release any multicast resources. After the join operation completes, if a QP is associated with the rdma_cm_id, it is automatically attached to the multicast group when the multicast event is retrieved by the user. Otherwise, the user is responsible for calling ibv_attach_mcast to bind the QP to the multicast group. The join context is returned to the user through the private_data field in the rdma_cm_event.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_leave_multicast/">rdma_leave_multicast</a>(3), <a HREF="/docs/linux/man/3-rdma_bind_addr/">rdma_bind_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_resolve_addr/">rdma_resolve_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_create_qp/">rdma_create_qp</a>(3), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3) 
