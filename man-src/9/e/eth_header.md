---
title: "eth_header(9)"
name: "eth_header"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_header/"
---

eth_header - create the Ethernet header

<h2>Synopsis</h2>

<pre><code>int eth_header(struct sk_buff *skb, struct net_device *dev, unsigned short type, const void *daddr, const void *saddr, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to alter</dl>
 

 <i>dev</i>
<dl><dd>source device</dl>
 

 <i>type</i>
<dl><dd>Ethernet type field</dl>
 

 <i>daddr</i>
<dl><dd>destination address (NULL leave destination address)</dl>
 

 <i>saddr</i>
<dl><dd>source address (NULL use device source address)</dl>
 

 <i>len</i>
<dl><dd>packet length (&lt;= skb-&gt;len)</dl>

<h2>Description</h2>

Set the protocol type. For a packet of type ETH_P_802_3/2 we put the length in here instead.

<h2>Copyright</h2>


