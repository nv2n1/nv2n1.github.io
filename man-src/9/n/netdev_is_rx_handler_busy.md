---
title: "netdev_is_rx_handler_busy(9)"
name: "netdev_is_rx_handler_busy"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_is_rx_handler_busy/"
description: "netdev_is_rx_handler_busy – check if receive handler is registered"
---

<p>netdev_is_rx_handler_busy &#8211; check if receive handler is registered</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool netdev_is_rx_handler_busy(struct net_device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device to check</dl>
<h2>Description</h2>
<p>Check if a receive handler is already registered for a given device. Return true if there one. </p>
<p> The caller must hold the rtnl_mutex.</p>
<h2>Copyright</h2>
