---
title: "ibv_open_qp(3)"
name: "ibv_open_qp"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_open_qp/"
description: "ibv_open_qp – open a shareable queue pair (QP)"
---

<h2 class="name">NAME</h2>
<p> ibv_open_qp &#8211; open a shareable queue pair (QP) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_qp *ibv_open_qp(struct ibv_context *context,
                           struct ibv_qp_open_attr *qp_open_attr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_open_qp()</code> opens an existing queue pair (QP) associated with the extended protection domain <i>xrcd</i>. The argument <i>qp_open_attr</i> is an ibv_qp_open_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_qp_open_attr {
    uint32_t comp_mask;       /* Identifies valid fields */
    uint32_t qp_num;          /* QP number */
    struct *ibv_xrcd;         /* XRC domain */
    void *qp_context;         /* User defined opaque value */
    enum ibv_qp_type qp_type; /* QP transport service type */
</code></pre>
<p> <code>ibv_destroy_qp()</code> closes the opened QP and destroys the underlying QP if it has no other references. <i>qp</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_open_qp()</code> returns a pointer to the opened QP, or NULL if the request fails. Check the QP number (<code>qp_num</code>) in the returned QP.</p>
<h2>NOTES</h2>
<p> <code>ibv_open_qp()</code> will fail if a it is asked to open a QP that does not exist within the xrcd with the specified qp_num and qp_type.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_alloc_pd/">ibv_alloc_pd</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_qp/">ibv_create_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_qp_ex/">ibv_create_qp_ex</a></code>(3), <code><a href="/docs/linux/man/3-ibv_modify_qp/">ibv_modify_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_qp/">ibv_query_qp</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Sean Hefty &lt;sean.hefty [at] intel.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
