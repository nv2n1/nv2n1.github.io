---
title: "skb_put_padto(9)"
name: "skb_put_padto"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_put_padto/"
---

skb_put_padto - increase size and pad an skbuff up to a minimal size

<h2>Synopsis</h2>

<pre><code>int skb_put_padto(struct sk_buff *skb, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to pad</dl>
 

 <i>len</i>
<dl><dd>minimal length</dl>

<h2>Description</h2>

Pads up a buffer to ensure the trailing bytes exist and are blanked. If the buffer already contains sufficient data it is untouched. Otherwise it is extended. Returns zero on success. The skb is freed on error.

<h2>Copyright</h2>


