---
title: "skb_gso_network_seglen(9)"
name: "skb_gso_network_seglen"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_gso_network_seglen/"
---

skb_gso_network_seglen - Return length of individual segments of a gso packet

<h2>Synopsis</h2>

<pre><code>unsigned int skb_gso_network_seglen(const struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>GSO skb</dl>

<h2>Description</h2>

skb_gso_network_seglen is used to determine the real size of the individual segments, including Layer3 (IP, IPv6) and L4 headers (TCP/UDP). 

 The MAC/L2 header is not accounted for.

<h2>Copyright</h2>


