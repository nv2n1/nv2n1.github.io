---
title: "rdma_get_local_addr(3)"
name: "rdma_get_local_addr"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_get_local_addr/"
---

rdma_get_local_addr - Returns the local IP address of a bound rdma_cm_id.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
struct sockaddr *rdma_get_local_addr

    (struct rdma_cm_id *id);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.</dl>

<h2>Description</h2>

Returns the local IP address for an rdma_cm_id that has been bound to a local device.

<h2>Return Value</h2>

Returns a pointer to the local sockaddr address of the rdma_cm_id. If the rdma_cm_id is not bound to an address, the contents of the sockaddr structure will be set to all zeroes.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_bind_addr/">rdma_bind_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_resolve_addr/">rdma_resolve_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_get_src_port/">rdma_get_src_port</a>(3), <a HREF="/docs/linux/man/3-rdma_get_dst_port/">rdma_get_dst_port</a>(3), <a HREF="/docs/linux/man/3-rdma_get_peer_addr/">rdma_get_peer_addr</a>(3) 
