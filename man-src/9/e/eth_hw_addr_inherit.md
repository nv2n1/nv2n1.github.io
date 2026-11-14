---
title: "eth_hw_addr_inherit(9)"
name: "eth_hw_addr_inherit"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_hw_addr_inherit/"
---

eth_hw_addr_inherit - Copy dev_addr from another net_device

<h2>Synopsis</h2>

<pre><code>void eth_hw_addr_inherit(struct net_device *dst, struct net_device *src);</code></pre>

<h2>Arguments</h2>

<i>dst</i>
<dl><dd><dd>pointer to net_device to copy dev_addr to</dl>
 

 <i>src</i>
<dl><dd>pointer to net_device to copy dev_addr from</dl>

<h2>Description</h2>

Copy the Ethernet address from one net_device to another along with the address attributes (addr_assign_type).

<h2>Copyright</h2>


