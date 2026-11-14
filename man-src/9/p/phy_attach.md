---
title: "phy_attach(9)"
name: "phy_attach"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_attach/"
description: "phy_attach – attach a network device to a particular PHY device"
---

<p>phy_attach &#8211; attach a network device to a particular PHY device</p>
<h2>Synopsis</h2>
<pre><code>struct phy_device *phy_attach(struct net_device *dev, const char *bus_id, phy_interface_t interface);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>network device to attach</dl>
<p> <i>bus_id</i></p>
<dl>
<dd>Bus ID of PHY device to attach</dl>
<p> <i>interface</i></p>
<dl>
<dd>PHY device&#8217;s interface</dl>
<h2>Description</h2>
<p>Same as <code>phy_attach_direct</code> except that a PHY bus_id string is passed instead of a pointer to a struct phy_device.</p>
<h2>Copyright</h2>
