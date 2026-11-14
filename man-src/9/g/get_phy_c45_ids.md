---
title: "get_phy_c45_ids(9)"
name: "get_phy_c45_ids"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_phy_c45_ids/"
---

get_phy_c45_ids - reads the specified addr for its 802.3-c45 IDs.

<h2>Synopsis</h2>

<pre><code>int get_phy_c45_ids(struct mii_bus *bus, int addr, u32 *phy_id, struct phy_c45_device_ids *c45_ids);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>the target MII bus</dl>
 

 <i>addr</i>
<dl><dd>PHY address on the MII bus</dl>
 

 <i>phy_id</i>
<dl><dd>where to store the ID retrieved.</dl>
 

 <i>c45_ids</i>
<dl><dd>where to store the c45 ID information.</dl>

<h2>Description</h2>

If the PHY devices-in-package appears to be valid, it and the corresponding identifiers are stored in <i>c45_ids</i>, zero is stored in <i>phy_id</i>. Otherwise 0xffffffff is stored in <i>phy_id</i>. Returns zero on success.

<h2>Copyright</h2>


