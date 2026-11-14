---
title: "skb_pad(9)"
name: "skb_pad"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_pad/"
---

skb_pad - zero pad the tail of an skb

<h2>Synopsis</h2>

<pre><code>int skb_pad(struct sk_buff *skb, int pad);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to pad</dl>
 

 <i>pad</i>
<dl><dd>space to pad</dl>

<h2>Description</h2>

Ensure that a buffer is followed by a padding area that is zero filled. Used by network drivers which may DMA or transfer data beyond the buffer end onto the wire. 

 May return error in out of memory cases. The skb is freed on error.

<h2>Copyright</h2>


