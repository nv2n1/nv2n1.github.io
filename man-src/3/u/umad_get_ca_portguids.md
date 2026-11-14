---
title: "umad_get_ca_portguids(3)"
name: "umad_get_ca_portguids"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_get_ca_portguids/"
description: "umad_get_ca_portguids – get the InfiniBand device ports GUIDs"
---

<p>umad_get_ca_portguids &#8211; get the InfiniBand device ports GUIDs</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_get_ca_portguids(char *ca_name, uint64_t *portguids, int max);</code></pre>
<h2>Description</h2>
<p><code>umad_get_ca_portguids()</code> fills the <i>portguids</i> array with up to <i>max</i> port GUIDs belonging the specified IB device <i>ca_name</i> , or to the default IB device if <i>ca_name</i> is NULL. The argument <i>portguids</i> is an array of <i>max</i> uint64_t entries.</p>
<h2>Return Value</h2>
<p>On success, <code>umad_get_ca_portguids()</code> returns a non-negative value equal to the number of port GUIDs actually filled. On failure, a negative value is returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_get_cas_names/">umad_get_cas_names</a></code>(3)</p>
<h2>Authors</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd>
<dt>Dotan Barak &lt;dotanb [at] mellanox.co.il&gt;</p>
<dd></dl>
