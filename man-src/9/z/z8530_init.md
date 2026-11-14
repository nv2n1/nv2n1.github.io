---
title: "z8530_init(9)"
name: "z8530_init"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_init/"
description: "z8530_init – Initialise a Z8530 device"
---

<p>z8530_init &#8211; Initialise a Z8530 device</p>
<h2>Synopsis</h2>
<pre><code>int z8530_init(struct z8530_dev *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Z8530 device to initialise.</dl>
<h2>Description</h2>
<p>Configure up a Z8530/Z85C30 or Z85230 chip. We check the device is present, identify the type and then program it to hopefully keep quite and behave. This matters a lot, a Z8530 in the wrong state will sometimes get into stupid modes generating 10Khz interrupt streams and the like. </p>
<p> We set the interrupt handler up to discard any events, in case we get them during reset or setp. </p>
<p> Return 0 for success, or a negative value indicating the problem in errno form.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
