---
title: "rio_device_probe(9)"
name: "rio_device_probe"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_device_probe/"
description: "rio_device_probe – Tell if a RIO device structure has a matching RIO device id structure"
---

<p>rio_device_probe &#8211; Tell if a RIO device structure has a matching RIO device id structure</p>
<h2>Synopsis</h2>
<pre><code>int rio_device_probe(struct device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the RIO device structure to match against</dl>
<h2>Description</h2>
<p>return 0 and set rio_dev-&gt;driver when drv claims rio_dev, else error</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
