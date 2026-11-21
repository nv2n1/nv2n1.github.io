---

title: "ibv_get_device_guid(3)"
name: "ibv_get_device_guid"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_get_device_guid/"
---

ibv_get_device_guid - get an RDMA device's GUID 

<dl>
<dt>
</dt><dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
uint64_t ibv_get_device_guid(struct ibv_device *device);
</code></pre></dd></dl>

ibv_get_device_name() returns the Global Unique IDentifier (GUID) of the RDMA device device.

<h2>RETURN VALUE</h2>

 

 ibv_get_device_guid() returns the GUID of the device in network byte order.

<h2>SEE ALSO</h2>

 

 ibv_get_device_list(3), ibv_get_device_name(3), ibv_open_device(3)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanba [at] gmail.com&gt;
