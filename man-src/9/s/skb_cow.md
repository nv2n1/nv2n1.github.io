---
title: "skb_cow(9)"
name: "skb_cow"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_cow/"
---

skb_cow - copy header of skb when it is required

<h2>Synopsis</h2>

<pre><code>int skb_cow(struct sk_buff *skb, unsigned int headroom);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to cow</dl>
 

 <i>headroom</i>
<dl><dd>needed headroom</dl>

<h2>Description</h2>

If the skb passed lacks sufficient headroom or its data part is shared, data is reallocated. If reallocation fails, an error is returned and original skb is not changed. 

 The result is skb with writable area skb-&gt;head...skb-&gt;tail and at least <i>headroom</i> of space at head.

<h2>Copyright</h2>


