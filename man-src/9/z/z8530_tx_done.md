---
title: "z8530_tx_done(9)"
name: "z8530_tx_done"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_tx_done/"
description: "z8530_tx_done – TX complete callback"
---

<p>z8530_tx_done &#8211; TX complete callback</p>
<h2>Synopsis</h2>
<pre><code>void z8530_tx_done(struct z8530_channel *c);</code></pre>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>The channel that completed a transmit.</dl>
<h2>Description</h2>
<p>This is called when we complete a packet send. We wake the queue, start the next packet going and then free the buffer of the existing packet. This code is fairly timing sensitive. </p>
<p> Called with the register lock held.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
