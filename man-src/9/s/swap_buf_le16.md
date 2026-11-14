---
title: "swap_buf_le16(9)"
name: "swap_buf_le16"
section: "9"
letter: "s"
url: "/docs/linux/man/9-swap_buf_le16/"
description: "swap_buf_le16 – swap halves of 16-bit words in place"
---

<p>swap_buf_le16 &#8211; swap halves of 16-bit words in place</p>
<h2>Synopsis</h2>
<pre><code>void swap_buf_le16(u16 *buf, unsigned int buf_words);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>Buffer to swap</dl>
<p> <i>buf_words</i></p>
<dl>
<dd>Number of 16-bit words in buffer.</dl>
<h2>Description</h2>
<p>Swap halves of 16-bit words if needed to convert from little-endian byte order to native cpu byte order, or vice-versa. </p>
<p> LOCKING: Inherited from caller.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
