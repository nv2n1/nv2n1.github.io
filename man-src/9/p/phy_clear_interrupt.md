---
title: "phy_clear_interrupt(9)"
name: "phy_clear_interrupt"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_clear_interrupt/"
---

phy_clear_interrupt - Ack the phy device's interrupt

<h2>Synopsis</h2>

<pre><code>int phy_clear_interrupt(struct phy_device *phydev);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>the phy_device struct</dl>

<h2>Description</h2>

If the <i>phydev</i> driver has an ack_interrupt function, call it to ack and clear the phy device's interrupt. 

 Returns 0 on success or &lt; 0 on error.

<h2>Copyright</h2>


