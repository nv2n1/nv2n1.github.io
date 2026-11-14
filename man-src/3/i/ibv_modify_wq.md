---
title: "ibv_modify_wq(3)"
name: "ibv_modify_wq"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_modify_wq/"
description: "ibv_modify_wq – Modify a Work Queue (WQ)."
---

<h2 class="name">NAME</h2>
<p> ibv_modify_wq &#8211; Modify a Work Queue (WQ). </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct int ibv_modify_wq(struct ibv_wq *wq,
                         struct ibv_wq_attr *wq_attr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_modify_wq()</code> modifys a WQ <i>wq</i>. The argument <i>wq_attr</i> is an ibv_wq_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_wq_attr {
    uint32_t attr_mask;              /* Use enum ibv_wq_attr_mask */
    enum ibv_wq_state wq_state;      /* Move to this state */
    enum ibv_wq_state curr_wq_state; /* Assume this is the current state */
    uint32_t flags;                  /* Flags values to modify, use enum ibv_wq_flags */
    uint32_t flags_mask;             /* Which flags to modify, use enum ibv_wq_flags */
};
</code></pre>
<p> The function <code>ibv_modify_wq()</code> will modify the WQ based on the given <i>wq_attr</i>-&gt;attr_mask</p>
<h2>RETURN VALUE</h2>
<p> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_wq/">ibv_create_wq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_destroy_wq/">ibv_destroy_wq</a></code>(3),</p>
<h2>AUTHORS</h2>
<dl>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
