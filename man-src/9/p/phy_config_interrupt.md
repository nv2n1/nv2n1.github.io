---
title: "phy_config_interrupt(9)"
name: "phy_config_interrupt"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_config_interrupt/"
---

phy_config_interrupt - configure the PHY device for the requested interrupts

<h2>Synopsis</h2>

<pre><code>int phy_config_interrupt(struct phy_device *phydev, u32 interrupts);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>the phy_device struct</dl>
 

 <i>interrupts</i>
<dl><dd>interrupt flags to configure for this <i>phydev</i></dl>

<h2>Description</h2>

Returns 0 on success or &lt; 0 on error.

<h2>Copyright</h2>


