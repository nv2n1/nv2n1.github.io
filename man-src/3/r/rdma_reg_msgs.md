---
title: "rdma_reg_msgs(3)"
name: "rdma_reg_msgs"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_reg_msgs/"
---

rdma_reg_msgs - register data buffer(s) for sending or receiving messages.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_verbs.h&gt;
struct ibv_mr *rdma_reg_msgs

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

Registers an array of memory buffers used for sending and receiving messages or for RDMA operations. Memory buffers registered using rdma_reg_msgs may be posted to an rdma_cm_id using rdma_post_send or rdma_post_recv, or specified as the target of an RDMA read operation or the source of an RDMA write reqeust.

<h2>Return Value</h2>

Returns a reference to the registered memory region on success, or NULL on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

rdma_reg_msgs is used to register an array of data buffers that will be used send and/or receive messages on a queue pair associated with an rdma_cm_id. The memory buffer is registered with the proteection domain associated with the idenfier. The start of the data buffer array is specified through the addr parameter, and the total size of the array is given by length. 

 All data buffers should be registered before being posted as a work request. Users must deregister all registered memory by calling rdma_dereg_mr.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3), <a HREF="/docs/linux/man/3-rdma_create_ep/">rdma_create_ep</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_read/">rdma_reg_read</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_write/">rdma_reg_write</a>(3), <a HREF="/docs/linux/man/3-ibv_reg_mr/">ibv_reg_mr</a>(3), <a HREF="/docs/linux/man/3-ibv_dereg_mr/">ibv_dereg_mr</a>(3), <a HREF="/docs/linux/man/3-rdma_post_send/">rdma_post_send</a>(3), <a HREF="/docs/linux/man/3-rdma_post_recv/">rdma_post_recv</a>(3), <a HREF="/docs/linux/man/3-rdma_post_read/">rdma_post_read</a>(3), <a HREF="/docs/linux/man/3-rdma_post_readv/">rdma_post_readv</a>(3), <a HREF="/docs/linux/man/3-rdma_post_write/">rdma_post_write</a>(3), <a HREF="/docs/linux/man/3-rdma_post_writev/">rdma_post_writev</a>(3) 
