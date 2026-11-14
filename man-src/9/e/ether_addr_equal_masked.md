---
title: "ether_addr_equal_masked(9)"
name: "ether_addr_equal_masked"
section: "9"
letter: "e"
url: "/docs/linux/man/9-ether_addr_equal_masked/"
description: "ether_addr_equal_masked – Compare two Ethernet addresses with a mask"
---

<p>ether_addr_equal_masked &#8211; Compare two Ethernet addresses with a mask</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool ether_addr_equal_masked(const u8&nbsp;<wbr>*&nbsp;<wbr></code><i>addr1</i><code>, const u8&nbsp;<wbr>*&nbsp;<wbr></code><i>addr2</i><code>, const u8&nbsp;<wbr>*&nbsp;<wbr></code><i>mask</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>addr1</i></p>
<dl>
<dd>
<dd>Pointer to a six-byte array containing the 1st Ethernet address</dl>
<p> <i>addr2</i></p>
<dl>
<dd>Pointer to a six-byte array containing the 2nd Ethernet address</dl>
<p> <i>mask</i></p>
<dl>
<dd>Pointer to a six-byte array containing the Ethernet address bitmask</dl>
<h2>Description</h2>
<p>Compare two Ethernet addresses with a mask, returns true if for every bit set in the bitmask the equivalent bits in the ethernet addresses are equal. Using a mask with all bits set is a slower ether_addr_equal.</p>
<h2>Copyright</h2>
