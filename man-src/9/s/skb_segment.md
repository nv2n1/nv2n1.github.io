---
title: "skb_segment(9)"
name: "skb_segment"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_segment/"
---

skb_segment - Perform protocol segmentation on skb.

<h2>Synopsis</h2>

<pre><code>struct sk_buff *skb_segment(struct sk_buff *head_skb, netdev_features_t features);</code></pre>

<h2>Arguments</h2>

<i>head_skb</i>
<dl><dd><dd>buffer to segment</dl>
 

 <i>features</i>
<dl><dd>features for the output path (see dev-&gt;features)</dl>

<h2>Description</h2>

This function performs segmentation on the given skb. It returns a pointer to the first in a list of new skbs for the segments. In case of error it returns ERR_PTR(err).

<h2>Copyright</h2>


