---
title: "z8530_flush_fifo(9)"
name: "z8530_flush_fifo"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_flush_fifo/"
description: "z8530_flush_fifo – Flush on chip RX FIFO"
---

<p>z8530_flush_fifo &#8211; Flush on chip RX FIFO</p>
<h2>Synopsis</h2>
<pre><code>void z8530_flush_fifo(struct z8530_channel *c);</code></pre>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>Channel to flush</dl>
<h2>Description</h2>
<p>Flush the receive FIFO. There is no specific option for this, we blindly read bytes and discard them. Reading when there is no data is harmless. The 8530 has a 4 byte FIFO, the 85230 has 8 bytes. </p>
<p> All locking is handled for the caller. On return data may still be present if it arrived during the flush.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
