---
title: "ibv_alloc_pd(3)"
name: "ibv_alloc_pd"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_alloc_pd/"
description: "ibv_alloc_pd, ibv_dealloc_pd – allocate or deallocate a protection domain (PDs)"
---

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
<p> <code>ibv_reg_mr</code>(3), <code>ibv_create_srq</code>(3), <code>ibv_create_qp</code>(3), <code>ibv_create_ah</code>(3), <code>ibv_create_ah_from_wc</code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</dt>
<dd>
</dd></dl>
