---
title: "ibnd_iter_nodes(3)"
name: "ibnd_iter_nodes"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibnd_iter_nodes/"
description: "ibnd_iter_nodes, ibnd_iter_nodes_type – given a fabric object and a function itterate over the nodes in the fabric."
---

<h2>NAME</h2>
<p> ibnd_iter_nodes, ibnd_iter_nodes_type &#8211; given a fabric object and a function itterate over the nodes in the fabric.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/ibnetdisc.h&gt;
void ibnd_iter_nodes(ibnd_fabric_t *fabric, ibnd_iter_func_t func, void *user_data) void ibnd_iter_nodes_type(ibnd_fabric_t *fabric, ibnd_iter_func_t func, ibnd_node_type_t type, void *user_data)
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibnd_iter_nodes()</code> Itterate through all the nodes in the fabric and call &quot;func&quot; on them. <code>ibnd_iter_nodes_type()</code> The same as ibnd_iter_nodes except to limit the iteration to the nodes with the specified type.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibnd_iter_nodes(), ibnd_iter_nodes_type()</code> NONE</p>
<h2>AUTHORS</h2>
<dl>
<dt>Ira Weiny &lt;weiny2 [at] llnl.gov&gt;</p>
<dd>
</dl>
<h2>Index</h2>
