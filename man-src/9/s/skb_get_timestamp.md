---
title: "skb_get_timestamp(9)"
name: "skb_get_timestamp"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_get_timestamp/"
---

skb_get_timestamp - get timestamp from a skb

<h2>Synopsis</h2>

<pre><code>void skb_get_timestamp(const struct sk_buff *skb, struct timeval *stamp);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>skb to get stamp from</dl>
 

 <i>stamp</i>
<dl><dd>pointer to struct timeval to store stamp in</dl>

<h2>Description</h2>

Timestamps are stored in the skb as offsets to a base timestamp. This function converts the offset back to a struct timeval and stores it in stamp.

<h2>Copyright</h2>


