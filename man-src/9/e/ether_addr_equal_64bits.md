---
title: "ether_addr_equal_64bits(9)"
name: "ether_addr_equal_64bits"
section: "9"
letter: "e"
url: "/docs/linux/man/9-ether_addr_equal_64bits/"
description: "ether_addr_equal_64bits – Compare two Ethernet addresses"
---

<p>ether_addr_equal_64bits &#8211; Compare two Ethernet addresses</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool ether_addr_equal_64bits(const u8&nbsp;<wbr></code><i>addr1[6+2]</i><code>, const u8&nbsp;<wbr></code><i>addr2[6+2]</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>addr1[6+2]</i></p>
<dl>
<dd>
<dd>Pointer to an array of 8 bytes</dl>
<p> <i>addr2[6+2]</i></p>
<dl>
<dd>Pointer to an other array of 8 bytes</dl>
<h2>Description</h2>
<p>Compare two Ethernet addresses, returns true if equal, false otherwise. </p>
<p> The function doesn&#8217;t need any conditional branches and possibly uses word memory accesses on CPU allowing cheap unaligned memory reads. arrays = { byte1, byte2, byte3, byte4, byte5, byte6, pad1, pad2 } </p>
<p> Please note that alignment of addr1 &amp; addr2 are only guaranteed to be 16 bits.</p>
<h2>Copyright</h2>
