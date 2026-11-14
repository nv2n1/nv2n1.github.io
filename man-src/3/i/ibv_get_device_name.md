---
title: "ibv_get_device_name(3)"
name: "ibv_get_device_name"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_get_device_name/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_get_device_name - get an RDMA device's name 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
const char *ibv_get_device_name(struct ibv_device *device);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_get_device_name() returns a human-readable name associated with the RDMA device device.

<h2>RETURN VALUE</h2>

 

 ibv_get_device_name() returns a pointer to the device name, or NULL if the request fails.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_get_device_guid/">ibv_get_device_guid</a>(3), <a HREF="/docs/linux/man/3-ibv_get_device_list/">ibv_get_device_list</a>(3), <a HREF="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a>(3)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanba [at] gmail.com&gt; 

<h2>Index</h2>


