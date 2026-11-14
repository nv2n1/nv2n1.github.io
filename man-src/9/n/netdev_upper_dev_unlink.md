---
title: "netdev_upper_dev_unlink(9)"
name: "netdev_upper_dev_unlink"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_upper_dev_unlink/"
---

netdev_upper_dev_unlink - Removes a link to upper device

<h2>Synopsis</h2>

<pre><code>void netdev_upper_dev_unlink(struct net_device *dev, struct net_device *upper_dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>upper_dev</i>
<dl><dd>new upper device</dl>

<h2>Description</h2>

Removes a link to device which is upper to this one. The caller must hold the RTNL lock.

<h2>Copyright</h2>


