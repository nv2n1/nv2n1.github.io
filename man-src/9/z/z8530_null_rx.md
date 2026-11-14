---
title: "z8530_null_rx(9)"
name: "z8530_null_rx"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_null_rx/"
description: "z8530_null_rx – Discard a packet"
---

<p>z8530_null_rx &#8211; Discard a packet</p>
<h2>Synopsis</h2>
<pre><code>void z8530_null_rx(struct z8530_channel *c, struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>The channel the packet arrived on</dl>
<p> <i>skb</i></p>
<dl>
<dd>The buffer</dl>
<h2>Description</h2>
<p>We point the receive handler at this function when idle. Instead of processing the frames we get to throw them away.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
