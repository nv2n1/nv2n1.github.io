---
title: "ibv_create_comp_channel(3)"
name: "ibv_create_comp_channel"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_create_comp_channel/"
description: "ibv_create_comp_channel, ibv_destroy_comp_channel – create or destroy a completion event channel"
---

<h2 class="name">NAME</h2>
<p> ibv_create_comp_channel, ibv_destroy_comp_channel &#8211; create or destroy a completion event channel </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_comp_channel *ibv_create_comp_channel(struct ibv_context
                                                     *context);
int ibv_destroy_comp_channel(struct ibv_comp_channel *channel);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_create_comp_channel()</code> creates a completion event channel for the RDMA device context <i>context</i>. </p>
<p> <code>ibv_destroy_comp_channel()</code> destroys the completion event channel <i>channel</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_create_comp_channel()</code> returns a pointer to the created completion event channel, or NULL if the request fails. </p>
<p> <code>ibv_destroy_comp_channel()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> A &quot;completion channel&quot; is an abstraction introduced by libibverbs that does not exist in the InfiniBand Architecture verbs specification or RDMA Protocol Verbs Specification. A completion channel is essentially file descriptor that is used to deliver completion notifications to a userspace process. When a completion event is generated for a completion queue (CQ), the event is delivered via the completion channel attached to that CQ. This may be useful to steer completion events to different threads by using multiple completion channels. </p>
<p> <code>ibv_destroy_comp_channel()</code> fails if any CQs are still associated with the completion event channel being destroyed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_cq/">ibv_create_cq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_get_cq_event/">ibv_get_cq_event</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
