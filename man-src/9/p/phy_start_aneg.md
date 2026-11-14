---
title: "phy_start_aneg(9)"
name: "phy_start_aneg"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_start_aneg/"
---

phy_start_aneg - start auto-negotiation for this PHY device

<h2>Synopsis</h2>

<pre><code>int phy_start_aneg(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>the phy_device struct</dl>

<h2>Description</h2>

Sanitizes the settings (if we're not autonegotiating them), and then calls the driver's config_aneg function. If the PHYCONTROL Layer is operating, we change the state to reflect the beginning of Auto-negotiation or forcing.

<h2>Copyright</h2>


