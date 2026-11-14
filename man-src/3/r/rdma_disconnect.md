---
title: "rdma_disconnect(3)"
name: "rdma_disconnect"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_disconnect/"
---

rdma_disconnect - This function disconnects a connection.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_disconnect

    (struct rdma_cm_id *id);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.</dl>

<h2>Description</h2>

Disconnects a connection and transitions any associated QP to the error state, which will flush any posted work requests to the completion queue. This routine should be called by both the client and server side of a connection. After successfully disconnecting, an RDMA_CM_EVENT_DISCONNECTED event will be generated on both sides of the connection.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_listen/">rdma_listen</a>(3), <a HREF="/docs/linux/man/3-rdma_accept/">rdma_accept</a>(3), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3) 
