---
title: "ibv_modify_srq(3)"
name: "ibv_modify_srq"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_modify_srq/"
description: "ibv_modify_srq – modify attributes of a shared receive queue (SRQ)"
---

<h2 class="name">NAME</h2>
<p> ibv_modify_srq &#8211; modify attributes of a shared receive queue (SRQ) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_modify_srq(struct ibv_srq *srq,
                   struct ibv_srq_attr *srq_attr,
                   int srq_attr_mask);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_modify_srq()</code> modifies the attributes of SRQ <i>srq</i> with the attributes in <i>srq_attr</i> according to the mask <i>srq_attr_mask</i>. The argument <i>srq_attr</i> is an ibv_srq_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_srq_attr {
    uint32_t max_wr;    /* maximum number of outstanding work requests (WRs) in the SRQ */
    uint32_t max_sge;   /* number of scatter elements per WR (irrelevant for ibv_modify_srq) */
    uint32_t srq_limit; /* the limit value of the SRQ */
};
</code></pre>
<p> The argument <i>srq_attr_mask</i> specifies the SRQ attributes to be modified. The argument is either 0 or the bitwise OR of one or more of the following flags: </p>
<dl>
<dt><code>IBV_SRQ_MAX_WR </code> Resize the SRQ</p>
<dd>
<dt><code>IBV_SRQ_LIMIT </code> Set the SRQ limit</p>
<dd></dl>
<h2>RETURN VALUE</h2>
<p> <code>ibv_modify_srq()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> If any of the modify attributes is invalid, none of the attributes will be modified. </p>
<p> Not all devices support resizing SRQs. To check if a device supports it, check if the <code>IBV_DEVICE_SRQ_RESIZE</code> bit is set in the device capabilities flags. </p>
<p> Modifying the srq_limit arms the SRQ to produce an <code>IBV_EVENT_SRQ_LIMIT_REACHED</code> &quot;low watermark&quot; asynchronous event once the number of WRs in the SRQ drops below srq_limit.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_query_device/">ibv_query_device</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_srq/">ibv_create_srq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_destroy_srq/">ibv_destroy_srq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_srq/">ibv_query_srq</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
