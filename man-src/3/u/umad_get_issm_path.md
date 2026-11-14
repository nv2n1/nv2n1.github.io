---
title: "umad_get_issm_path(3)"
name: "umad_get_issm_path"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_get_issm_path/"
description: "umad_get_issm_path – get path of issm device"
---

<p>umad_get_issm_path &#8211; get path of issm device</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_get_issm_path(char *ca_name, int portnum, char *path, intmax);</code></pre>
<h2>Description</h2>
<p><code>umad_get_issm_path()</code> resolves path to issm device (which used for setting/clearing PortInfo:CapMask IsSM bit) for <i>portnum</i> of the IB device <i>ca_name</i> , it stores resolved path in <i>path</i> array which cannot exceed <i>max</i> bytes in length (including NULL terminator). Opening issm device sets PortInfo:CapMask IsSM bit and closing clears it.</p>
<h2>Return Value</h2>
<p><code>umad_open_port()</code> returns 0 on success and a negative value on error as follows:<br />
&nbsp;<wbr>-ENODEV IB device can&#8217;t be resolved<br />
&nbsp;<wbr>-EINVAL port is not valid&nbsp;<wbr>(bad <i>portnum</i> or no umad device)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_open_port/">umad_open_port</a></code>(3), <code><a href="/docs/linux/man/3-umad_get_port/">umad_get_port</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Sasha Khapyorsky &lt;sashak [at] voltaire.com&gt;</p>
<dd></dl>
