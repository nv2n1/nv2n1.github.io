---
title: "rio_lop_write(9)"
name: "rio_lop_write"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_lop_write/"
description: "RIO_LOP_WRITE – Generate rio_local_write_config_* functions"
---

<p>RIO_LOP_WRITE &#8211; Generate rio_local_write_config_* functions</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>RIO_LOP_WRITE(</code><i>size</i><code>, </code><i>type</i><code>, </code><i>len</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>size</i></p>
<dl>
<dd>
<dd>Size of configuration space write (8, 16, 32 bits)</dl>
<p> <i>type</i></p>
<dl>
<dd>C type of value argument</dl>
<p> <i>len</i></p>
<dl>
<dd>Length of configuration space write (1, 2, 4 bytes)</dl>
<h2>Description</h2>
<p>Generates rio_local_write_config_* functions used to access configuration space registers on the local device.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
