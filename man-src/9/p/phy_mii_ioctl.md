---
title: "phy_mii_ioctl(9)"
name: "phy_mii_ioctl"
section: "9"
letter: "p"
url: "/docs/linux/man/9-phy_mii_ioctl/"
---

phy_mii_ioctl - generic PHY MII ioctl interface

<h2>Synopsis</h2>

<pre><code>int phy_mii_ioctl(struct phy_device *phydev, struct ifreq *ifr, int cmd);</code></pre>

<h2>Arguments</h2>

<i>phydev</i>
<dl><dd><dd>the phy_device struct</dl>
 

 <i>ifr</i>
<dl><dd>struct ifreq for socket ioctl's</dl>
 

 <i>cmd</i>
<dl><dd>ioctl cmd to execute</dl>

<h2>Description</h2>

Note that this function is currently incompatible with the PHYCONTROL layer. It changes registers without regard to current state. Use at own risk.

<h2>Copyright</h2>


