---
title: "umad_get_cas_names(3)"
name: "umad_get_cas_names"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_get_cas_names/"
description: "umad_get_cas_names – get list of available InfiniBand device names"
---

<p>umad_get_cas_names &#8211; get list of available InfiniBand device names</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_get_cas_names(char cas[][UMAD_CA_NAME_LEN], int max);</code></pre>
<h2>Description</h2>
<p><code>umad_get_cas_names()</code> fills the <i>cas</i> array with up to <i>max</i> local IB devices (CAs) names. The argument <i>cas</i> is a character array with <i>max</i> entries, each with <code>UMAD_CA_NAME_LEN</code> characters.</p>
<h2>Return Value</h2>
<p><code>umad_get_cas_names()</code> returns a non-negative value equal to the number of entries filled, or -1 on errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_get_ca_portguids/">umad_get_ca_portguids</a></code>(3), <code><a href="/docs/linux/man/3-umad_open_port/">umad_open_port</a></code>(3)</p>
<h2>Authors</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd>
<dt>Dotan Barak &lt;dotanb [at] mellanox.co.il&gt;</p>
<dd></dl>
