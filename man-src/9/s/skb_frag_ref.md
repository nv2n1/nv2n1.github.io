---
title: "skb_frag_ref(9)"
name: "skb_frag_ref"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_frag_ref/"
---

skb_frag_ref - take an addition reference on a paged fragment of an skb.

<h2>Synopsis</h2>

<pre><code>void skb_frag_ref(struct sk_buff *skb, int f);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>the buffer</dl>
 

 <i>f</i>
<dl><dd>the fragment offset.</dl>

<h2>Description</h2>

Takes an additional reference on the <i>f</i>'th paged fragment of <i>skb</i>.

<h2>Copyright</h2>


