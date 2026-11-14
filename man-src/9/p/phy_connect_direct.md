---
title: "phy_connect_direct(9)"
name: "phy_connect_direct"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_connect_direct/"
---

phy_connect_direct - connect an ethernet device to a specific phy_device

<h2>Synopsis</h2>

<pre><code>int phy_connect_direct(struct net_device *dev, struct phy_device *phydev, void (*handler)(struct net_device *), phy_interface_t interface);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the network device to connect</dl>
 

 <i>phydev</i>
<dl><dd>the pointer to the phy device</dl>
 

 <i>handler</i>
<dl><dd>callback function for state change notifications</dl>
 

 <i>interface</i>
<dl><dd>PHY device's interface</dl>

<h2>Copyright</h2>


