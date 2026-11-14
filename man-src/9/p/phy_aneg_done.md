---
title: "phy_aneg_done(9)"
name: "phy_aneg_done"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_aneg_done/"
---

phy_aneg_done - return auto-negotiation status

<h2>Synopsis</h2>

<pre><code>int phy_aneg_done(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>

<h2>Description</h2>

Return the auto-negotiation status from this <i>phydev</i> Returns &gt; 0 on success or &lt; 0 on error. 0 means that auto-negotiation is still pending.

<h2>Copyright</h2>


