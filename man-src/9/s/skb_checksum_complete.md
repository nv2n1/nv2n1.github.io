---
title: "skb_checksum_complete(9)"
name: "skb_checksum_complete"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_checksum_complete/"
description: "skb_checksum_complete – Calculate checksum of an entire packet"
---

<p>skb_checksum_complete &#8211; Calculate checksum of an entire packet</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>__sum16 skb_checksum_complete(struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>skb</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>packet to process</dl>
<h2>Description</h2>
<p>This function calculates the checksum over the entire packet plus the value of skb-&gt;csum. The latter can be used to supply the checksum of a pseudo header as used by TCP/UDP. It returns the checksum. </p>
<p> For protocols that contain complete checksums such as ICMP/TCP/UDP, this function can be used to verify that checksum on received packets. In that case the function should return zero if the checksum is correct. In particular, this function will return zero if skb-&gt;ip_summed is CHECKSUM_UNNECESSARY which indicates that the hardware has already verified the correctness of the checksum.</p>
<h2>Copyright</h2>
