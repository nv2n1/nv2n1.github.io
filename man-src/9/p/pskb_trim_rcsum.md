---
title: "pskb_trim_rcsum(9)"
name: "pskb_trim_rcsum"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pskb_trim_rcsum/"
---

pskb_trim_rcsum - trim received skb and update checksum

<h2>Synopsis</h2>

<pre><code>int pskb_trim_rcsum(struct sk_buff *skb, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to trim</dl>
 

 <i>len</i>
<dl><dd>new length</dl>

<h2>Description</h2>

This is exactly the same as pskb_trim except that it ensures the checksum of received packets are still valid after the operation.

<h2>Copyright</h2>


