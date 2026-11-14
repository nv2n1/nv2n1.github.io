---
title: "fsl_local_config_write(9)"
name: "fsl_local_config_write"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fsl_local_config_write/"
description: "fsl_local_config_write – Generate a MPC85xx local config space write"
---

<p>fsl_local_config_write &#8211; Generate a MPC85xx local config space write</p>
<h2>Synopsis</h2>
<pre><code>int fsl_local_config_write(struct rio_mport *mport, int index, u32 offset, int len, u32 data);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>RapidIO master port info</dl>
<p> <i>index</i></p>
<dl>
<dd>ID of RapdiIO interface</dl>
<p> <i>offset</i></p>
<dl>
<dd>Offset into configuration space</dl>
<p> <i>len</i></p>
<dl>
<dd>Length (in bytes) of the maintenance transaction</dl>
<p> <i>data</i></p>
<dl>
<dd>Value to be written</dl>
<h2>Description</h2>
<p>Generates a MPC85xx local configuration space write. Returns <code>0</code> on success or <code>-EINVAL</code> on failure.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
