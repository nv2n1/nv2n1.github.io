---
title: "rio_sport_is_active(9)"
name: "rio_sport_is_active"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_sport_is_active/"
description: "rio_sport_is_active – Tests if a switch port has an active connection."
---

<p>rio_sport_is_active &#8211; Tests if a switch port has an active connection.</p>
<h2>Synopsis</h2>
<pre><code>int rio_sport_is_active(struct rio_dev *rdev, int sp);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RapidIO device object</dl>
<p> <i>sp</i></p>
<dl>
<dd>Switch port number</dl>
<h2>Description</h2>
<p>Reads the port error status CSR for a particular switch port to determine if the port has an active link. Returns <code>RIO_PORT_N_ERR_STS_PORT_OK</code> if the port is active or <code>0</code> if it is inactive.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
