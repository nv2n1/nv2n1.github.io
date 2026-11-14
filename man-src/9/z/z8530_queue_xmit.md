---
title: "z8530_queue_xmit(9)"
name: "z8530_queue_xmit"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_queue_xmit/"
description: "z8530_queue_xmit – Queue a packet"
---

<p>z8530_queue_xmit &#8211; Queue a packet</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>netdev_tx_t z8530_queue_xmit(struct z8530_channel&nbsp;<wbr>*&nbsp;<wbr></code><i>c</i><code>, struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>skb</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>The channel to use</dl>
<p> <i>skb</i></p>
<dl>
<dd>The packet to kick down the channel</dl>
<h2>Description</h2>
<p>Queue a packet for transmission. Because we have rather hard to hit interrupt latencies for the Z85230 per packet even in DMA mode we do the flip to DMA buffer if needed here not in the IRQ. </p>
<p> Called from the network code. The lock is not held at this point.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
