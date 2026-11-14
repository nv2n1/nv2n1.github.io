---
title: "skb_cloned(9)"
name: "skb_cloned"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_cloned/"
description: "skb_cloned – is the buffer a clone"
---

<p>skb_cloned &#8211; is the buffer a clone</p>
<h2>Synopsis</h2>
<pre><code>int skb_cloned(const struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer to check</dl>
<h2>Description</h2>
<p>Returns true if the buffer was generated with <code>skb_clone</code> and is one of multiple shared copies of the buffer. Cloned buffers are shared data so must not be written to under normal circumstances.</p>
<h2>Copyright</h2>
