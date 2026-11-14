---
title: "of_mdio_find_bus(9)"
name: "of_mdio_find_bus"
section: "9"
letter: "o"
url: "/docs/linux/man/9-of_mdio_find_bus/"
description: "of_mdio_find_bus – Given an mii_bus node, find the mii_bus."
---

<p>of_mdio_find_bus &#8211; Given an mii_bus node, find the mii_bus.</p>
<h2>Synopsis</h2>
<pre><code>struct mii_bus *of_mdio_find_bus(struct device_node *mdio_bus_np);</code></pre>
<h2>Arguments</h2>
<p><i>mdio_bus_np</i></p>
<dl>
<dd>
<dd>Pointer to the mii_bus.</dl>
<h2>Description</h2>
<p>Returns a reference to the mii_bus, or NULL if none found. The embedded struct device will have its reference count incremented, and this must be put once the bus is finished with. </p>
<p> Because the association of a device_node and mii_bus is made via <code>of_mdiobus_register</code>, the mii_bus cannot be found before it is registered with <code>of_mdiobus_register</code>.</p>
<h2>Copyright</h2>
