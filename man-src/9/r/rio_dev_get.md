---
title: "rio_dev_get(9)"
name: "rio_dev_get"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_dev_get/"
description: "rio_dev_get – Increments the reference count of the RIO device structure"
---

<p>rio_dev_get &#8211; Increments the reference count of the RIO device structure</p>
<h2>Synopsis</h2>
<pre><code>struct rio_dev *rio_dev_get(struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device being referenced</dl>
<h2>Description</h2>
<p>Each live reference to a device should be refcounted. </p>
<p> Drivers for RIO devices should normally record such references in their <code>probe</code> methods, when they bind to a device, and release them by calling <code>rio_dev_put</code>, in their <code>disconnect</code> methods.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
