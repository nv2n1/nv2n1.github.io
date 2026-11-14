---
title: "netdev_increment_features(9)"
name: "netdev_increment_features"
section: "9"
letter: "n"
url: "/docs/linux/man/9-netdev_increment_features/"
description: "netdev_increment_features – increment feature set by one"
---

<p>netdev_increment_features &#8211; increment feature set by one</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>netdev_features_t netdev_increment_features(netdev_features_t&nbsp;<wbr></code><i>all</i><code>, netdev_features_t&nbsp;<wbr></code><i>one</i><code>, netdev_features_t&nbsp;<wbr></code><i>mask</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>all</i></p>
<dl>
<dd>
<dd>current feature set</dl>
<p> <i>one</i></p>
<dl>
<dd>new feature set</dl>
<p> <i>mask</i></p>
<dl>
<dd>mask feature set</dl>
<h2>Description</h2>
<p>Computes a new feature set after adding a device with feature set <i>one</i> to the master device with current feature set <i>all</i>. Will not enable anything that is off in <i>mask</i>. Returns the new feature set.</p>
<h2>Copyright</h2>
