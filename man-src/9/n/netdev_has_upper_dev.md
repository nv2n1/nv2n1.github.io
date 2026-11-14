---
title: "netdev_has_upper_dev(9)"
name: "netdev_has_upper_dev"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_has_upper_dev/"
description: "netdev_has_upper_dev – Check if device is linked to an upper device"
---

<p>netdev_has_upper_dev &#8211; Check if device is linked to an upper device</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool netdev_has_upper_dev(struct net_device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, struct net_device&nbsp;<wbr>*&nbsp;<wbr></code><i>upper_dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device</dl>
<p> <i>upper_dev</i></p>
<dl>
<dd>upper device to check</dl>
<h2>Description</h2>
<p>Find out if a device is linked to specified upper device and return true in case it is. Note that this checks only immediate upper device, not through a complete stack of devices. The caller must hold the RTNL lock.</p>
<h2>Copyright</h2>
