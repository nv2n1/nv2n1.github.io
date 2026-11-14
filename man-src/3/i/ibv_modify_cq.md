---
title: "ibv_modify_cq(3)"
name: "ibv_modify_cq"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_modify_cq/"
description: "ibv_modify_cq – modify a completion queue (CQ)"
---

<h2 class="name">NAME</h2>
<p> ibv_modify_cq &#8211; modify a completion queue (CQ) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_modify_cq(struct ibv_cq *cq, struct ibv_modify_cq_attr *cq_attr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_modify_cq()</code> modify a CQ <i>cq</i>. The argument <i>cq_attr</i> is an ibv_modify_cq_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_moderate_cq {
    uint16_t cq_count;  /* number of completions per event */
    uint16_t cq_period; /* in micro seconds */
};
struct ibv_modify_cq_attr {
    uint32_t attr_mask;
    struct ibv_moderate_cq moderate;
};
</code></pre>
<p> The function <code>ibv_modify_cq()</code> will modify the CQ, based on the given <i>cq_attr</i>-&gt;attr_mask</p>
<h2>RETURN VALUE</h2>
<p> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_cq/">ibv_create_cq</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Yonatan Cohen &lt;yonatanc [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
