---
title: "pskb_trim_unique(9)"
name: "pskb_trim_unique"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pskb_trim_unique/"
---

pskb_trim_unique - remove end from a paged unique (not cloned) buffer

<h2>Synopsis</h2>

<pre><code>void pskb_trim_unique(struct sk_buff *skb, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to alter</dl>
 

 <i>len</i>
<dl><dd>new length</dl>

<h2>Description</h2>

This is identical to pskb_trim except that the caller knows that the skb is not cloned so we should never get an error due to out- of-memory.

<h2>Copyright</h2>


