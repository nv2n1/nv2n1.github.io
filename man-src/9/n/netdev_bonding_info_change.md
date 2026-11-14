---
title: "netdev_bonding_info_change(9)"
name: "netdev_bonding_info_change"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_bonding_info_change/"
---

netdev_bonding_info_change - Dispatch event about slave change

<h2>Synopsis</h2>

<pre><code>void netdev_bonding_info_change(struct net_device *dev, struct netdev_bonding_info *bonding_info);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>bonding_info</i>
<dl><dd>info to dispatch</dl>

<h2>Description</h2>

Send NETDEV_BONDING_INFO to netdev notifiers with info. The caller must hold the RTNL lock.

<h2>Copyright</h2>


