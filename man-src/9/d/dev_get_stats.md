---
title: "dev_get_stats(9)"
name: "dev_get_stats"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_get_stats/"
---

dev_get_stats - get network device statistics

<h2>Synopsis</h2>

<pre><code>struct rtnl_link_stats64 *dev_get_stats(struct net_device *dev, struct rtnl_link_stats64 *storage);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device to get statistics from</dl>
 

 <i>storage</i>
<dl><dd>place to store stats</dl>

<h2>Description</h2>

Get network statistics from device. Return <i>storage</i>. The device driver may provide its own method by setting dev-&gt;netdev_ops-&gt;get_stats64 or dev-&gt;netdev_ops-&gt;get_stats; otherwise the internal statistics structure is used.

<h2>Copyright</h2>


