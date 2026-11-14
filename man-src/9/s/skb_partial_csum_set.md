---
title: "skb_partial_csum_set(9)"
name: "skb_partial_csum_set"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_partial_csum_set/"
description: "skb_partial_csum_set – set up and verify partial csum values for packet"
---

<p>skb_partial_csum_set &#8211; set up and verify partial csum values for packet</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool skb_partial_csum_set(struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>skb</i><code>, u16&nbsp;<wbr></code><i>start</i><code>, u16&nbsp;<wbr></code><i>off</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>the skb to set</dl>
<p> <i>start</i></p>
<dl>
<dd>the number of bytes after skb-&gt;data to start checksumming.</dl>
<p> <i>off</i></p>
<dl>
<dd>the offset from start to place the checksum.</dl>
<h2>Description</h2>
<p>For untrusted partially-checksummed packets, we need to make sure the values for skb-&gt;csum_start and skb-&gt;csum_offset are valid so we don&#8217;t oops. </p>
<p> This function checks and sets those values and skb-&gt;ip_summed: if this returns false you should drop the packet.</p>
<h2>Copyright</h2>
