---
title: "devm_mdiobus_alloc_size(9)"
name: "devm_mdiobus_alloc_size"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_mdiobus_alloc_size/"
description: "devm_mdiobus_alloc_size – Resource-managed mdiobus_alloc_size"
---

<p>devm_mdiobus_alloc_size &#8211; Resource-managed <code>mdiobus_alloc_size</code></p>
<h2>Synopsis</h2>
<pre><code>struct mii_bus *devm_mdiobus_alloc_size(struct device *dev, int sizeof_priv);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to allocate mii_bus for</dl>
<p> <i>sizeof_priv</i></p>
<dl>
<dd>Space to allocate for private structure.</dl>
<h2>Description</h2>
<p>Managed mdiobus_alloc_size. mii_bus allocated with this function is automatically freed on driver detach. </p>
<p> If an mii_bus allocated with this function needs to be freed separately, <code>devm_mdiobus_free</code> must be used.</p>
<h2>Return</h2>
<p>Pointer to allocated mii_bus on success, NULL on failure.</p>
<h2>Copyright</h2>
