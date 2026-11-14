---
title: "netif_set_real_num_rx_queues(9)"
name: "netif_set_real_num_rx_queues"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_set_real_num_rx_queues/"
---

netif_set_real_num_rx_queues - set actual number of RX queues used

<h2>Synopsis</h2>

<pre><code>int netif_set_real_num_rx_queues(struct net_device *dev, unsigned int rxq);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>Network device</dl>
 

 <i>rxq</i>
<dl><dd>Actual number of RX queues</dl>

<h2>Description</h2>

This must be called either with the rtnl_lock held or before registration of the net device. Returns 0 on success, or a negative error code. If called before registration, it always succeeds.

<h2>Copyright</h2>


