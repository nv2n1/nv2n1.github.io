---
title: "rio_register_driver(9)"
name: "rio_register_driver"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_register_driver/"
description: "rio_register_driver – register a new RIO driver"
---

<p>rio_register_driver &#8211; register a new RIO driver</p>
<h2>Synopsis</h2>
<pre><code>int rio_register_driver(struct rio_driver *rdrv);</code></pre>
<h2>Arguments</h2>
<p><i>rdrv</i></p>
<dl>
<dd>
<dd>the RIO driver structure to register</dl>
<h2>Description</h2>
<p>Adds a struct rio_driver to the list of registered drivers. Returns a negative value on error, otherwise 0. If no error occurred, the driver remains registered even if no device was claimed during registration.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
