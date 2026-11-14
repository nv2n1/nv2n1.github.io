---
title: "eth_proto_is_802_3(9)"
name: "eth_proto_is_802_3"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_proto_is_802_3/"
description: "eth_proto_is_802_3 – Determine if a given Ethertype/length is a protocol"
---

<p>eth_proto_is_802_3 &#8211; Determine if a given Ethertype/length is a protocol</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool eth_proto_is_802_3(__be16&nbsp;<wbr></code><i>proto</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>proto</i></p>
<dl>
<dd>
<dd>Ethertype/length value to be tested</dl>
<h2>Description</h2>
<p>Check that the value from the Ethertype/length field is a valid Ethertype. </p>
<p> Return true if the valid is an 802.3 supported Ethertype.</p>
<h2>Copyright</h2>
