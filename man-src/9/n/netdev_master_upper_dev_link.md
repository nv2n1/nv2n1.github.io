---
title: "netdev_master_upper_dev_link(9)"
name: "netdev_master_upper_dev_link"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_master_upper_dev_link/"
---

netdev_master_upper_dev_link - Add a master link to the upper device

<h2>Synopsis</h2>

<pre><code>int netdev_master_upper_dev_link(struct net_device *dev, struct net_device *upper_dev, void *upper_priv, void *upper_info);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>upper_dev</i>
<dl><dd>new upper device</dl>
 

 <i>upper_priv</i>
<dl><dd>upper device private</dl>
 

 <i>upper_info</i>
<dl><dd>upper info to be passed down via notifier</dl>

<h2>Description</h2>

Adds a link to device which is upper to this one. In this case, only one master upper device can be linked, although other non-master devices might be linked as well. The caller must hold the RTNL lock. On a failure a negative errno code is returned. On success the reference counts are adjusted and the function returns zero.

<h2>Copyright</h2>


