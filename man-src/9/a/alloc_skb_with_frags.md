---
title: "alloc_skb_with_frags(9)"
name: "alloc_skb_with_frags"
section: "9"
letter: "a"
url: "/docs/linux/man/9-alloc_skb_with_frags/"
---

alloc_skb_with_frags - allocate skb with page frags

<h2>Synopsis</h2>

<pre><code>struct sk_buff *alloc_skb_with_frags(unsigned long header_len, unsigned long data_len, int max_page_order, int *errcode, gfp_t gfp_mask);</code></pre>

<h2>Arguments</h2>

<i>header_len</i>
<dl><dd><dd>size of linear part</dl>
 

 <i>data_len</i>
<dl><dd>needed length in frags</dl>
 

 <i>max_page_order</i>
<dl><dd>max page order desired.</dl>
 

 <i>errcode</i>
<dl><dd>pointer to error code if any</dl>
 

 <i>gfp_mask</i>
<dl><dd>allocation mask</dl>

<h2>Description</h2>

This can be used to allocate a paged skb, given a maximal order for frags.

<h2>Copyright</h2>


