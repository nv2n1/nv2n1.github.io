---
title: "dev_set_promiscuity(9)"
name: "dev_set_promiscuity"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_set_promiscuity/"
---

dev_set_promiscuity - update promiscuity count on a device

<h2>Synopsis</h2>

<pre><code>int dev_set_promiscuity(struct net_device *dev, int inc);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>inc</i>
<dl><dd>modifier</dl>

<h2>Description</h2>

Add or remove promiscuity from a device. While the count in the device remains above zero the interface remains promiscuous. Once it hits zero the device reverts back to normal filtering operation. A negative inc value is used to drop promiscuity on the device. Return 0 if successful or a negative errno code on error.

<h2>Copyright</h2>


