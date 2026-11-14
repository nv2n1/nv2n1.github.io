---
title: "phy_device_remove(9)"
name: "phy_device_remove"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_device_remove/"
description: "phy_device_remove – Remove a previously registered phy device from the MDIO bus"
---

<p>phy_device_remove &#8211; Remove a previously registered phy device from the MDIO bus</p>
<h2>Synopsis</h2>
<pre><code>void phy_device_remove(struct phy_device *phydev);</code></pre>
<h2>Arguments</h2>
<p><i>phydev</i></p>
<dl>
<dd>
<dd>phy_device structure to remove</dl>
<h2>Description</h2>
<p>This doesn&#8217;t free the phy_device itself, it merely reverses the effects of <code>phy_device_register</code>. Use <code>phy_device_free</code> to free the device after calling this function.</p>
<h2>Copyright</h2>
