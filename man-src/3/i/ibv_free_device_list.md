---
title: "ibv_free_device_list(3)"
name: "ibv_free_device_list"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_free_device_list/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_get_device_list, ibv_free_device_list - get and release list of available RDMA devices 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_device **ibv_get_device_list(int *num_devices);
void ibv_free_device_list(struct ibv_device **list);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_get_device_list() returns a NULL-terminated array of RDMA devices currently available. The argument num_devices is optional; if not NULL, it is set to the number of devices returned in the array. 

 ibv_free_device_list() frees the array of devices list returned by ibv_get_device_list().

<h2>RETURN VALUE</h2>

 

 ibv_get_device_list() returns the array of available RDMA devices, or sets errno and returns NULL if the request fails. If no devices are found then num_devices is set to 0, and non-NULL is returned. 

 ibv_free_device_list() returns no value.

<h2>ERRORS</h2>

<dl>
<dt>EPERM
<dd> Permission denied.
<dt>ENOSYS
<dd> No kernel support for RDMA.
<dt>ENOMEM
<dd> Insufficient memory to complete the operation.</dl>

<h2>NOTES</h2>

 

 Client code should open all the devices it intends to use with ibv_open_device() before calling ibv_free_device_list(). Once it frees the array with ibv_free_device_list(), it will be able to use only the open devices; pointers to unopened devices will no longer be valid. 

 Setting the environment variable IBV_SHOW_WARNINGS will cause warnings to be emitted to stderr if a kernel verbs device is discovered, but no corresponding userspace driver can be found for it.

<h2>STATIC LINKING</h2>

 

 If libibverbs is statically linked to the application then all provider drivers must also be statically linked. The library will not load dynamic providers when static linking is used. 

 To link the providers set the RDMA_STATIC_PROVIDERS define to the comma separated list of desired providers when compiling the application. The special keyword `all' will statically link all supported libibverbs providers. 

 This is intended to be used along with <a HREF="/docs/linux/man/1-pkg-config/">pkg-config</a>(1) to setup the proper flags for libibverbs linking. 

 If this is not done then ibv_get_device_list will always return an empty list. 

 Using only dynamic linking for libibverbs applications is strongly recommended.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_fork_init/">ibv_fork_init</a>(3), <a HREF="/docs/linux/man/3-ibv_get_device_guid/">ibv_get_device_guid</a>(3), <a HREF="/docs/linux/man/3-ibv_get_device_name/">ibv_get_device_name</a>(3), <a HREF="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a>(3)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanba [at] gmail.com&gt; 

<h2>Index</h2>


