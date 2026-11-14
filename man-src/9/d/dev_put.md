---
title: "dev_put(9)"
name: "dev_put"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_put/"
---

dev_put - release reference to device

<h2>Synopsis</h2>

<pre><code>void dev_put(struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>network device</dl>

<h2>Description</h2>

Release reference to device to allow it to be freed.

<h2>Copyright</h2>


