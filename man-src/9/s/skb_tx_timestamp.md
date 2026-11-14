---
title: "skb_tx_timestamp(9)"
name: "skb_tx_timestamp"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_tx_timestamp/"
description: "skb_tx_timestamp – Driver hook for transmit timestamping"
---

<p>skb_tx_timestamp &#8211; Driver hook for transmit timestamping</p>
<h2>Synopsis</h2>
<pre><code>void skb_tx_timestamp(struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>A socket buffer.</dl>
<h2>Description</h2>
<p>Ethernet MAC Drivers should call this function in their <code>hard_xmit</code> function immediately before giving the sk_buff to the MAC hardware. </p>
<p> Specifically, one should make absolutely sure that this function is called before TX completion of this packet can trigger. Otherwise the packet could potentially already be freed.</p>
<h2>Copyright</h2>
