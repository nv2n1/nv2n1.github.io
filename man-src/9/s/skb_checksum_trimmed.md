---
title: "skb_checksum_trimmed(9)"
name: "skb_checksum_trimmed"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_checksum_trimmed/"
---

skb_checksum_trimmed - validate checksum of an skb

<h2>Synopsis</h2>

<pre><code>struct sk_buff *skb_checksum_trimmed(struct sk_buff *skb, unsigned int transport_len, __sum16 (*skb_chkf)(struct sk_buff *skb));</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>the skb to check</dl>
 

 <i>transport_len</i>
<dl><dd>the data length beyond the network header</dl>
 

 <i>skb_chkf</i>
<dl><dd>checksum function to use</dl>

<h2>Description</h2>

Applies the given checksum function skb_chkf to the provided skb. Returns a checked and maybe trimmed skb. Returns NULL on error. 

 If the skb has data beyond the given transport length, then a trimmed &amp; cloned skb is checked and returned. 

 Caller needs to set the skb transport header and free any returned skb if it differs from the provided skb.

<h2>Copyright</h2>


