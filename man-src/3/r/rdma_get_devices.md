---
title: "rdma_get_devices(3)"
name: "rdma_get_devices"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_get_devices/"
---

rdma_get_devices - Get a list of RDMA devices currently available.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
struct ibv_context **rdma_get_devices

    (int *num_devices);</code></pre>

<h2>Arguments</h2>

<dl><dt>num_devices
<dd>If non-NULL, set to the number of devices returned.</dl>

<h2>Description</h2>

Return a NULL-terminated array of opened RDMA devices. Callers can use this routine to allocate resources on specific RDMA devices that will be shared across multiple rdma_cm_id's.

<h2>Return Value</h2>

Returns an array of available RDMA devices, or NULL if the request fails. On failure, errno will be set to indicate the failure reason.

<h2>Notes</h2>

The returned array must be released by calling rdma_free_devices. Devices remain opened while the librdmacm is loaded.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_free_devices/">rdma_free_devices</a>(3) 
