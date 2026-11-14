---
title: "phy_prepare_link(9)"
name: "phy_prepare_link"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_prepare_link/"
---

phy_prepare_link - prepares the PHY layer to monitor link status

<h2>Synopsis</h2>

<pre><code>void phy_prepare_link(struct phy_device *phydev, void (*handler)(struct net_device *));</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>target phy_device struct</dl>
 

 <i>handler</i>
<dl><dd>callback function for link status change notifications</dl>

<h2>Description</h2>

Tells the PHY infrastructure to handle the gory details on monitoring link status (whether through polling or an interrupt), and to call back to the connected device driver when the link status changes. If you want to monitor your own link state, don't call this function.

<h2>Copyright</h2>


