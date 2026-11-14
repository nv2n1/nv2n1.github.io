---
title: "rdma_getaddrinfo(3)"
name: "rdma_getaddrinfo"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_getaddrinfo/"
---

rdma_getaddrinfo - Provides transport independent address translation.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_getaddrinfo

    (char *node,

     char *service,

     struct rdma_addrinfo *hints,

     struct rdma_addrinfo **res);</code></pre>

<h2>Arguments</h2>

<dl><dt>node
<dd>Optional, name, dotted-decimal IPv4, or IPv6 hex address to resolve.
<dt>service
<dd>Service name or port number of address.
<dt>hints
<dd>Reference to an rdma_addrinfo structure containing hints about the type of service the caller supports.
<dt>res
<dd>A pointer to a linked list of rdma_addrinfo structures containing response information.</dl>

<h2>Description</h2>

Resolves the destination node and service address and returns information needed to establish communication. Provides the RDMA functional equivalent to getaddrinfo.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Either node, service, or hints must be provided. If hints are provided, the operation will be controlled by hints.ai_flags. If RAI_PASSIVE is specified, the call will resolve address information for use on the passive side of a connection. If node is provided, rdma_getaddrinfo will attempt to resolve the RDMA address, route, and connection data to the given node. The hints parameter, if provided, may be used to control the resulting output as indicated below. If node is not given, rdma_getaddrinfo will attempt to resolve the RDMA addressing information based on the hints.ai_src_addr, hints.ai_dst_addr, or hints.ai_route.

<h2>rdma_addrinfo</h2>

<dl><dt>ai_flags
<dd>Hint flags that control the operation. Supported flags are:
<dt>RAI_PASSIVE
<dd>Indicates that the results will be used on the passive/listening side of a connection.
<dt>RAI_NUMERICHOST
<dd>If specified, then the node parameter, if provided, must be a numerical network address. This flag suppresses any lengthy address resolution.
<dt>RAI_NOROUTE
<dd>If set, this flag suppresses any lengthy route resolution.
<dt>RAI_FAMILY
<dd>If set, the ai_family setting should be used as an input hint for interpretting the node parameter.
<dt>ai_family
<dd>Address family for the source and destination address. Supported families are: AF_INET, AF_INET6, and AF_IB.
<dt>ai_qp_type
<dd>Indicates the type of RDMA QP used for communication. Supported types are: IBV_UD (unreliable datagram) and IBV_RC (reliable connected).
<dt>ai_port_space
<dd>RDMA port space in use. Supported values are: RDMA_PS_UDP, RDMA_PS_TCP, and RDMA_PS_IB.
<dt>ai_src_len
<dd>The length of the source address referenced by ai_src_addr. This will be 0 if an appropriate source address could not be discovered for a given destination.
<dt>ai_dst_len
<dd>The length of the destination address referenced by ai_dst_addr. This will be 0 if the RAI_PASSIVE flag was specified as part of the hints.
<dt>ai_src_addr
<dd>If provided, the address for the local RDMA device.
<dt>ai_dst_addr
<dd>If provided, the address for the destination RDMA device.
<dt>ai_src_canonname
<dd>The canonical for the source.
<dt>ai_dst_canonname
<dd>The canonical for the destination.
<dt>ai_route_len
<dd>Size of the routing information buffer referenced by ai_route. This will be 0 if the underlying transport does not require routing data, or none could be resolved.
<dt>ai_route
<dd>Routing information for RDMA transports that require routing data as part of connection establishment. The format of the routing data depends on the underlying transport. If Infiniband transports are used, ai_route will reference an array of struct ibv_path_data on output, if routing data is available. Routing paths may be restricted by setting desired routing data fields on input to rdma_getaddrinfo. For Infiniband, hints.ai_route may reference an array of struct ibv_path_record or struct ibv_path_data on input.
<dt>ai_connect_len
<dd>Size of connection information referenced by ai_connect. This will be 0 if the underlying transport does not require additional connection information.
<dt>ai_connect
<dd>Data exchanged as part of the connection establishment process. If provided, ai_connect data must be transferred as private data, with any user supplied private data following it.
<dt>ai_next
<dd>Pointer to the next rdma_addrinfo structure in the list. Will be NULL if no more structures exist.</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3), <a HREF="/docs/linux/man/3-rdma_resolve_route/">rdma_resolve_route</a>(3), <a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_create_qp/">rdma_create_qp</a>(3), <a HREF="/docs/linux/man/3-rdma_bind_addr/">rdma_bind_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_create_ep/">rdma_create_ep</a>(3) 
