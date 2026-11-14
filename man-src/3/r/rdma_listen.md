---
title: "rdma_listen(3)"
name: "rdma_listen"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_listen/"
---

rdma_listen - Listen for incoming connection requests.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_listen

    (struct rdma_cm_id *id,

     int backlog);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.
<dt>backlog
<dd>backlog of incoming connection requests.</dl>

<h2>Description</h2>

Initiates a listen for incoming connection requests or datagram service lookup. The listen will be restricted to the locally bound source address.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Users must have bound the rdma_cm_id to a local address by calling rdma_bind_addr before calling this routine. If the rdma_cm_id is bound to a specific IP address, the listen will be restricted to that address and the associated RDMA device. If the rdma_cm_id is bound to an RDMA port number only, the listen will occur across all RDMA devices.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_bind_addr/">rdma_bind_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_accept/">rdma_accept</a>(3), <a HREF="/docs/linux/man/3-rdma_reject/">rdma_reject</a>(3), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3) 
