---
title: "ether_addr_copy(9)"
name: "ether_addr_copy"
section: "9"
letter: "e"
url: "/docs/linux/man/9-ether_addr_copy/"
---

ether_addr_copy - Copy an Ethernet address

<h2>Synopsis</h2>

<pre><code>void ether_addr_copy(u8 *dst, const u8 *src);</code></pre>

<h2>Arguments</h2>

<i>dst</i>
<dl><dd><dd>Pointer to a six-byte array Ethernet address destination</dl>
 

 <i>src</i>
<dl><dd>Pointer to a six-byte array Ethernet address source</dl>

<h2>Description</h2>

Please note: dst &amp; src must both be aligned to u16.

<h2>Copyright</h2>


