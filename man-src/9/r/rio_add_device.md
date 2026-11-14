---
title: "rio_add_device(9)"
name: "rio_add_device"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_add_device/"
description: "rio_add_device – Adds a RIO device to the device model"
---

<p>rio_add_device &#8211; Adds a RIO device to the device model</p>
<h2>Synopsis</h2>
<pre><code>int rio_add_device(struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device</dl>
<h2>Description</h2>
<p>Adds the RIO device to the global device list and adds the RIO device to the RIO device list. Creates the generic sysfs nodes for an RIO device.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
