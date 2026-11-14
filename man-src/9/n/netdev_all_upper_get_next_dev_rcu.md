---
title: "netdev_all_upper_get_next_dev_rcu(9)"
name: "netdev_all_upper_get_next_dev_rcu"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_all_upper_get_next_dev_rcu/"
---

netdev_all_upper_get_next_dev_rcu - Get the next dev from upper list

<h2>Synopsis</h2>

<pre><code>struct net_device *netdev_all_upper_get_next_dev_rcu(struct net_device *dev, struct list_head **iter);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>iter</i>
<dl><dd>list_head ** of the current position</dl>

<h2>Description</h2>

Gets the next device from the dev's upper list, starting from iter position. The caller must hold RCU read lock.

<h2>Copyright</h2>


