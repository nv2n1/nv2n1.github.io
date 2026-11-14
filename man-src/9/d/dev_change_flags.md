---
title: "dev_change_flags(9)"
name: "dev_change_flags"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_change_flags/"
---

dev_change_flags - change device settings

<h2>Synopsis</h2>

<pre><code>int dev_change_flags(struct net_device *dev, unsigned int flags);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>flags</i>
<dl><dd>device state flags</dl>

<h2>Description</h2>

Change settings on device based state flags. The flags are in the userspace exported format.

<h2>Copyright</h2>


