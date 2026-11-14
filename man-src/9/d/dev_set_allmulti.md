---
title: "dev_set_allmulti(9)"
name: "dev_set_allmulti"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_set_allmulti/"
---

dev_set_allmulti - update allmulti count on a device

<h2>Synopsis</h2>

<pre><code>int dev_set_allmulti(struct net_device *dev, int inc);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>inc</i>
<dl><dd>modifier</dl>

<h2>Description</h2>

Add or remove reception of all multicast frames to a device. While the count in the device remains above zero the interface remains listening to all interfaces. Once it hits zero the device reverts back to normal filtering operation. A negative <i>inc</i> value is used to drop the counter when releasing a resource needing all multicasts. Return 0 if successful or a negative errno code on error.

<h2>Copyright</h2>


