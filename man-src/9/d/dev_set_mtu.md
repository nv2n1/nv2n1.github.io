---
title: "dev_set_mtu(9)"
name: "dev_set_mtu"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_set_mtu/"
---

dev_set_mtu - Change maximum transfer unit

<h2>Synopsis</h2>

<pre><code>int dev_set_mtu(struct net_device *dev, int new_mtu);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>new_mtu</i>
<dl><dd>new transfer unit</dl>

<h2>Description</h2>

Change the maximum transfer size of the network device.

<h2>Copyright</h2>


