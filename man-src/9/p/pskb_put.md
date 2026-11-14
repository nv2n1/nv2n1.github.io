---
title: "pskb_put(9)"
name: "pskb_put"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pskb_put/"
---

pskb_put - add data to the tail of a potentially fragmented buffer

<h2>Synopsis</h2>

<pre><code>unsigned char *pskb_put(struct sk_buff *skb, struct sk_buff *tail, int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>start of the buffer to use</dl>
 

 <i>tail</i>
<dl><dd>tail fragment of the buffer to use</dl>
 

 <i>len</i>
<dl><dd>amount of data to add</dl>

<h2>Description</h2>

This function extends the used data area of the potentially fragmented buffer. <i>tail</i> must be the last fragment of <i>skb</i> -- or <i>skb</i> itself. If this would exceed the total buffer size the kernel will panic. A pointer to the first byte of the extra data is returned.

<h2>Copyright</h2>


