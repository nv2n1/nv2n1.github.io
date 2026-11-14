---
title: "rdma_reject(3)"
name: "rdma_reject"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_reject/"
---

rdma_reject - Called to reject a connection request.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_reject

    (struct rdma_cm_id *id,

     const void *private_data,

     uint8_t private_data_len);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>Connection identifier associated with the request.
<dt>private_data
<dd>Optional private data to send with the reject message.
<dt>private_data_len
<dd>Specifies the size of the user-controlled data buffer. Note that the actual amount of data transferred to the remote side is transport dependent and may be larger than that requested.</dl>

<h2>Description</h2>

Called from the listening side to reject a connection or datagram service lookup request.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

After receiving a connection request event, a user may call rdma_reject to reject the request. If the underlying RDMA transport supports private data in the reject message, the specified data will be passed to the remote side.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_listen/">rdma_listen</a>(3), <a HREF="/docs/linux/man/3-rdma_accept/">rdma_accept</a>(3), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3) 
