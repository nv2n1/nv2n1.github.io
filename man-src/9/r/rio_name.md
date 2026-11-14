---
title: "rio_name(9)"
name: "rio_name"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_name/"
description: "rio_name – Get the unique RIO device identifier"
---

<p>rio_name &#8211; Get the unique RIO device identifier</p>
<h2>Synopsis</h2>
<pre><code>const char *rio_name(struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device</dl>
<h2>Description</h2>
<p>Get the unique RIO device identifier. Returns the device identifier string.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
