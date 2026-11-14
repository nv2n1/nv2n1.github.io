---
title: "ibv_destroy_counters(3)"
name: "ibv_destroy_counters"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_destroy_counters/"
description: "ibv_create_counters, ibv_destroy_counters – Create or destroy a counters handle"
---

<h2 class="name">NAME</h2>
<p> ibv_create_counters, ibv_destroy_counters &#8211; Create or destroy a counters handle </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_counters *
ibv_create_counters(struct ibv_context *context,
                    struct ibv_counters_init_attr *init_attr);
int ibv_destroy_counters(struct ibv_counters *counters);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> ibv_create_counters() creates a new counters handle for the RDMA device context. </p>
<p> An ibv_counters handle can be attached to a verbs resource (e.g.: QP, WQ, Flow) statically when these are created. </p>
<p> For example attach an ibv_counters statically to a Flow (struct ibv_flow) during creation of a new Flow by calling ibv_create_flow(). </p>
<p> Counters are cleared upon creation and values will be monotonically increasing. </p>
<p> ibv_destroy_counters() releases the counters handle, user should detach the counters object before destroying it.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt>context</p>
<dd> RDMA device context to create the counters on.</p>
<dt>init_attr</p>
<dd> Is an ibv_counters_init_attr struct, as defined in verbs.h.</dl>
<h3>init_attr Argument</h3>
<dl>
<dt>
<dd>
<pre><code>
struct ibv_counters_init_attr {
    int comp_mask;
};
</code></pre>
<dt>comp_mask</p>
<dd> Bitmask specifying what fields in the structure are valid.</dl>
<h2>RETURN VALUE</h2>
<p> ibv_create_counters() returns a pointer to the allocated ibv_counters object, or NULL if the request fails (and sets errno to indicate the failure reason) </p>
<p> ibv_destroy_counters() returns 0 on success, or the value of errno on failure (which indicates the failure reason)</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EOPNOTSUPP</code></p>
<dd> ibv_create_counters() is not currently supported on this device (ENOSYS may sometimes be returned by old versions of libibverbs).</p>
<dt><code>ENOMEM</code></p>
<dd> ibv_create_counters() could not create ibv_counters object, not enough memory</p>
<dt><code>EINVAL</code></p>
<dd> invalid parameter supplied ibv_destroy_counters()</dl>
<h2>EXAMPLE</h2>
<p> An example of use of ibv_counters is shown in ibv_read_counters</p>
<h2>SEE ALSO</h2>
<p> ibv_attach_counters_point_flow, ibv_read_counters, ibv_create_flow</p>
<h2>AUTHORS</h2>
<p> Raed Salem &lt;raeds [at] mellanox.com&gt; </p>
<p> Alex Rosenbaum &lt;alexr [at] mellanox.com&gt; </p>
<h2>Index</h2>
