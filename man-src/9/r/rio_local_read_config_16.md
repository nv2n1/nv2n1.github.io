---
title: "rio_local_read_config_16(9)"
name: "rio_local_read_config_16"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_local_read_config_16/"
description: "rio_local_read_config_16 – Read 16 bits from local configuration space"
---

<p>rio_local_read_config_16 &#8211; Read 16 bits from local configuration space</p>
<h2>Synopsis</h2>
<pre><code>int rio_local_read_config_16(struct rio_mport *port, u32 offset, u16 *data);</code></pre>
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
<p>Reads 16 bits of data from the specified offset within the local device&#8217;s configuration space.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
