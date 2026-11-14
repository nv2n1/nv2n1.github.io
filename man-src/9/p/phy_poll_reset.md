---
title: "phy_poll_reset(9)"
name: "phy_poll_reset"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_poll_reset/"
description: "phy_poll_reset – Safely wait until a PHY reset has properly completed"
---

<p>phy_poll_reset &#8211; Safely wait until a PHY reset has properly completed</p>
<h2>Synopsis</h2>
<pre><code>int phy_poll_reset(struct phy_device *phydev);</code></pre>
<h2>Arguments</h2>
<p><i>phydev</i></p>
<dl>
<dd>
<dd>The PHY device to poll</dl>
<h2>Description</h2>
<p>According to IEEE 802.3, Section 2, Subsection 22.2.4.1.1, as published in 2008, a PHY reset may take up to 0.5 seconds. The MII BMCR register must be polled until the BMCR_RESET bit clears. </p>
<p> Furthermore, any attempts to write to PHY registers may have no effect or even generate MDIO bus errors until this is complete. </p>
<p> Some PHYs (such as the Marvell 88E1111) don&#8217;t entirely conform to the standard and do not fully reset after the BMCR_RESET bit is set, and may even *REQUIRE* a soft-reset to properly restart autonegotiation. In an effort to support such broken PHYs, this function is separate from the standard <code>phy_init_hw</code> which will zero all the other bits in the BMCR and reapply all driver-specific and board-specific fixups.</p>
<h2>Copyright</h2>
