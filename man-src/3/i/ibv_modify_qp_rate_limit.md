---
title: "ibv_modify_qp_rate_limit(3)"
name: "ibv_modify_qp_rate_limit"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_modify_qp_rate_limit/"
description: "ibv_modify_qp_rate_limit – modify the send rate limits attributes of a queue pair (QP)"
---

<h2 class="name">NAME</h2>
<p> ibv_modify_qp_rate_limit &#8211; modify the send rate limits attributes of a queue pair (QP) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_modify_qp_rate_limit(struct ibv_qp *qp, struct ibv_qp_rate_limit_attr *attr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_modify_qp_rate_limit()</code> modifies the send rate limiting packet pacing attributes of QP <i>qp</i> with the attributes in <i>attr</i>. The argument <i>attr</i> is an ibv_qp_rate_limit_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<p> The <i>rate_limit</i> defines the MAX send rate this QP will send as long as the link in not blocked and there are work requests in send queue. </p>
<p> Finer control for shaping the rate limit of a QP is achieved by defining the <i>max_burst_sz</i>, single burst max bytes size and the <i>typical_pkt_sz</i>, typical packet bytes size. These allow the device to adjust the inter-burst gap delay required to correctly shape the scheduling of sends to the wire in order to reach for requested application requirements. </p>
<p> Setting a value of 0 for <i>max_burst_sz</i> or <i>typical_pkt_sz</i> will use the devices defaults. <i>typical_pkt_sz</i> will default to the port&#8217;s MTU value. </p>
<pre><code>
struct ibv_qp_rate_limit_attr {
    uint32_t rate_limit;     /* kbps */
    uint32_t max_burst_sz;   /* bytes */
    uint16_t typical_pkt_sz; /* bytes */
};
</code></pre>
<h2>RETURN VALUE</h2>
<p> <code>ibv_modify_qp_rate_limit()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>ERRORS</h2>
<h3>EINVAL</h3>
<p> Invalid arguments.</p>
<h3>EOPNOTSUPP</h3>
<p> Function is not implemented for this device. (ENOSYS may sometimes be returned by old versions of libibverbs). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_qp/">ibv_create_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_destroy_qp/">ibv_destroy_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_modify_qp/">ibv_modify_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_qp/">ibv_query_qp</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Alex Rosenbaum &lt;alexr [at] mellanox.com&gt;</p>
<dd>
<dt>Bodong Wang &lt;bodong [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
