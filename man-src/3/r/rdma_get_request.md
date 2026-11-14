---
title: "rdma_get_request(3)"
name: "rdma_get_request"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_get_request/"
---

rdma_get_request - Retrieves the next pending connection request event.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_get_request

    (struct rdma_cm_id *listen,

     struct rdma_cm_id **id);</code></pre>

<h2>Arguments</h2>

<dl><dt>listen
<dd>Listening rdma_cm_id.
<dt>id
<dd>rdma_cm_id associated with the new connection.</dl>

<h2>Description</h2>

Retrieves a connection request event. If no requests are pending, the call will block until an event is received.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

This call may only be used on listening rdma_cm_id's operating synchronously. On success, a new rdma_cm_id representing the connection request will be returned to the user. The new rdma_cm_id will reference event information associated with the request until the user calls rdma_reject, rdma_accept, or rdma_destroy_id on the newly created identifier. For a description of the event data, see rdma_get_cm_event. 

 If QP attributes are associated with the listening endpoint, the returned rdma_cm_id will also reference an allocated QP.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3), <a HREF="/docs/linux/man/3-rdma_accept/">rdma_accept</a>(3), <a HREF="/docs/linux/man/3-rdma_reject/">rdma_reject</a>(3), <a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_listen/">rdma_listen</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_id/">rdma_destroy_id</a>(3) 
