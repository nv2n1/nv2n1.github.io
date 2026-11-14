---
title: "get_phy_device(9)"
name: "get_phy_device"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_phy_device/"
---

get_phy_device - reads the specified PHY device and returns its <i>phy_device</i> struct

<h2>Synopsis</h2>

<pre><code>struct phy_device *get_phy_device(struct mii_bus *bus, int addr, bool is_c45);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>the target MII bus</dl>
 

 <i>addr</i>
<dl><dd>PHY address on the MII bus</dl>
 

 <i>is_c45</i>
<dl><dd>If true the PHY uses the 802.3 clause 45 protocol</dl>

<h2>Description</h2>

Reads the ID registers of the PHY at <i>addr</i> on the <i>bus</i>, then allocates and returns the phy_device to represent it.

<h2>Copyright</h2>


