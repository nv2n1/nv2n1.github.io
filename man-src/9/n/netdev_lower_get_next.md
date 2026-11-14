---
title: "netdev_lower_get_next(9)"
name: "netdev_lower_get_next"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_lower_get_next/"
---

netdev_lower_get_next - Get the next device from the lower neighbour list

<h2>Synopsis</h2>

<pre><code>void *netdev_lower_get_next(struct net_device *dev, struct list_head **iter);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>iter</i>
<dl><dd>list_head ** of the current position</dl>

<h2>Description</h2>

Gets the next netdev_adjacent from the dev's lower neighbour list, starting from iter position. The caller must hold RTNL lock or its own locking that guarantees that the neighbour lower list will remain unchanged.

<h2>Copyright</h2>


