---
title: "rdma_post_read(3)"
name: "rdma_post_read"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_post_read/"
---

rdma_post_read - post an RDMA read work request.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_verbs.h&gt;
int rdma_post_read

    (struct rdma_cm_id *id,

     void *context,

     void *addr,

     size_t length,

     struct ibv_mr *mr,

     int flags,

     uint64_t remote_addr,

     uint32_t rkey);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>A reference to a communication identifier where the request will be posted.
<dt>context
<dd>User-defined context associated with the request.
<dt>addr
<dd>The address of the local destination of the read request.
<dt>length
<dd>The length of the read operation.
<dt>mr
<dd>Registered memory region associated with the local buffer.
<dt>flags
<dd>Optional flags used to control the read operation.
<dt>remote_addr
<dd>The address of the remote registered memory to read from.
<dt>rkey
<dd>The registered memory key associated with the remote address.</dl>

<h2>Description</h2>

Posts a work request to the send queue of the queue pair associated with the rdma_cm_id. The contents of the remote memory region will be read into the local data buffer.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

For a list of supported flags, see ibv_post_send. Both the remote and local data buffers must have been registered before the read is issued, and the buffers must remain registered until the read completes. 

 Read operations may not be posted to an rdma_cm_id or the corresponding queue pair until it has been connected. 

 The user-defined context associated with the read request will be returned to the user through the work completion wr_id, work request identifier, field.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_accept/">rdma_accept</a>(3), <a HREF="/docs/linux/man/3-ibv_post_send/">ibv_post_send</a>(3), <a HREF="/docs/linux/man/3-rdma_post_readv/">rdma_post_readv</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_read/">rdma_reg_read</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_msgs/">rdma_reg_msgs</a>(3) 
