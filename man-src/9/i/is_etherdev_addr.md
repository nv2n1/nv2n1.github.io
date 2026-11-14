---
title: "is_etherdev_addr(9)"
name: "is_etherdev_addr"
section: "9"
letter: "i"
url: "/docs/linux/man/9-is_etherdev_addr/"
description: "is_etherdev_addr – Tell if given Ethernet address belongs to the device."
---

<p>is_etherdev_addr &#8211; Tell if given Ethernet address belongs to the device.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool is_etherdev_addr(const struct net_device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, const u8&nbsp;<wbr></code><i>addr[6&nbsp;<wbr>+&nbsp;<wbr>2]</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Pointer to a device structure</dl>
<p> <i>addr[6 + 2]</i></p>
<dl>
<dd>Pointer to a six-byte array containing the Ethernet address</dl>
<h2>Description</h2>
<p>Compare passed address with all addresses of the device. Return true if the address if one of the device addresses. </p>
<p> Note that this function calls <code>ether_addr_equal_64bits</code> so take care of the right padding.</p>
<h2>Copyright</h2>
