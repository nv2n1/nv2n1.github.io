---
title: "rdma_resolve_route(3)"
name: "rdma_resolve_route"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_resolve_route/"
---

rdma_resolve_route - Resolve the route information needed to establish a connection.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_resolve_route

    (struct rdma_cm_id *id,

     int timeout_ms);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.
<dt>timeout_ms
<dd>Time to wait for resolution to complete.</dl>

<h2>Description</h2>

Resolves an RDMA route to the destination address in order to establish a connection. The destination address must have already been resolved by calling rdma_resolve_addr.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

This is called on the client side of a connection after calling rdma_resolve_addr, but before calling rdma_connect.

<h2>Infiniband Specific</h2>

This call obtains a path record that is used by the connection.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_resolve_addr/">rdma_resolve_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3) 
