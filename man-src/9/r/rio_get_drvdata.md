---
title: "rio_get_drvdata(9)"
name: "rio_get_drvdata"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_get_drvdata/"
description: "rio_get_drvdata – Get RIO driver specific data"
---

<p>rio_get_drvdata &#8211; Get RIO driver specific data</p>
<h2>Synopsis</h2>
<pre><code>void *rio_get_drvdata(struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device</dl>
<h2>Description</h2>
<p>Get RIO driver specific data. Returns a pointer to the driver specific data.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
