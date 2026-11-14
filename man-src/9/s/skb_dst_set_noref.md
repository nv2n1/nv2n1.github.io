---
title: "skb_dst_set_noref(9)"
name: "skb_dst_set_noref"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_dst_set_noref/"
---

skb_dst_set_noref - sets skb dst, hopefully, without taking reference

<h2>Synopsis</h2>

<pre><code>void skb_dst_set_noref(struct sk_buff *skb, struct dst_entry *dst);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer</dl>
 

 <i>dst</i>
<dl><dd>dst entry</dl>

<h2>Description</h2>

Sets skb dst, assuming a reference was not taken on dst. If dst entry is cached, we do not take reference and dst_release will be avoided by refdst_drop. If dst entry is not cached, we take reference, so that last dst_release can destroy the dst immediately.

<h2>Copyright</h2>


