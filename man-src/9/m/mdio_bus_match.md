---
title: "mdio_bus_match(9)"
name: "mdio_bus_match"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mdio_bus_match/"
---

mdio_bus_match - determine if given MDIO driver supports the given MDIO device

<h2>Synopsis</h2>

<pre><code>int mdio_bus_match(struct device *dev, struct device_driver *drv);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>target MDIO device</dl>
 

 <i>drv</i>
<dl><dd>given MDIO driver</dl>

<h2>Description</h2>

Given a MDIO device, and a MDIO driver, return 1 if the driver supports the device. Otherwise, return 0. This may require calling the devices own match function, since different classes of MDIO devices have different match criteria.

<h2>Copyright</h2>


