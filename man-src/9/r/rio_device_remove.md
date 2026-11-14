---
title: "rio_device_remove(9)"
name: "rio_device_remove"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_device_remove/"
description: "rio_device_remove – Remove a RIO device from the system"
---

<p>rio_device_remove &#8211; Remove a RIO device from the system</p>
<h2>Synopsis</h2>
<pre><code>int rio_device_remove(struct device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the RIO device structure to match against</dl>
<h2>Description</h2>
<p>Remove a RIO device from the system. If it has an associated driver, then run the driver <code>remove</code> method. Then update the reference count.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
