---
title: "rdma_resolve_addr(3)"
name: "rdma_resolve_addr"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_resolve_addr/"
---

rdma_resolve_addr - Resolve destination and optional source addresses.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_resolve_addr

    (struct rdma_cm_id *id,

     struct sockaddr *src_addr,

     struct sockaddr *dst_addr,

     int timeout_ms);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.
<dt>src_addr
<dd>Source address information. This parameter may be NULL.
<dt>dst_addr
<dd>Destination address information.
<dt>timeout_ms
<dd>Time to wait for resolution to complete.</dl>

<h2>Description</h2>

Resolve destination and optional source addresses from IP addresses to an RDMA address. If successful, the specified rdma_cm_id will be bound to a local device.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

This call is used to map a given destination IP address to a usable RDMA address. The IP to RDMA address mapping is done using the local routing tables, or via ARP. If a source address is given, the rdma_cm_id is bound to that address, the same as if rdma_bind_addr were called. If no source address is given, and the rdma_cm_id has not yet been bound to a device, then the rdma_cm_id will be bound to a source address based on the local routing tables. After this call, the rdma_cm_id will be bound to an RDMA device. This call is typically made from the active side of a connection before calling rdma_resolve_route and rdma_connect.

<h2>Infiniband Specific</h2>

This call maps the destination and, if given, source IP addresses to GIDs. In order to perform the mapping, IPoIB must be running on both the local and remote nodes.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3), <a HREF="/docs/linux/man/3-rdma_resolve_route/">rdma_resolve_route</a>(3), <a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_create_qp/">rdma_create_qp</a>(3), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3), <a HREF="/docs/linux/man/3-rdma_bind_addr/">rdma_bind_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_get_src_port/">rdma_get_src_port</a>(3), <a HREF="/docs/linux/man/3-rdma_get_dst_port/">rdma_get_dst_port</a>(3), <a HREF="/docs/linux/man/3-rdma_get_local_addr/">rdma_get_local_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_get_peer_addr/">rdma_get_peer_addr</a>(3) 
