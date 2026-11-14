---
title: "ibv_query_rt_values_ex(3)"
name: "ibv_query_rt_values_ex"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_query_rt_values_ex/"
description: "ibv_query_rt_values_ex – query an RDMA device for some real time values"
---

<h2 class="name">NAME</h2>
<p> ibv_query_rt_values_ex &#8211; query an RDMA device for some real time values </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_query_rt_values_ex(struct ibv_context *context,
                           struct ibv_values_ex *values);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_query_rt_values_ex()</code> returns certain real time values of a device <i>context</i>. The argument <i>attr</i> is a pointer to an ibv_device_attr_ex struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_values_ex {
    uint32_t comp_mask;        /* Compatibility mask that defines the query/queried fields [in/out] */
    struct timespec raw_clock; /* HW raw clock */
};
enum ibv_values_mask {
    IBV_VALUES_MASK_RAW_CLOCK = 1 &lt;&lt; 0, /* HW raw clock */
};
</code></pre>
<h2>RETURN VALUE</h2>
<p> <code>ibv_query_rt_values_ex()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> This extension verb only calls the provider, the provider has to query this value somehow and mark the queried values in the comp_mask field.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_query_device/">ibv_query_device</a></code>(3), <code><a href="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_port/">ibv_query_port</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_pkey/">ibv_query_pkey</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_gid/">ibv_query_gid</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Matan Barak &lt;matanb [at] mellanox.com&gt;</p>
<dd>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
