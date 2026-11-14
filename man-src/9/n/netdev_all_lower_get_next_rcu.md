---
title: "netdev_all_lower_get_next_rcu(9)"
name: "netdev_all_lower_get_next_rcu"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_all_lower_get_next_rcu/"
---

netdev_all_lower_get_next_rcu - Get the next device from all lower neighbour list, RCU variant

<h2>Synopsis</h2>

<pre><code>struct net_device *netdev_all_lower_get_next_rcu(struct net_device *dev, struct list_head **iter);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>iter</i>
<dl><dd>list_head ** of the current position</dl>

<h2>Description</h2>

Gets the next netdev_adjacent from the dev's all lower neighbour list, starting from iter position. The caller must hold RCU read lock.

<h2>Copyright</h2>


