---
title: "netdev_update_features(9)"
name: "netdev_update_features"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_update_features/"
---

netdev_update_features - recalculate device features

<h2>Synopsis</h2>

<pre><code>void netdev_update_features(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the device to check</dl>

<h2>Description</h2>

Recalculate dev-&gt;features set and send notifications if it has changed. Should be called after driver or hardware dependent conditions might have changed that influence the features.

<h2>Copyright</h2>


