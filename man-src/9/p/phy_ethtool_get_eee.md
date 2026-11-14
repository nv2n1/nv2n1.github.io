---
title: "phy_ethtool_get_eee(9)"
name: "phy_ethtool_get_eee"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_ethtool_get_eee/"
---

phy_ethtool_get_eee - get EEE supported and status

<h2>Synopsis</h2>

<pre><code>int phy_ethtool_get_eee(struct phy_device *phydev, struct ethtool_eee *data);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>
 

 <i>data</i>
<dl><dd>ethtool_eee data</dl>

<h2>Description</h2>

it reportes the Supported/Advertisement/LP Advertisement capabilities.

<h2>Copyright</h2>


