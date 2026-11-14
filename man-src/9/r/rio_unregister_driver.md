---
title: "rio_unregister_driver(9)"
name: "rio_unregister_driver"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_unregister_driver/"
description: "rio_unregister_driver – unregister a RIO driver"
---

<p>rio_unregister_driver &#8211; unregister a RIO driver</p>
<h2>Synopsis</h2>
<pre><code>void rio_unregister_driver(struct rio_driver *rdrv);</code></pre>
<h2>Arguments</h2>
<p><i>rdrv</i></p>
<dl>
<dd>
<dd>the RIO driver structure to unregister</dl>
<h2>Description</h2>
<p>Deletes the struct rio_driver from the list of registered RIO drivers, gives it a chance to clean up by calling its <code>remove</code> function for each device it was responsible for, and marks those devices as driverless.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
