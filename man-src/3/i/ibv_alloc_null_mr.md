---
title: "ibv_alloc_null_mr(3)"
name: "ibv_alloc_null_mr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_alloc_null_mr/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_alloc_null_mr - allocate a null memory region (MR) 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_mr *ibv_alloc_null_mr(struct ibv_pd *pd);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_alloc_null_mr() allocates a null memory region (MR) that is associated with the protection domain pd. 

 A null MR discards all data written to it, and always returns 0 on read. It has the maximum length and only the lkey is valid, the MR is not exposed as an rkey. 

 A device should implement the null MR in a way that bypasses PCI transfers, internally discarding or sourcing 0 data. This provides a way to avoid PCI bus transfers by using a scatter/gather list in commands if applications do not intend to access the data, or need data to be 0 filled. 

 Specifically upon ibv_post_send() the device skips PCI read cycles and upon ibv_post_recv() the device skips PCI write cycles which finally improves performance. 

 ibv_dereg_mr() deregisters the MR. The use of ibv_rereg_mr() or ibv_bind_mw() with this MR is invalid.

<h2>RETURN VALUE</h2>

 

 ibv_alloc_null_mr() returns a pointer to the allocated MR, or NULL if the request fails.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_reg_mr/">ibv_reg_mr</a>(3), <a HREF="/docs/linux/man/3-ibv_dereg_mr/">ibv_dereg_mr</a>(3),

<h2>AUTHOR</h2>

 

 Yonatan Cohen &lt;yonatanc [at] mellanox.com&gt; 

<h2>Index</h2>


