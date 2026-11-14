---
title: "eth_change_mtu(9)"
name: "eth_change_mtu"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_change_mtu/"
---

eth_change_mtu - set new MTU size

<h2>Synopsis</h2>

<pre><code>int eth_change_mtu(struct net_device *dev, int new_mtu);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>network device</dl>
 

 <i>new_mtu</i>
<dl><dd>new Maximum Transfer Unit</dl>

<h2>Description</h2>

Allow changing MTU size. Needs to be overridden for devices supporting jumbo frames.

<h2>Copyright</h2>


