---
title: "netdev_reset_queue(9)"
name: "netdev_reset_queue"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_reset_queue/"
---

netdev_reset_queue - reset the packets and bytes count of a network device

<h2>Synopsis</h2>

<pre><code>void netdev_reset_queue(struct net_device *dev_queue);</code></pre>

<h2>Arguments</h2>

<i>dev_queue</i>
<dl><dd><dd>network device</dl>

<h2>Description</h2>

Reset the bytes and packet count of a network device and clear the software flow control OFF bit for this network device

<h2>Copyright</h2>


