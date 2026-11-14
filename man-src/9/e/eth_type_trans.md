---
title: "eth_type_trans(9)"
name: "eth_type_trans"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_type_trans/"
description: "eth_type_trans – determine the packet’s protocol ID."
---

<p>eth_type_trans &#8211; determine the packet&#8217;s protocol ID.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>__be16 eth_type_trans(struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>skb</i><code>, struct net_device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>received socket data</dl>
<p> <i>dev</i></p>
<dl>
<dd>receiving network device</dl>
<h2>Description</h2>
<p>The rule here is that we assume 802.3 if the type field is short enough to be a length. This is normal practice and works for any &#8216;now in use&#8217; protocol.</p>
<h2>Copyright</h2>
