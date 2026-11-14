---
title: "ibnd_find_node_guid(3)"
name: "ibnd_find_node_guid"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibnd_find_node_guid/"
description: "ibnd_find_node_guid, ibnd_find_node_dr – given a fabric object find the node object within it which matches the guid or directed route specified."
---

<h2>NAME</h2>
<p> ibnd_find_node_guid, ibnd_find_node_dr &#8211; given a fabric object find the node object within it which matches the guid or directed route specified.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/ibnetdisc.h&gt;
ibnd_node_t *ibnd_find_node_guid(ibnd_fabric_t *fabric, uint64_t guid)
    ibnd_node_t *ibnd_find_node_dr(ibnd_fabric_t *fabric, char *dr_str)
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibnd_find_node_guid()</code> Given a fabric object and a guid, return the ibnd_node_t object with that node guid. <code>ibnd_find_node_dr()</code> Given a fabric object and a directed route, return the ibnd_node_t object with that directed route.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibnd_find_node_guid(), ibnd_find_node_dr()</code> return NULL on failure, otherwise a valid ibnd_node_t object.</p>
<h2>AUTHORS</h2>
<dl>
<dt>Ira Weiny &lt;weiny2 [at] llnl.gov&gt;</p>
<dd>
</dl>
<h2>Index</h2>
