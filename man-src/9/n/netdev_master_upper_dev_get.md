---
title: "netdev_master_upper_dev_get(9)"
name: "netdev_master_upper_dev_get"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_master_upper_dev_get/"
---

netdev_master_upper_dev_get - Get master upper device

<h2>Synopsis</h2>

<pre><code>struct net_device *netdev_master_upper_dev_get(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>

<h2>Description</h2>

Find a master upper device and return pointer to it or NULL in case it's not there. The caller must hold the RTNL lock.

<h2>Copyright</h2>


