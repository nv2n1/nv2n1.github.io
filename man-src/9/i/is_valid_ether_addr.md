---
title: "is_valid_ether_addr(9)"
name: "is_valid_ether_addr"
section: "9"
letter: "i"
url: "/docs/linux/man/9-is_valid_ether_addr/"
description: "is_valid_ether_addr – Determine if the given Ethernet address is valid"
---

<p>is_valid_ether_addr &#8211; Determine if the given Ethernet address is valid</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool is_valid_ether_addr(const u8&nbsp;<wbr>*&nbsp;<wbr></code><i>addr</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>addr</i></p>
<dl>
<dd>
<dd>Pointer to a six-byte array containing the Ethernet address</dl>
<h2>Description</h2>
<p>Check that the Ethernet address (MAC) is not 00:00:00:00:00:00, is not a multicast address, and is not FF:FF:FF:FF:FF:FF. </p>
<p> Return true if the address is valid. </p>
<p> Please note: addr must be aligned to u16.</p>
<h2>Copyright</h2>
