---
title: "ibv_get_device_guid(3)"
name: "ibv_get_device_guid"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_get_device_guid/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_get_device_guid - get an RDMA device's GUID 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
uint64_t ibv_get_device_guid(struct ibv_device *device);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_get_device_name() returns the Global Unique IDentifier (GUID) of the RDMA device device.

<h2>RETURN VALUE</h2>

 

 ibv_get_device_guid() returns the GUID of the device in network byte order.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_get_device_list/">ibv_get_device_list</a>(3), <a HREF="/docs/linux/man/3-ibv_get_device_name/">ibv_get_device_name</a>(3), <a HREF="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a>(3)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanba [at] gmail.com&gt; 

<h2>Index</h2>


