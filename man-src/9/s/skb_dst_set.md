---
title: "skb_dst_set(9)"
name: "skb_dst_set"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_dst_set/"
description: "skb_dst_set – sets skb dst"
---

<p>skb_dst_set &#8211; sets skb dst</p>
<h2>Synopsis</h2>
<pre><code>void skb_dst_set(struct sk_buff *skb, struct dst_entry *dst);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer</dl>
<p> <i>dst</i></p>
<dl>
<dd>dst entry</dl>
<h2>Description</h2>
<p>Sets skb dst, assuming a reference was taken on dst and should be released by <code>skb_dst_drop</code></p>
<h2>Copyright</h2>
