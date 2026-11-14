---
title: "rdma_bind_addr(3)"
name: "rdma_bind_addr"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_bind_addr/"
---

rdma_bind_addr - Bind an RDMA identifier to a source address.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_bind_addr

    (struct rdma_cm_id *id,

     struct sockaddr *addr);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.
<dt>addr
<dd>Local address information. Wildcard values are permitted.</dl>

<h2>Description</h2>

Associates a source address with an rdma_cm_id. The address may be wildcarded. If binding to a specific local address, the rdma_cm_id will also be bound to a local RDMA device.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Typically, this routine is called before calling rdma_listen to bind to a specific port number, but it may also be called on the active side of a connection before calling rdma_resolve_addr to bind to a specific address. 

 If used to bind to port 0, the rdma_cm will select an available port, which can be retrieved with <a HREF="/docs/linux/man/3-rdma_get_src_port/">rdma_get_src_port</a>(3).

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3), <a HREF="/docs/linux/man/3-rdma_listen/">rdma_listen</a>(3), <a HREF="/docs/linux/man/3-rdma_resolve_addr/">rdma_resolve_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_create_qp/">rdma_create_qp</a>(3), <a HREF="/docs/linux/man/3-rdma_get_local_addr/">rdma_get_local_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_get_src_port/">rdma_get_src_port</a>(3) 
