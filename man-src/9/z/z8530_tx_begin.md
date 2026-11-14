---
title: "z8530_tx_begin(9)"
name: "z8530_tx_begin"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_tx_begin/"
description: "z8530_tx_begin – Begin packet transmission"
---

<p>z8530_tx_begin &#8211; Begin packet transmission</p>
<h2>Synopsis</h2>
<pre><code>void z8530_tx_begin(struct z8530_channel *c);</code></pre>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>The Z8530 channel to kick</dl>
<h2>Description</h2>
<p>This is the speed sensitive side of transmission. If we are called and no buffer is being transmitted we commence the next buffer. If nothing is queued we idle the sync.</p>
<h2>Note</h2>
<p>We are handling this code path in the interrupt path, keep it fast or bad things will happen. </p>
<p> Called with the lock held.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
