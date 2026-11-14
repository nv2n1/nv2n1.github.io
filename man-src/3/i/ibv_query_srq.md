---
title: "ibv_query_srq(3)"
name: "ibv_query_srq"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_query_srq/"
description: "ibv_query_srq – get the attributes of a shared receive queue (SRQ)"
---

<h2 class="name">NAME</h2>
<p> ibv_query_srq &#8211; get the attributes of a shared receive queue (SRQ) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_query_srq(struct ibv_srq *srq, struct ibv_srq_attr *srq_attr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_query_srq()</code> gets the attributes of the SRQ <i>srq</i> and returns them through the pointer <i>srq_attr</i>. The argument <i>srq_attr</i> is an ibv_srq_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_srq_attr {
    uint32_t max_wr;    /* maximum number of outstanding work requests (WRs) in the SRQ */
    uint32_t max_sge;   /* maximum number of scatter elements per WR */
    uint32_t srq_limit; /* the limit value of the SRQ */
};
</code></pre>
<h2>RETURN VALUE</h2>
<p> <code>ibv_query_srq()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> If the value returned for srq_limit is 0, then the SRQ limit reached (&quot;low watermark&quot;) event is not (or no longer) armed, and no asynchronous events will be generated until the event is rearmed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_srq/">ibv_create_srq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_destroy_srq/">ibv_destroy_srq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_modify_srq/">ibv_modify_srq</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
