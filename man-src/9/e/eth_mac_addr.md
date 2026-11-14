---
title: "eth_mac_addr(9)"
name: "eth_mac_addr"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_mac_addr/"
---

eth_mac_addr - set new Ethernet hardware address

<h2>Synopsis</h2>

<pre><code>int eth_mac_addr(struct net_device *dev, void *p);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>network device</dl>
 

 <i>p</i>
<dl><dd>socket address</dl>

<h2>Description</h2>

Change hardware address of device. 

 This doesn't change hardware matching, so needs to be overridden for most real devices.

<h2>Copyright</h2>


