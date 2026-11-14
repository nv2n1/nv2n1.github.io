---
title: "skb_checksum_setup(9)"
name: "skb_checksum_setup"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_checksum_setup/"
---

skb_checksum_setup - set up partial checksum offset

<h2>Synopsis</h2>

<pre><code>int skb_checksum_setup(struct sk_buff *skb, bool recalculate);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>the skb to set up</dl>
 

 <i>recalculate</i>
<dl><dd>if true the pseudo-header checksum will be recalculated</dl>

<h2>Copyright</h2>


