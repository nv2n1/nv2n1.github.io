---
title: "skb_frag_dma_map(9)"
name: "skb_frag_dma_map"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_frag_dma_map/"
description: "skb_frag_dma_map – maps a paged fragment via the DMA API"
---

<p>skb_frag_dma_map &#8211; maps a paged fragment via the DMA API</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>dma_addr_t skb_frag_dma_map(struct device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, const skb_frag_t&nbsp;<wbr>*&nbsp;<wbr></code><i>frag</i><code>, size_t&nbsp;<wbr></code><i>offset</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>, enum dma_data_direction&nbsp;<wbr></code><i>dir</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device to map the fragment to</dl>
<p> <i>frag</i></p>
<dl>
<dd>the paged fragment to map</dl>
<p> <i>offset</i></p>
<dl>
<dd>the offset within the fragment (starting at the fragment&#8217;s own offset)</dl>
<p> <i>size</i></p>
<dl>
<dd>the number of bytes to map</dl>
<p> <i>dir</i></p>
<dl>
<dd>the direction of the mapping (<code>PCI_DMA_</code>*)</dl>
<h2>Description</h2>
<p>Maps the page associated with <i>frag</i> to <i>device</i>.</p>
<h2>Copyright</h2>
