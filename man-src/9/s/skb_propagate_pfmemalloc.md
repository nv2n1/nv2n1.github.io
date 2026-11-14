---
title: "skb_propagate_pfmemalloc(9)"
name: "skb_propagate_pfmemalloc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_propagate_pfmemalloc/"
---

skb_propagate_pfmemalloc - Propagate pfmemalloc if skb is allocated after RX page

<h2>Synopsis</h2>

<pre><code>void skb_propagate_pfmemalloc(struct page *page, struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>page</i>
<dl><dd><dd>The page that was allocated from skb_alloc_page</dl>
 

 <i>skb</i>
<dl><dd>The skb that may need pfmemalloc set</dl>

<h2>Copyright</h2>


