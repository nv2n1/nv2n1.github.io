---
title: "skb_gso_transport_seglen(9)"
name: "skb_gso_transport_seglen"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_gso_transport_seglen/"
---

skb_gso_transport_seglen - Return length of individual segments of a gso packet

<h2>Synopsis</h2>

<pre><code>unsigned int skb_gso_transport_seglen(const struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>GSO skb</dl>

<h2>Description</h2>

skb_gso_transport_seglen is used to determine the real size of the individual segments, including Layer4 headers (TCP/UDP). 

 The MAC/L2 or network (IP, IPv6) headers are not accounted for.

<h2>Copyright</h2>


