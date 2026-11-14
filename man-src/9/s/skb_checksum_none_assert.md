---
title: "skb_checksum_none_assert(9)"
name: "skb_checksum_none_assert"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_checksum_none_assert/"
---

skb_checksum_none_assert - make sure skb ip_summed is CHECKSUM_NONE

<h2>Synopsis</h2>

<pre><code>void skb_checksum_none_assert(const struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>skb to check</dl>

<h2>Description</h2>

fresh skbs have their ip_summed set to CHECKSUM_NONE. Instead of forcing ip_summed to CHECKSUM_NONE, we can use this helper, to document places where we make this assertion.

<h2>Copyright</h2>


