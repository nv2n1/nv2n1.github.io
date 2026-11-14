---
title: "umad_open_port(3)"
name: "umad_open_port"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_open_port/"
description: "umad_open_port – open InfiniBand device port for umad access"
---

<p>umad_open_port &#8211; open InfiniBand device port for umad access</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_open_port(char *ca_name, int portnum);</code></pre>
<h2>Description</h2>
<p><code>umad_open_port()</code> opens the port <i>portnum</i> of the IB device <i>ca_name</i> for umad access. The port is selected by the library if not all parameters are provided (see <code>umad_get_port()</code> for details).</p>
<h2>Return Value</h2>
<p><code>umad_open_port()</code> returns 0 or an unique positive value of umad device descriptor on success, and a negative value on error as follows:<br />
&nbsp;<wbr>-ENODEV IB device can&#8217;t be resolved<br />
&nbsp;<wbr>-EINVAL port is not valid&nbsp;<wbr>(bad <i>portnum</i> or no umad device)<br />
&nbsp;<wbr>-EIO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>umad device for this port can&#8217;t be opened</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_close_port/">umad_close_port</a></code>(3), <code><a href="/docs/linux/man/3-umad_get_cas_names/">umad_get_cas_names</a></code>(3), <code><a href="/docs/linux/man/3-umad_get_port/">umad_get_port</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
