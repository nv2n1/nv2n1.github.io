---
title: "ibv_dealloc_mw(3)"
name: "ibv_dealloc_mw"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_dealloc_mw/"
description: "ibv_alloc_mw, ibv_dealloc_mw – allocate or deallocate a memory window (MW)"
---

<h2 class="name">NAME</h2>
<p> ibv_alloc_mw, ibv_dealloc_mw &#8211; allocate or deallocate a memory window (MW) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_mw *ibv_alloc_mw(struct ibv_pd *pd,
                            enum ibv_mw_type type);
int ibv_dealloc_mw(struct ibv_mw *mw);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_alloc_mw()</code> allocates a memory window (MW) associated with the protection domain <i>pd</i>. The MW&#8217;s type (1 or 2A/2B) is <i>type</i>. </p>
<p> The MW is created not bound. For it to be useful, the MW must be bound, through either ibv_bind_mw (type 1) or a special WR (type 2). Once bound, the memory window allows RDMA (remote) access to a subset of the MR to which it was bound, until invalidated by: ibv_bind_mw verb with zero length for type 1, IBV_WR_LOCAL_INV/IBV_WR_SEND_WITH_INV WR opcode for type 2, deallocation. </p>
<p> <code>ibv_dealloc_mw()</code> Unbinds in case was previously bound and deallocates the MW <i>mw</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_alloc_mw()</code> returns a pointer to the allocated MW, or NULL if the request fails. The remote key (<code>R_Key</code>) field <code>rkey</code> is used by remote processes to perform Atomic and RDMA operations. This key will be changed during bind operations. The remote process places this <code>rkey</code> as the rkey field of struct ibv_send_wr passed to the ibv_post_send function. </p>
<p> <code>ibv_dealloc_mw()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> <code>ibv_dereg_mr()</code> fails if any memory window is still bound to this MR.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_alloc_pd/">ibv_alloc_pd</a></code>(3), <code><a href="/docs/linux/man/3-ibv_post_send/">ibv_post_send</a></code>(3), <code><a href="/docs/linux/man/3-ibv_bind_mw/">ibv_bind_mw</a></code>(3), <code><a href="/docs/linux/man/3-ibv_reg_mr/">ibv_reg_mr</a></code>(3),</p>
<h2>AUTHORS</h2>
<dl>
<dt>Majd Dibbiny &lt;majd [at] mellanox.com&gt;</p>
<dd>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
