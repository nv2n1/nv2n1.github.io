---
title: "netdev_upper_dev_link(9)"
name: "netdev_upper_dev_link"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_upper_dev_link/"
---

netdev_upper_dev_link - Add a link to the upper device

<h2>Synopsis</h2>

<pre><code>int netdev_upper_dev_link(struct net_device *dev, struct net_device *upper_dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>upper_dev</i>
<dl><dd>new upper device</dl>

<h2>Description</h2>

Adds a link to device which is upper to this one. The caller must hold the RTNL lock. On a failure a negative errno code is returned. On success the reference counts are adjusted and the function returns zero.

<h2>Copyright</h2>


