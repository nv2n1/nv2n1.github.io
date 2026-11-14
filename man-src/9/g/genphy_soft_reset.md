---
title: "genphy_soft_reset(9)"
name: "genphy_soft_reset"
section: "9"
letter: "g"
url: "/docs/linux/man/9-genphy_soft_reset/"
---

genphy_soft_reset - software reset the PHY via BMCR_RESET bit

<h2>Synopsis</h2>

<pre><code>int genphy_soft_reset(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>

<h2>Description</h2>

Perform a software PHY reset using the standard BMCR_RESET bit and poll for the reset bit to be cleared.

<h2>Return</h2>

0 on success, &lt; 0 on failure

<h2>Copyright</h2>


