---
title: "ibv_reg_dm_mr(3)"
name: "ibv_reg_dm_mr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_reg_dm_mr/"
description: "ibv_alloc_dm, ibv_free_dm, ibv_memcpy_to/from_dm – allocate or free a device memory buffer (DMs) and perform memory copy to or from it"
---

<h2 class="name">NAME</h2>
<p> ibv_alloc_dm, ibv_free_dm, ibv_memcpy_to/from_dm &#8211; allocate or free a device memory buffer (DMs) and perform memory copy to or from it </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_dm *ibv_alloc_dm(struct ibv_context *context,
                            struct ibv_alloc_dm_attr *attr);
int ibv_free_dm(struct ibv_dm *dm);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_alloc_dm()</code> allocates a device memory buffer for the RDMA device context <i>context</i>. The argument <i>attr</i> is a pointer to an ibv_alloc_dm_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<p> <code>ibv_free_dm()</code> free the device memory buffer <i>dm</i>. </p>
<p>struct ibv_alloc_dm_attr {<br />
    size_t length;          /* Length of desired device memory buffer */<br />
    uint32_t log_align_req; /* Log base 2 of address alignment requirement */<br />
    uint32_t comp_mask;     /* Compatibility mask that defines which of the following variables are valid */<br />
};<br />
Address alignment may be required in cases where RDMA atomic operations will be performed using the device memory.In such cases, the user may specify the device memory start address alignment using the log_align_req parameter<br />
                                                                                                                                     in the allocation attributes struct.</p>
<h2>Accessing an allocated device memory</h2>
<p>In order to perform a write / read memory access to an allocated device memory, a user could use the ibv_memcpy_to_dm<br />
                                                                                    and ibv_memcpy_from_dm calls respectively.int<br />
                                                                                    ibv_memcpy_to_dm(struct ibv_dm *dm, uint64_t dm_offset,<br />
                                                                                                     void *host_addr, size_t length);<br />
int ibv_memcpy_from_dm(void *host_addr, struct ibv_dm *dm,<br />
                       uint64_t dm_offset, size_t length);<br />
dm_offest<br />
    is the byte offset from the beginning of the allocated device memory buffer to access.host_addr<br />
        is the host memory buffer address to access.length<br />
            is the copy length in bytes.</p>
<h2>Device memory registration</h2>
<pre><code>
User may register the allocated device memory as a memory region and use the lkey / rkey inside sge when posting receive or sending work request.This type of MR is defined as zero based and therefore any reference to it(specifically in sge)
                                                                                                                                is done with a byte offset from the beginning of the region.This type of registration is done using ibv_reg_dm_mr.struct ibv_mr *ibv_reg_dm_mr(struct ibv_pd *pd, struct ibv_dm *dm, uint64_t dm_offset,
                                                                                                                                                                                                                                                                               size_t length, uint32_t access);
pd
the associated pd for this registration.
dm
the associated dm for this registartion.
dm_offest
is the byte offset from the beginning of the allocated device memory buffer to register.
length
the memory length to register.
access
mr access flags (Use enum ibv_access_flags). For this type of registration, user must set the IBV_ACCESS_ZERO_BASED
flag.
</code></pre>
<h2>RETURN VALUE</h2>
<p> <code>ibv_alloc_dm()</code> returns a pointer to an ibv_dm struct or NULL if the request fails. </p>
<p> <code>ibv_free_dm()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason). </p>
<p> <code>ibv_reg_dm_mr()</code> returns a pointer to an ibv_mr struct on success or NULL if request fails. </p>
<p> <code>ibv_memcpy_to_dm()/ibv_memcpy_from_dm()</code> returns 0 on success or the failure reason value on failure.</p>
<h2>NOTES</h2>
<p> <code>ibv_alloc_dm()</code> may fail if device has no more free device memory left, where the maximum amount of allocated memory is provided by the <i>max_dm_size</i> attribute in <i>ibv_device_attr_ex</i> struct. <code>ibv_free_dm()</code> may fail if any other resources (such as an MR) is still associated with the DM being freed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_query_device_ex/">ibv_query_device_ex</a></code>(3),</p>
<h2>AUTHORS</h2>
<dl>
<dt>Ariel Levkovich &lt;lariel [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
