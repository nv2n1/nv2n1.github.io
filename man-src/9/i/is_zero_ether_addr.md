---
title: "is_zero_ether_addr(9)"
name: "is_zero_ether_addr"
section: "9"
letter: "i"
url: "/docs/linux/man/9-is_zero_ether_addr/"
description: "is_zero_ether_addr – Determine if give Ethernet address is all zeros."
---

<p>is_zero_ether_addr &#8211; Determine if give Ethernet address is all zeros.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool is_zero_ether_addr(const u8&nbsp;<wbr>*&nbsp;<wbr></code><i>addr</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>addr</i></p>
<dl>
<dd>
<dd>Pointer to a six-byte array containing the Ethernet address</dl>
<h2>Description</h2>
<p>Return true if the address is all zeroes. </p>
<p> Please note: addr must be aligned to u16.</p>
<h2>Copyright</h2>
