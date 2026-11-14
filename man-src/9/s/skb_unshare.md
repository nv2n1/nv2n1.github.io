---
title: "skb_unshare(9)"
name: "skb_unshare"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_unshare/"
description: "skb_unshare – make a copy of a shared buffer"
---

<p>skb_unshare &#8211; make a copy of a shared buffer</p>
<h2>Synopsis</h2>
<pre><code>struct sk_buff *skb_unshare(struct sk_buff *skb, gfp_t pri);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer to check</dl>
<p> <i>pri</i></p>
<dl>
<dd>priority for memory allocation</dl>
<h2>Description</h2>
<p>If the socket buffer is a clone then this function creates a new copy of the data, drops a reference count on the old copy and returns the new copy with the reference count at 1. If the buffer is not a clone the original buffer is returned. When called with a spinlock held or from interrupt state <i>pri</i> must be <code>GFP_ATOMIC</code> </p>
<p> <code>NULL</code> is returned on a memory allocation failure.</p>
<h2>Copyright</h2>
