---
title: "eth_random_addr(9)"
name: "eth_random_addr"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_random_addr/"
---

eth_random_addr - Generate software assigned random Ethernet address

<h2>Synopsis</h2>

<pre><code>void eth_random_addr(u8 *addr);</code></pre>

<h2>Arguments</h2>

<i>addr</i>
<dl><dd><dd>Pointer to a six-byte array containing the Ethernet address</dl>

<h2>Description</h2>

Generate a random Ethernet address (MAC) that is not multicast and has the local assigned bit set.

<h2>Copyright</h2>


