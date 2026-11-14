---
title: "dev_disable_lro(9)"
name: "dev_disable_lro"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_disable_lro/"
---

dev_disable_lro - disable Large Receive Offload on a device

<h2>Synopsis</h2>

<pre><code>void dev_disable_lro(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>

<h2>Description</h2>

Disable Large Receive Offload (LRO) on a net device. Must be called under RTNL. This is needed if received packets may be forwarded to another interface.

<h2>Copyright</h2>


