---
title: "genphy_config_aneg(9)"
name: "genphy_config_aneg"
section: "9"
letter: "g"
url: "/docs/linux/man/9-genphy_config_aneg/"
---

genphy_config_aneg - restart auto-negotiation or write BMCR

<h2>Synopsis</h2>

<pre><code>int genphy_config_aneg(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>

<h2>Description</h2>

If auto-negotiation is enabled, we configure the advertising, and then restart auto-negotiation. If it is not enabled, then we write the BMCR.

<h2>Copyright</h2>


