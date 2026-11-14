---
title: "skb_gso_validate_mtu(9)"
name: "skb_gso_validate_mtu"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_gso_validate_mtu/"
description: "skb_gso_validate_mtu – Return in case such skb fits a given MTU"
---

<p>skb_gso_validate_mtu &#8211; Return in case such skb fits a given MTU</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool skb_gso_validate_mtu(const struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>skb</i><code>, unsigned int&nbsp;<wbr></code><i>mtu</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>GSO skb</dl>
<p> <i>mtu</i></p>
<dl>
<dd>MTU to validate against</dl>
<h2>Description</h2>
<p>skb_gso_validate_mtu validates if a given skb will fit a wanted MTU once split.</p>
<h2>Copyright</h2>
