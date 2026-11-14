---
title: "rio_local_read_config_8(9)"
name: "rio_local_read_config_8"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_local_read_config_8/"
description: "rio_local_read_config_8 – Read 8 bits from local configuration space"
---

<p>rio_local_read_config_8 &#8211; Read 8 bits from local configuration space</p>
<h2>Synopsis</h2>
<pre><code>int rio_local_read_config_8(struct rio_mport *port, u32 offset, u8 *data);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>Master port</dl>
<p> <i>offset</i></p>
<dl>
<dd>Offset into local configuration space</dl>
<p> <i>data</i></p>
<dl>
<dd>Pointer to read data into</dl>
<h2>Description</h2>
<p>Reads 8 bits of data from the specified offset within the local device&#8217;s configuration space.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
