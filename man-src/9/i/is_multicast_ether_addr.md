---
title: "is_multicast_ether_addr(9)"
name: "is_multicast_ether_addr"
section: "9"
letter: "i"
url: "/docs/linux/man/9-is_multicast_ether_addr/"
description: "is_multicast_ether_addr – Determine if the Ethernet address is a multicast."
---

<p>is_multicast_ether_addr &#8211; Determine if the Ethernet address is a multicast.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool is_multicast_ether_addr(const u8&nbsp;<wbr>*&nbsp;<wbr></code><i>addr</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>addr</i></p>
<dl>
<dd>
<dd>Pointer to a six-byte array containing the Ethernet address</dl>
<h2>Description</h2>
<p>Return true if the address is a multicast address. By definition the broadcast address is also a multicast address.</p>
<h2>Copyright</h2>
