---
title: "struct_rio_scan_node(9)"
name: "struct_rio_scan_node"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_scan_node/"
description: "struct_rio_scan_node – list node to register RapidIO enumeration and discovery methods with RapidIO core."
---

<p>struct_rio_scan_node &#8211; list node to register RapidIO enumeration and discovery methods with RapidIO core.</p>
<h2>Synopsis</h2>
<pre><code>struct rio_scan_node {
    int mport_id;
    struct list_head node;
    struct rio_scan *ops;
};</code></pre>
<h2>Members</h2>
<p>mport_id</p>
<dl>
<dd>ID of an mport (net) serviced by this enumerator</dl>
<p> node</p>
<dl>
<dd>node in global list of registered enumerators</dl>
<p> ops</p>
<dl>
<dd>RIO enumeration and discovery operations</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
