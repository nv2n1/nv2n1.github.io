---
title: "netif_start_subqueue(9)"
name: "netif_start_subqueue"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netif_start_subqueue/"
---

netif_start_subqueue - allow sending packets on subqueue

<h2>Synopsis</h2>

<pre><code>void netif_start_subqueue(struct net_device *dev, u16 queue_index);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>network device</dl>
 

 <i>queue_index</i>
<dl><dd>sub queue index</dl>

<h2>Description</h2>

Start individual transmit queue of a device with multiple transmit queues.

<h2>Copyright</h2>


