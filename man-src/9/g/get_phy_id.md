---
title: "get_phy_id(9)"
name: "get_phy_id"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_phy_id/"
description: "get_phy_id – reads the specified addr for its ID."
---

<p>get_phy_id &#8211; reads the specified addr for its ID.</p>
<h2>Synopsis</h2>
<pre><code>int get_phy_id(struct mii_bus *bus, int addr, u32 *phy_id, bool is_c45, struct phy_c45_device_ids *c45_ids);</code></pre>
<h2>Arguments</h2>
<p><i>bus</i></p>
<dl>
<dd>
<dd>the target MII bus</dl>
<p> <i>addr</i></p>
<dl>
<dd>PHY address on the MII bus</dl>
<p> <i>phy_id</i></p>
<dl>
<dd>where to store the ID retrieved.</dl>
<p> <i>is_c45</i></p>
<dl>
<dd>If true the PHY uses the 802.3 clause 45 protocol</dl>
<p> <i>c45_ids</i></p>
<dl>
<dd>where to store the c45 ID information.</dl>
<h2>Description</h2>
<p>In the case of a 802.3-c22 PHY, reads the ID registers of the PHY at <i>addr</i> on the <i>bus</i>, stores it in <i>phy_id</i> and returns zero on success. </p>
<p> In the case of a 802.3-c45 PHY, <code>get_phy_c45_ids</code> is invoked, and its return value is in turn returned.</p>
<h2>Copyright</h2>
