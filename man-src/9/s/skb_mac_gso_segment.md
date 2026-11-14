---
title: "skb_mac_gso_segment(9)"
name: "skb_mac_gso_segment"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_mac_gso_segment/"
---

skb_mac_gso_segment - mac layer segmentation handler.

<h2>Synopsis</h2>

<pre><code>struct sk_buff *skb_mac_gso_segment(struct sk_buff *skb, netdev_features_t features);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to segment</dl>
 

 <i>features</i>
<dl><dd>features for the output path (see dev-&gt;features)</dl>

<h2>Copyright</h2>


