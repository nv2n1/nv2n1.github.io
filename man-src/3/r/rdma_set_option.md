---
title: "rdma_set_option(3)"
name: "rdma_set_option"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_set_option/"
---

rdma_set_option - Set communication options for an rdma_cm_id.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_set_option

    (struct rdma_cm_id *id,

     int level,

     int optname,

     void *optval,

     size_t optlen);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.
<dt>level
<dd>Protocol level of the option to set.
<dt>optname
<dd>Name of the option, relative to the level, to set.
<dt>optval
<dd>Reference to the option data. The data is dependent on the level and optname.
<dt>optlen
<dd>The size of the %optval buffer.</dl>

<h2>Description</h2>

Sets communication options for an rdma_cm_id. This call is used to override the default system settings.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Option details may be found in the relevent header files.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3) 
