---
title: "phy_sanitize_settings(9)"
name: "phy_sanitize_settings"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_sanitize_settings/"
---

phy_sanitize_settings - make sure the PHY is set to supported speed and duplex

<h2>Synopsis</h2>

<pre><code>void phy_sanitize_settings(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>the target phy_device struct</dl>

<h2>Description</h2>

Make sure the PHY is set to supported speeds and duplexes. Drop down by one in this order: 1000/FULL, 1000/HALF, 100/FULL, 100/HALF, 10/FULL, 10/HALF.

<h2>Copyright</h2>


