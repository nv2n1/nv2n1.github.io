---
title: "ether_addr_equal_unaligned(9)"
name: "ether_addr_equal_unaligned"
section: "9"
letter: "e"
url: "/docs/linux/man/9-ether_addr_equal_unaligned/"
description: "ether_addr_equal_unaligned – Compare two not u16 aligned Ethernet addresses"
---

<p>ether_addr_equal_unaligned &#8211; Compare two not u16 aligned Ethernet addresses</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool ether_addr_equal_unaligned(const u8&nbsp;<wbr>*&nbsp;<wbr></code><i>addr1</i><code>, const u8&nbsp;<wbr>*&nbsp;<wbr></code><i>addr2</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>addr1</i></p>
<dl>
<dd>
<dd>Pointer to a six-byte array containing the Ethernet address</dl>
<p> <i>addr2</i></p>
<dl>
<dd>Pointer other six-byte array containing the Ethernet address</dl>
<h2>Description</h2>
<p>Compare two Ethernet addresses, returns true if equal </p>
<p> Please note: Use only when any Ethernet address may not be u16 aligned.</p>
<h2>Copyright</h2>
