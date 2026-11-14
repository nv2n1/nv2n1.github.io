---
title: "phy_start(9)"
name: "phy_start"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_start/"
description: "phy_start – start or restart a PHY device"
---

<p>phy_start &#8211; start or restart a PHY device</p>
<h2>Synopsis</h2>
<pre><code>void phy_start(struct phy_device *phydev);</code></pre>
<h2>Arguments</h2>
<p><i>phydev</i></p>
<dl>
<dd>
<dd>target phy_device struct</dl>
<h2>Description</h2>
<p>Indicates the attached device&#8217;s readiness to handle PHY-related work. Used during startup to start the PHY, and after a call to <code>phy_stop</code> to resume operation. Also used to indicate the MDIO bus has cleared an error condition.</p>
<h2>Copyright</h2>
