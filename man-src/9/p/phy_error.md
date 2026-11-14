---
title: "phy_error(9)"
name: "phy_error"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_error/"
---

phy_error - enter HALTED state for this PHY device

<h2>Synopsis</h2>

<pre><code>void phy_error(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>

<h2>Description</h2>

Moves the PHY to the HALTED state in response to a read or write error, and tells the controller the link is down. Must not be called from interrupt context, or while the phydev-&gt;lock is held.

<h2>Copyright</h2>


