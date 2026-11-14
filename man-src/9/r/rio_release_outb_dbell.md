---
title: "rio_release_outb_dbell(9)"
name: "rio_release_outb_dbell"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_release_outb_dbell/"
description: "rio_release_outb_dbell – release outbound doorbell message range"
---

<p>rio_release_outb_dbell &#8211; release outbound doorbell message range</p>
<h2>Synopsis</h2>
<pre><code>int rio_release_outb_dbell(struct rio_dev *rdev, struct resource *res);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device from which to release the doorbell resource</dl>
<p> <i>res</i></p>
<dl>
<dd>Doorbell resource to be freed</dl>
<h2>Description</h2>
<p>Releases ownership of a doorbell message range. Returns 0 if the request has been satisfied.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
