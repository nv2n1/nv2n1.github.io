---
title: "z8530_status_clear(9)"
name: "z8530_status_clear"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_status_clear/"
description: "z8530_status_clear – Handle status events from a stopped chip"
---

<p>z8530_status_clear &#8211; Handle status events from a stopped chip</p>
<h2>Synopsis</h2>
<pre><code>void z8530_status_clear(struct z8530_channel *chan);</code></pre>
<h2>Arguments</h2>
<p><i>chan</i></p>
<dl>
<dd>
<dd>Z8530 channel to shut up</dl>
<h2>Description</h2>
<p>Status interrupt vectors for a Z8530 that is in &#8216;parked&#8217; mode. For machines with PCI Z85x30 cards, or level triggered interrupts (eg the MacII) we must clear the interrupt cause or die.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
