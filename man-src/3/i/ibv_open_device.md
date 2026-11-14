---
title: "ibv_open_device(3)"
name: "ibv_open_device"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_open_device/"
description: "ibv_open_device, ibv_close_device – open and close an RDMA device context"
---

<h2 class="name">NAME</h2>
<p> ibv_open_device, ibv_close_device &#8211; open and close an RDMA device context </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_context *ibv_open_device(struct ibv_device *device);
int ibv_close_device(struct ibv_context *context);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_open_device()</code> opens the device <i>device</i> and creates a context for further use. </p>
<p> <code>ibv_close_device()</code> closes the device context <i>context</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_open_device()</code> returns a pointer to the allocated device context, or NULL if the request fails. </p>
<p> <code>ibv_close_device()</code> returns 0 on success, -1 on failure.</p>
<h2>NOTES</h2>
<p> <code>ibv_close_device()</code> does not release all the resources allocated using context <i>context</i>. To avoid resource leaks, the user should release all associated resources before closing a context. </p>
<p> Setting the environment variable **RDMAV_ALLOW_DISASSOC_DESTROY** tells the library to relate an EIO from destroy commands as a success as the kernel resources were already released. This comes to prevent memory leakage in the user space area upon device disassociation. Applications using this flag cannot call ibv_get_cq_event or ibv_get_async_event concurrently with any call to an object destruction function. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_get_device_list/">ibv_get_device_list</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_device/">ibv_query_device</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_port/">ibv_query_port</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_gid/">ibv_query_gid</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_pkey/">ibv_query_pkey</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
