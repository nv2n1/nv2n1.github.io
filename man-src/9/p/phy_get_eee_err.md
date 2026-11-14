---
title: "phy_get_eee_err(9)"
name: "phy_get_eee_err"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_get_eee_err/"
---

phy_get_eee_err - report the EEE wake error count

<h2>Synopsis</h2>

<pre><code>int phy_get_eee_err(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>

<h2>Description</h2>

it is to report the number of time where the PHY failed to complete its normal wake sequence.

<h2>Copyright</h2>


