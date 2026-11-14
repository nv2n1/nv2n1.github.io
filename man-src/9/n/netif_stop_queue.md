---
title: "netif_stop_queue(9)"
name: "netif_stop_queue"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_stop_queue/"
---

netif_stop_queue - stop transmitted packets

<h2>Synopsis</h2>

<pre><code>void netif_stop_queue(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>network device</dl>

<h2>Description</h2>

Stop upper layers calling the device hard_start_xmit routine. Used for flow control when transmit resources are unavailable.

<h2>Copyright</h2>


