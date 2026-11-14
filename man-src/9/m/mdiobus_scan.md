---
title: "mdiobus_scan(9)"
name: "mdiobus_scan"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mdiobus_scan/"
---

mdiobus_scan - scan a bus for MDIO devices.

<h2>Synopsis</h2>

<pre><code>struct phy_device *mdiobus_scan(struct mii_bus *bus, int addr);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>mii_bus to scan</dl>
 

 <i>addr</i>
<dl><dd>address on bus to scan</dl>

<h2>Description</h2>

This function scans the MDIO bus, looking for devices which can be identified using a vendor/product ID in registers 2 and 3. Not all MDIO devices have such registers, but PHY devices typically do. Hence this function assumes anything found is a PHY, or can be treated as a PHY. Other MDIO devices, such as switches, will probably not be found during the scan.

<h2>Copyright</h2>


