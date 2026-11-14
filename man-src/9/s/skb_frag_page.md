---
title: "skb_frag_page(9)"
name: "skb_frag_page"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_frag_page/"
---

skb_frag_page - retrieve the page referred to by a paged fragment

<h2>Synopsis</h2>

<pre><code>struct page *skb_frag_page(const skb_frag_t *frag);</code></pre>

<h2>Arguments</h2>

<i>frag</i>
<dl><dd><dd>the paged fragment</dl>

<h2>Description</h2>

Returns the struct page associated with <i>frag</i>.

<h2>Copyright</h2>


