---
title: "ibv_create_ah_from_wc(3)"
name: "ibv_create_ah_from_wc"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_create_ah_from_wc/"
description: "ibv_init_ah_from_wc, ibv_create_ah_from_wc – initialize or create an address handle (AH) from a work completion"
---

<h2 class="name">NAME</h2>
<p> ibv_init_ah_from_wc, ibv_create_ah_from_wc &#8211; initialize or create an address handle (AH) from a work completion </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_init_ah_from_wc(struct ibv_context *context, uint8_t port_num,
                        struct ibv_wc *wc, struct ibv_grh *grh,
                        struct ibv_ah_attr *ah_attr);
struct ibv_ah *ibv_create_ah_from_wc(struct ibv_pd *pd,
                                     struct ibv_wc *wc,
                                     struct ibv_grh *grh,
                                     uint8_t port_num);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_init_ah_from_wc()</code> initializes the address handle (AH) attribute structure <i>ah_attr</i> for the RDMA device context <i>context</i> using the port number <i>port_num</i>, using attributes from the work completion <i>wc</i> and the Global Routing Header (GRH) structure <i>grh</i>. </p>
<p> <code>ibv_create_ah_from_wc()</code> creates an AH associated with the protection domain <i>pd</i> using the port number <i>port_num</i>, using attributes from the work completion <i>wc</i> and the Global Routing Header (GRH) structure <i>grh</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_init_ah_from_wc()</code> returns 0 on success, and -1 on error. </p>
<p> <code>ibv_create_ah_from_wc()</code> returns a pointer to the created AH, or NULL if the request fails.</p>
<h2>NOTES</h2>
<p> The filled structure <i>ah_attr</i> returned from <code>ibv_init_ah_from_wc()</code> can be used to create a new AH using <code>ibv_create_ah()</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a></code>(3), <code><a href="/docs/linux/man/3-ibv_alloc_pd/">ibv_alloc_pd</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_ah/">ibv_create_ah</a></code>(3), <code><a href="/docs/linux/man/3-ibv_destroy_ah/">ibv_destroy_ah</a></code>(3), <code><a href="/docs/linux/man/3-ibv_poll_cq/">ibv_poll_cq</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
