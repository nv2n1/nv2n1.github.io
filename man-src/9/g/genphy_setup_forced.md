---
title: "genphy_setup_forced(9)"
name: "genphy_setup_forced"
section: "9"
letter: "g"
url: "/docs/linux/man/9-genphy_setup_forced/"
description: "genphy_setup_forced – configures/forces speed/duplex from phydev"
---

<p>genphy_setup_forced &#8211; configures/forces speed/duplex from <i>phydev</i></p>
<h2>Synopsis</h2>
<pre><code>int genphy_setup_forced(struct phy_device *phydev);</code></pre>
<h2>Arguments</h2>
<p><i>phydev</i></p>
<dl>
<dd>
<dd>target phy_device struct</dl>
<h2>Description</h2>
<p>Configures MII_BMCR to force speed/duplex to the values in phydev. Assumes that the values are valid. Please see <code>phy_sanitize_settings</code>.</p>
<h2>Copyright</h2>
