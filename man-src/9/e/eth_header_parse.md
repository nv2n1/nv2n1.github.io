---
title: "eth_header_parse(9)"
name: "eth_header_parse"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_header_parse/"
---

eth_header_parse - extract hardware address from packet

<h2>Synopsis</h2>

<pre><code>int eth_header_parse(const struct sk_buff *skb, unsigned char *haddr);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>packet to extract header from</dl>
 

 <i>haddr</i>
<dl><dd>destination buffer</dl>

<h2>Copyright</h2>


