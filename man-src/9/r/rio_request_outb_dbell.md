---
title: "rio_request_outb_dbell(9)"
name: "rio_request_outb_dbell"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_request_outb_dbell/"
description: "rio_request_outb_dbell – request outbound doorbell message range"
---

<p>rio_request_outb_dbell &#8211; request outbound doorbell message range</p>
<h2>Synopsis</h2>
<pre><code>struct resource *rio_request_outb_dbell(struct rio_dev *rdev, u16 start, u16 end);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device from which to allocate the doorbell resource</dl>
<p> <i>start</i></p>
<dl>
<dd>Doorbell message range start</dl>
<p> <i>end</i></p>
<dl>
<dd>Doorbell message range end</dl>
<h2>Description</h2>
<p>Requests ownership of a doorbell message range. Returns a resource if the request has been satisfied or <code>NULL</code> on failure.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
