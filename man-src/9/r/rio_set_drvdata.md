---
title: "rio_set_drvdata(9)"
name: "rio_set_drvdata"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_set_drvdata/"
description: "rio_set_drvdata – Set RIO driver specific data"
---

<p>rio_set_drvdata &#8211; Set RIO driver specific data</p>
<h2>Synopsis</h2>
<pre><code>void rio_set_drvdata(struct rio_dev *rdev, void *data);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device</dl>
<p> <i>data</i></p>
<dl>
<dd>Pointer to driver specific data</dl>
<h2>Description</h2>
<p>Set RIO driver specific data. device struct driver data pointer is set to the <i>data</i> argument.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
