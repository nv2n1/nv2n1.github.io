---
title: "rio_write_config_8(9)"
name: "rio_write_config_8"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_write_config_8/"
description: "rio_write_config_8 – Write 8 bits to configuration space"
---

<p>rio_write_config_8 &#8211; Write 8 bits to configuration space</p>
<h2>Synopsis</h2>
<pre><code>int rio_write_config_8(struct rio_dev *rdev, u32 offset, u8 data);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device</dl>
<p> <i>offset</i></p>
<dl>
<dd>Offset into device configuration space</dl>
<p> <i>data</i></p>
<dl>
<dd>Data to be written</dl>
<h2>Description</h2>
<p>Writes 8 bits of data to the specified offset within the RIO device&#8217;s configuration space.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
