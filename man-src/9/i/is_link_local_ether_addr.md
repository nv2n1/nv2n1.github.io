---
title: "is_link_local_ether_addr(9)"
name: "is_link_local_ether_addr"
section: "9"
letter: "i"
url: "/docs/linux/man/9-is_link_local_ether_addr/"
description: "is_link_local_ether_addr – Determine if given Ethernet address is link-local"
---

<p>is_link_local_ether_addr &#8211; Determine if given Ethernet address is link-local</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool is_link_local_ether_addr(const u8&nbsp;<wbr>*&nbsp;<wbr></code><i>addr</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>addr</i></p>
<dl>
<dd>
<dd>Pointer to a six-byte array containing the Ethernet address</dl>
<h2>Description</h2>
<p>Return true if address is link local reserved addr (01:80:c2:00:00:0X) per IEEE 802.1Q 8.6.3 Frame filtering. </p>
<p> Please note: addr must be aligned to u16.</p>
<h2>Copyright</h2>
