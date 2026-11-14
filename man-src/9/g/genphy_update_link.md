---
title: "genphy_update_link(9)"
name: "genphy_update_link"
section: "9"
letter: "g"
url: "/docs/linux/man/9-genphy_update_link/"
---

genphy_update_link - update link status in <i>phydev</i>

<h2>Synopsis</h2>

<pre><code>int genphy_update_link(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>

<h2>Description</h2>

Update the value in phydev-&gt;link to reflect the current link value. In order to do this, we need to read the status register twice, keeping the second value.

<h2>Copyright</h2>


