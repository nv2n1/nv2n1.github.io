---
title: "netdev_lower_get_first_private_rcu(9)"
name: "netdev_lower_get_first_private_rcu"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_lower_get_first_private_rcu/"
---

netdev_lower_get_first_private_rcu - Get the first -&gt;private from the lower neighbour list, RCU variant

<h2>Synopsis</h2>

<pre><code>void *netdev_lower_get_first_private_rcu(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>

<h2>Description</h2>

Gets the first netdev_adjacent-&gt;private from the dev's lower neighbour list. The caller must hold RCU read lock.

<h2>Copyright</h2>


