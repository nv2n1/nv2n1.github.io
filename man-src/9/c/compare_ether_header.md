---
title: "compare_ether_header(9)"
name: "compare_ether_header"
section: "9"
letter: "c"
url: "/docs/linux/man/9-compare_ether_header/"
---

compare_ether_header - Compare two Ethernet headers

<h2>Synopsis</h2>

<pre><code>unsigned long compare_ether_header(const void *a, const void *b);</code></pre>

<h2>Arguments</h2>

<i>a</i>
<dl><dd><dd>Pointer to Ethernet header</dl>
 

 <i>b</i>
<dl><dd>Pointer to Ethernet header</dl>

<h2>Description</h2>

Compare two Ethernet headers, returns 0 if equal. This assumes that the network header (i.e., IP header) is 4-byte aligned OR the platform can handle unaligned access. This is the case for all packets coming into netif_receive_skb or similar entry points.

<h2>Copyright</h2>


