---
title: "netdev_change_features(9)"
name: "netdev_change_features"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_change_features/"
description: "netdev_change_features – recalculate device features"
---

<p>netdev_change_features &#8211; recalculate device features</p>
<h2>Synopsis</h2>
<pre><code>void netdev_change_features(struct net_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device to check</dl>
<h2>Description</h2>
<p>Recalculate dev-&gt;features set and send notifications even if they have not changed. Should be called instead of <code>netdev_update_features</code> if also dev-&gt;vlan_features might have changed to allow the changes to be propagated to stacked VLAN devices.</p>
<h2>Copyright</h2>
