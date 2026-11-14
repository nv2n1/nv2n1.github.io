---
title: "skb_availroom(9)"
name: "skb_availroom"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_availroom/"
description: "skb_availroom – bytes at buffer end"
---

<p>skb_availroom &#8211; bytes at buffer end</p>
<h2>Synopsis</h2>
<pre><code>int skb_availroom(const struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer to check</dl>
<h2>Description</h2>
<p>Return the number of bytes of free space at the tail of an sk_buff allocated by <code>sk_stream_alloc</code></p>
<h2>Copyright</h2>
