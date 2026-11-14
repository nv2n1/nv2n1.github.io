---
title: "z8530_shutdown(9)"
name: "z8530_shutdown"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_shutdown/"
description: "z8530_shutdown – Shutdown a Z8530 device"
---

<p>z8530_shutdown &#8211; Shutdown a Z8530 device</p>
<h2>Synopsis</h2>
<pre><code>int z8530_shutdown(struct z8530_dev *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>The Z8530 chip to shutdown</dl>
<h2>Description</h2>
<p>We set the interrupt handlers to silence any interrupts. We then reset the chip and wait 100uS to be sure the reset completed. Just in case the caller then tries to do stuff. </p>
<p> This is called without the lock held</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
