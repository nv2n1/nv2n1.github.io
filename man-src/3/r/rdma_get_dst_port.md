---
title: "rdma_get_dst_port(3)"
name: "rdma_get_dst_port"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_get_dst_port/"
description: "rdma_get_dst_port – Returns the remote port number of a bound rdma_cm_id."
---

<p>rdma_get_dst_port &#8211; Returns the remote port number of a bound rdma_cm_id.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;rdma/rdma_cma.h&gt;</code></pre>
<p> <code>uint16_t rdma_get_dst_port</code> <code>(struct rdma_cm_id *</code><i>id</i><code>);</code></p>
<h2>Arguments</h2>
<dl>
<dt>id</p>
<dd>RDMA identifier.</dl>
<h2>Description</h2>
<p>Returns the remote port number for an rdma_cm_id that has been bound to a remote address.</p>
<h2>Return Value</h2>
<p>Returns the 16-bit port identifier associated with the peer endpoint. If the rdma_cm_id is not connected, the returned value is 0.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a href="/docs/linux/man/3-rdma_accept/">rdma_accept</a>(3), <a href="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3), <a href="/docs/linux/man/3-rdma_get_src_port/">rdma_get_src_port</a>(3), <a href="/docs/linux/man/3-rdma_get_local_addr/">rdma_get_local_addr</a>(3), <a href="/docs/linux/man/3-rdma_get_peer_addr/">rdma_get_peer_addr</a>(3) </p>
