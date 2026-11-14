---
title: "rdma_leave_multicast(3)"
name: "rdma_leave_multicast"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_leave_multicast/"
---

rdma_leave_multicast - Leaves a multicast group.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_leave_multicast

    (struct rdma_cm_id *id,

     struct sockaddr *addr);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>Communication identifier associated with the request.
<dt>addr
<dd>Multicast address identifying the group to leave.</dl>

<h2>Description</h2>

Leaves a multicast group and detaches an associated QP from the group.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Calling this function before a group has been fully joined results in canceling the join operation. Users should be aware that messages received from the multicast group may stilled be queued for completion processing immediately after leaving a multicast group. Destroying an rdma_cm_id will automatically leave all multicast groups.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_join_multicast/">rdma_join_multicast</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_qp/">rdma_destroy_qp</a>(3) 
