---
title: "devm_mdiobus_free(9)"
name: "devm_mdiobus_free"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_mdiobus_free/"
description: "devm_mdiobus_free – Resource-managed mdiobus_free"
---

<p>devm_mdiobus_free &#8211; Resource-managed <code>mdiobus_free</code></p>
<h2>Synopsis</h2>
<pre><code>void devm_mdiobus_free(struct device *dev, struct mii_bus *bus);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device this mii_bus belongs to</dl>
<p> <i>bus</i></p>
<dl>
<dd>the mii_bus associated with the device</dl>
<h2>Description</h2>
<p>Free mii_bus allocated with <code>devm_mdiobus_alloc_size</code>.</p>
<h2>Copyright</h2>
