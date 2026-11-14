---
title: "rio_chk_dev_route(9)"
name: "rio_chk_dev_route"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_chk_dev_route/"
description: "rio_chk_dev_route – Validate route to the specified device."
---

<p>rio_chk_dev_route &#8211; Validate route to the specified device.</p>
<h2>Synopsis</h2>
<pre><code>int rio_chk_dev_route(struct rio_dev *rdev, struct rio_dev **nrdev, int *npnum);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device failed to respond</dl>
<p> <i>nrdev</i></p>
<dl>
<dd>Last active device on the route to rdev</dl>
<p> <i>npnum</i></p>
<dl>
<dd>nrdev&#8217;s port number on the route to rdev</dl>
<h2>Description</h2>
<p>Follows a route to the specified RIO device to determine the last available device (and corresponding RIO port) on the route.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
