---
title: "phy_detach(9)"
name: "phy_detach"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_detach/"
description: "phy_detach – detach a PHY device from its network device"
---

<p>phy_detach &#8211; detach a PHY device from its network device</p>
<h2>Synopsis</h2>
<pre><code>void phy_detach(struct phy_device *phydev);</code></pre>
<h2>Arguments</h2>
<p><i>phydev</i></p>
<dl>
<dd>
<dd>target phy_device struct</dl>
<h2>Description</h2>
<p>This detaches the phy device from its network device and the phy driver, and drops the reference count taken in <code>phy_attach_direct</code>.</p>
<h2>Copyright</h2>
