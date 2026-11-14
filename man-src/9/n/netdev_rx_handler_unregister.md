---
title: "netdev_rx_handler_unregister(9)"
name: "netdev_rx_handler_unregister"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_rx_handler_unregister/"
---

netdev_rx_handler_unregister - unregister receive handler

<h2>Synopsis</h2>

<pre><code>void netdev_rx_handler_unregister(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device to unregister a handler from</dl>

<h2>Description</h2>

Unregister a receive handler from a device. 

 The caller must hold the rtnl_mutex.

<h2>Copyright</h2>


