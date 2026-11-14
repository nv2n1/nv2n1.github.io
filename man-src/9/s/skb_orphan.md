---
title: "skb_orphan(9)"
name: "skb_orphan"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_orphan/"
---

skb_orphan - orphan a buffer

<h2>Synopsis</h2>

<pre><code>void skb_orphan(struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to orphan</dl>

<h2>Description</h2>

If a buffer currently has an owner then we call the owner's destructor function and make the <i>skb</i> unowned. The buffer continues to exist but is no longer charged to its former owner.

<h2>Copyright</h2>


