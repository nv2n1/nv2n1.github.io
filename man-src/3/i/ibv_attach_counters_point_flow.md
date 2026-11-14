---
title: "ibv_attach_counters_point_flow(3)"
name: "ibv_attach_counters_point_flow"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_attach_counters_point_flow/"
description: "ibv_attach_counters_point_flow – attach individual counter definition to a flow object"
---

<h2 class="name">NAME</h2>
<p> ibv_attach_counters_point_flow &#8211; attach individual counter definition to a flow object </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_attach_counters_point_flow(struct ibv_counters *counters,
                                   struct ibv_counter_attach_attr *counter_attach_attr,
                                   struct ibv_flow *flow);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> Attach counters point are a family of APIs to attach individual counter description definition to a verb object at a specific index location. </p>
<p> Counters object will start collecting values after it is bound to the verb object resource. </p>
<p> A static attach can be created when NULL is provided instead of the reference to the verbs object (e.g.: in case of flow providing NULL instead of flow). In this case, this counters object will only start collecting values after it is bound to the verbs resource, for flow this is when referencing the counters handle when creating a flow with ibv_create_flow(). </p>
<p> Once an ibv_counters is bound statically to a verbs resource, no additional attach is allowed till the counter object is not bound to any verb object. </p>
<p> The argument counter_desc specifies which counter value should be collected. It is defined in verbs.h as one of the enum ibv_counter_description options. </p>
<p> Supported capabilities of specific counter_desc values per verbs object can be tested by checking the return value for success or ENOTSUP errno. </p>
<p> Attaching a counters handle to multiple objects of the same type will accumulate the values into a single index. e.g.: creating several ibv_flow(s) with the same ibv_counters handle will collect the values from all relevant flows into the relevant index location when reading the values from ibv_read_counters(), setting the index more than once with different or same counter_desc will aggregate the values from all relevant counters into the relevant index location. </p>
<p> The runtime values of counters can be read from the hardware by calling ibv_read_counters().</p>
<h2>ARGUMENTS</h2>
<dl>
<dt>counters</p>
<dd> Existing counters to attach new counter point on.</p>
<dt>counter_attach_attr</p>
<dd> An ibv_counter_attach_attr struct, as defined in verbs.h.</p>
<dt>flow</p>
<dd> Existing flow to attach a new counters point on (in static mode it must be NULL).</dl>
<h3>counter_attach_attr Argument</h3>
<dl>
<dt>
<dd>
struct ibv_counter_attach_attr {<br />
    enum ibv_counter_description counter_desc;<br />
    uint32_t index;<br />
    uint32_t comp_mask;<br />
};
</dl>
<h3>counter_desc Argument</h3>
<dl>
<dt>
<dd>
<pre><code>
enum ibv_counter_description {
    IBV_COUNTER_PACKETS,
    IBV_COUNTER_BYTES,
};
</code></pre>
<dt>index</p>
<dd> Desired location of the specific counter at the counters object.</p>
<dt>comp_mask</p>
<dd> Bitmask specifying what fields in the structure are valid.</dl>
<h2>RETURN VALUE</h2>
<p> ibv_attach_counters_point_flow() returns 0 on success, or the value of errno on failure (which indicates the failure reason)</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> invalid argument(s) passed</p>
<dt><code>ENOTSUP</code></p>
<dd> counter_desc is not supported on the requested object</p>
<dt><code>EBUSY</code></p>
<dd> the counter object is already bound to a flow, additional attach calls is not allowed (valid for static attach only)</p>
<dt><code>ENOMEM</code></p>
<dd> not enough memory</dl>
<h2>NOTES</h2>
<p> Counter values in each index location are cleared upon creation when calling ibv_create_counters(). Attaching counters points will only increase these values accordingly.</p>
<h2>EXAMPLE</h2>
<p> An example of use of ibv_attach_counters_point_flow() is shown in ibv_read_counters</p>
<h2>SEE ALSO</h2>
<p> ibv_create_counters, ibv_destroy_counters, ibv_read_counters, ibv_create_flow</p>
<h2>AUTHORS</h2>
<p> Raed Salem &lt;raeds [at] mellanox.com&gt; </p>
<p> Alex Rosenbaum &lt;alexr [at] mellanox.com&gt; </p>
<h2>Index</h2>
