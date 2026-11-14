---
title: "netif_wake_queue(9)"
name: "netif_wake_queue"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_wake_queue/"
---

netif_wake_queue - restart transmit

<h2>Synopsis</h2>

<pre><code>void netif_wake_queue(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>network device</dl>

<h2>Description</h2>

Allow upper layers to call the device hard_start_xmit routine. Used for flow control when transmit resources are available.

<h2>Copyright</h2>


