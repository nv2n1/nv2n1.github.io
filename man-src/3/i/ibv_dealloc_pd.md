---
title: "ibv_dealloc_pd(3)"
name: "ibv_dealloc_pd"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_dealloc_pd/"
description: "ibv_alloc_pd, ibv_dealloc_pd – allocate or deallocate a protection domain (PDs)"
---

<h2 class="name">NAME</h2>
<p> ibv_alloc_pd, ibv_dealloc_pd &#8211; allocate or deallocate a protection domain (PDs) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_pd *ibv_alloc_pd(struct ibv_context *context);
int ibv_dealloc_pd(struct ibv_pd *pd);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_alloc_pd()</code> allocates a PD for the RDMA device context <i>context</i>. </p>
<p> <code>ibv_dealloc_pd()</code> deallocates the PD <i>pd</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_alloc_pd()</code> returns a pointer to the allocated PD, or NULL if the request fails. </p>
<p> <code>ibv_dealloc_pd()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> <code>ibv_dealloc_pd()</code> may fail if any other resource is still associated with the PD being freed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_reg_mr/">ibv_reg_mr</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_srq/">ibv_create_srq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_qp/">ibv_create_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_ah/">ibv_create_ah</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_ah_from_wc/">ibv_create_ah_from_wc</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
