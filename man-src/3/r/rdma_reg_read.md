---
title: "rdma_reg_read(3)"
name: "rdma_reg_read"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_reg_read/"
---

rdma_reg_read - register data buffer(s) for remote RDMA read access.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_verbs.h&gt;
struct ibv_mr *rdma_reg_read

    (struct rdma_cm_id *id,

     void *addr,

     size_t length);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>A reference to a communication identifier where the message buffer(s) will be used.
<dt>addr
<dd>The address of the memory buffer(s) to register.
<dt>length
<dd>The total length of the memory to register.</dl>

<h2>Description</h2>

Registers a memory buffer that will be accessed by a remote RDMA read operation. Memory buffers registered using rdma_reg_read may be targeted in an RDMA read request, allowing the buffer to be specified on the remote side of an RDMA connection as the remote_addr of rdma_post_read, or similar call.

<h2>Return Value</h2>

Returns a reference to the registered memory region on success, or NULL on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

rdma_reg_read is used to register a data buffer that will be the target of an RDMA read operation on a queue pair associated with an rdma_cm_id. The memory buffer is registered with the proteection domain associated with the idenfier. The start of the data buffer is specified through the addr parameter, and the total size of the buffer is given by length. 

 All data buffers should be registered before being posted as a work request. Users must deregister all registered memory by calling rdma_dereg_mr.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3), <a HREF="/docs/linux/man/3-rdma_create_ep/">rdma_create_ep</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_msgs/">rdma_reg_msgs</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_write/">rdma_reg_write</a>(3), <a HREF="/docs/linux/man/3-ibv_reg_mr/">ibv_reg_mr</a>(3), <a HREF="/docs/linux/man/3-ibv_dereg_mr/">ibv_dereg_mr</a>(3), <a HREF="/docs/linux/man/3-rdma_post_read/">rdma_post_read</a>(3) 
