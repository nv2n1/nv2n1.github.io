---
title: "skb_frag_address(9)"
name: "skb_frag_address"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_frag_address/"
---

skb_frag_address - gets the address of the data contained in a paged fragment

<h2>Synopsis</h2>

<pre><code>void *skb_frag_address(const skb_frag_t *frag);</code></pre>

<h2>Arguments</h2>

<i>frag</i>
<dl><dd><dd>the paged fragment buffer</dl>

<h2>Description</h2>

Returns the address of the data within <i>frag</i>. The page must already be mapped.

<h2>Copyright</h2>


