---
title: "rio_release_inb_dbell(9)"
name: "rio_release_inb_dbell"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_release_inb_dbell/"
description: "rio_release_inb_dbell – release inbound doorbell message service"
---

<p>rio_release_inb_dbell &#8211; release inbound doorbell message service</p>
<h2>Synopsis</h2>
<pre><code>int rio_release_inb_dbell(struct rio_mport *mport, u16 start, u16 end);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>RIO master port from which to release the doorbell resource</dl>
<p> <i>start</i></p>
<dl>
<dd>Doorbell info range start</dl>
<p> <i>end</i></p>
<dl>
<dd>Doorbell info range end</dl>
<h2>Description</h2>
<p>Releases ownership of an inbound doorbell resource and removes callback from the doorbell event list. Returns 0 if the request has been satisfied.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
