---
title: "z8530_status(9)"
name: "z8530_status"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_status/"
description: "z8530_status – Handle a PIO status exception"
---

<p>z8530_status &#8211; Handle a PIO status exception</p>
<h2>Synopsis</h2>
<pre><code>void z8530_status(struct z8530_channel *chan);</code></pre>
<h2>Arguments</h2>
<p><i>chan</i></p>
<dl>
<dd>
<dd>Z8530 channel to process</dl>
<h2>Description</h2>
<p>A status event occurred in PIO synchronous mode. There are several reasons the chip will bother us here. A transmit underrun means we failed to feed the chip fast enough and just broke a packet. A DCD change is a line up or down.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
