---
title: "phy_driver_register(9)"
name: "phy_driver_register"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_driver_register/"
---

phy_driver_register - register a phy_driver with the PHY layer

<h2>Synopsis</h2>

<pre><code>int phy_driver_register(struct phy_driver *new_driver, struct module *owner);</code></pre>

<h2>Arguments</h2>

<i>new_driver</i>
<dl><dd><dd>new phy_driver to register</dl>
 

 <i>owner</i>
<dl><dd>module owning this PHY</dl>

<h2>Copyright</h2>


