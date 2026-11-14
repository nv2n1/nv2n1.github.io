---
title: "skb_clone_writable(9)"
name: "skb_clone_writable"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_clone_writable/"
---

skb_clone_writable - is the header of a clone writable

<h2>Synopsis</h2>

<pre><code>int skb_clone_writable(const struct sk_buff *skb, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to check</dl>
 

 <i>len</i>
<dl><dd>length up to which to write</dl>

<h2>Description</h2>

Returns true if modifying the header part of the cloned buffer does not requires the data to be copied.

<h2>Copyright</h2>


