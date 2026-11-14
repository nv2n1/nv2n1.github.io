---
title: "fsl_rio_setup(9)"
name: "fsl_rio_setup"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fsl_rio_setup/"
description: "fsl_rio_setup – Setup Freescale PowerPC RapidIO interface"
---

<p>fsl_rio_setup &#8211; Setup Freescale PowerPC RapidIO interface</p>
<h2>Synopsis</h2>
<pre><code>int fsl_rio_setup(struct platform_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>platform_device pointer</dl>
<h2>Description</h2>
<p>Initializes MPC85xx RapidIO hardware interface, configures master port with system-specific info, and registers the master port with the RapidIO subsystem.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
