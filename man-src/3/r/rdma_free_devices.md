---
title: "rdma_free_devices(3)"
name: "rdma_free_devices"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_free_devices/"
---

rdma_free_devices - Frees the list of devices returned by rdma_get_devices.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
void rdma_free_devices

    (struct ibv_context **list);</code></pre>

<h2>Arguments</h2>

<dl><dt>list
<dd>List of devices returned from rdma_get_devices.</dl>

<h2>Description</h2>

Frees the device array returned by rdma_get_devices.

<h2>Return Value</h2>

None

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_get_devices/">rdma_get_devices</a>(3) 
