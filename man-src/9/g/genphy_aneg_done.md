---
title: "genphy_aneg_done(9)"
name: "genphy_aneg_done"
section: "9"
letter: "g"
url: "/docs/linux/man/9-genphy_aneg_done/"
---

genphy_aneg_done - return auto-negotiation status

<h2>Synopsis</h2>

<pre><code>int genphy_aneg_done(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>

<h2>Description</h2>

Reads the status register and returns 0 either if auto-negotiation is incomplete, or if there was an error. Returns BMSR_ANEGCOMPLETE if auto-negotiation is done.

<h2>Copyright</h2>


