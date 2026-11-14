---
title: "ibv_alloc_td(3)"
name: "ibv_alloc_td"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_alloc_td/"
description: "ibv_alloc_td(), ibv_dealloc_td() – allocate and deallocate thread domain object"
---

<h2 class="name">NAME</h2>
<p> ibv_alloc_td(), ibv_dealloc_td() &#8211; allocate and deallocate thread domain object </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_td *ibv_alloc_td(struct ibv_context *context,
                            struct ibv_td_init_attr *init_attr);
int ibv_dealloc_td(struct ibv_td *td);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_alloc_td()</code> allocates a thread domain object for the RDMA device context <i>context</i>. </p>
<p> The thread domain object defines how the verbs libraries and provider will use locks and additional hardware capabilities to achieve best performance for handling multi-thread or single-thread protection. An application assigns verbs resources to a thread domain when it creates a verbs object. </p>
<p> If the <i>ibv_td</i> object is specified then any objects created under this thread domain will disable internal locking designed to protect against concurrent access to that object from multiple user threads. By default all verbs objects are safe for multi-threaded access, whether or not a thread domain is specified. </p>
<p> A <i>struct ibv_td</i> can be added to a parent domain via <code>ibv_alloc_parent_domain()</code> and then the parent domain can be used to create verbs objects. </p>
<p> <code>ibv_dealloc_td()</code> will deallocate the thread domain <i>td</i>. All resources created with the <i>td</i> should be destroyed prior to deallocating the <i>td</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_alloc_td()</code> returns a pointer to the allocated struct <i>ibv_td</i> object, or NULL if the request fails (and sets errno to indicate the failure reason). </p>
<p> <code>ibv_dealloc_td()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_alloc_parent_domain/">ibv_alloc_parent_domain</a></code>(3),</p>
<h2>AUTHORS</h2>
<dl>
<dt>Alex Rosenbaum &lt;alexr [at] mellanox.com&gt;</p>
<dd>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
