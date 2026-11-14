---
title: "phy_probe(9)"
name: "phy_probe"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_probe/"
---

phy_probe - probe and init a PHY device

<h2>Synopsis</h2>

<pre><code>int phy_probe(struct device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device to probe and init</dl>

<h2>Description</h2>

Take care of setting up the phy_device structure, set the state to READY (the driver's init function should set it to STARTING if needed).

<h2>Copyright</h2>


