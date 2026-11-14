---
title: "netdev_rx_handler_register(9)"
name: "netdev_rx_handler_register"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_rx_handler_register/"
---

netdev_rx_handler_register - register receive handler

<h2>Synopsis</h2>

<pre><code>int netdev_rx_handler_register(struct net_device *dev, rx_handler_func_t *rx_handler, void *rx_handler_data);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device to register a handler for</dl>
 

 <i>rx_handler</i>
<dl><dd>receive handler to register</dl>
 

 <i>rx_handler_data</i>
<dl><dd>data pointer that is used by rx handler</dl>

<h2>Description</h2>

Register a receive handler for a device. This handler will then be called from __netif_receive_skb. A negative errno code is returned on a failure. 

 The caller must hold the rtnl_mutex. 

 For a general description of rx_handler, see enum rx_handler_result.

<h2>Copyright</h2>


