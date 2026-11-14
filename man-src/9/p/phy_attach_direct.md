---
title: "phy_attach_direct(9)"
name: "phy_attach_direct"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_attach_direct/"
---

phy_attach_direct - attach a network device to a given PHY device pointer

<h2>Synopsis</h2>

<pre><code>int phy_attach_direct(struct net_device *dev, struct phy_device *phydev, u32 flags, phy_interface_t interface);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>network device to attach</dl>
 

 <i>phydev</i>
<dl><dd>Pointer to phy_device to attach</dl>
 

 <i>flags</i>
<dl><dd>PHY device's dev_flags</dl>
 

 <i>interface</i>
<dl><dd>PHY device's interface</dl>

<h2>Description</h2>

Called by drivers to attach to a particular PHY device. The phy_device is found, and properly hooked up to the phy_driver. If no driver is attached, then a generic driver is used. The phy_device is given a ptr to the attaching device, and given a callback for link status change. The phy_device is returned to the attaching driver. This function takes a reference on the phy device.

<h2>Copyright</h2>


