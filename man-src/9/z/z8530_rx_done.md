---
title: "z8530_rx_done(9)"
name: "z8530_rx_done"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_rx_done/"
description: "z8530_rx_done – Receive completion callback"
---

<p>z8530_rx_done &#8211; Receive completion callback</p>
<h2>Synopsis</h2>
<pre><code>void z8530_rx_done(struct z8530_channel *c);</code></pre>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>The channel that completed a receive</dl>
<h2>Description</h2>
<p>A new packet is complete. Our goal here is to get back into receive mode as fast as possible. On the Z85230 we could change to using ESCC mode, but on the older chips we have no choice. We flip to the new buffer immediately in DMA mode so that the DMA of the next frame can occur while we are copying the previous buffer to an sk_buff </p>
<p> Called with the lock held</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
