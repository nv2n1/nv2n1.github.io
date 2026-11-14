---
title: "phy_connect(9)"
name: "phy_connect"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_connect/"
---

phy_connect - connect an ethernet device to a PHY device

<h2>Synopsis</h2>

<pre><code>struct phy_device *phy_connect(struct net_device *dev, const char *bus_id, void (*handler)(struct net_device *), phy_interface_t interface);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the network device to connect</dl>
 

 <i>bus_id</i>
<dl><dd>the id string of the PHY device to connect</dl>
 

 <i>handler</i>
<dl><dd>callback function for state change notifications</dl>
 

 <i>interface</i>
<dl><dd>PHY device's interface</dl>

<h2>Description</h2>

Convenience function for connecting ethernet devices to PHY devices. The default behavior is for the PHY infrastructure to handle everything, and only notify the connected driver when the link status changes. If you don't want, or can't use the provided functionality, you may choose to call only the subset of functions which provide the desired functionality.

<h2>Copyright</h2>


