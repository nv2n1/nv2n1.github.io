---
title: "eth_hw_addr_random(9)"
name: "eth_hw_addr_random"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_hw_addr_random/"
---

eth_hw_addr_random - Generate software assigned random Ethernet and set device flag

<h2>Synopsis</h2>

<pre><code>void eth_hw_addr_random(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>pointer to net_device structure</dl>

<h2>Description</h2>

Generate a random Ethernet address (MAC) to be used by a net device and set addr_assign_type so the state can be read by sysfs and be used by userspace.

<h2>Copyright</h2>


