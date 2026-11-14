---
title: "skb_page_frag_refill(9)"
name: "skb_page_frag_refill"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_page_frag_refill/"
description: "skb_page_frag_refill – check that a page_frag contains enough room"
---

<p>skb_page_frag_refill &#8211; check that a page_frag contains enough room</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool skb_page_frag_refill(unsigned int&nbsp;<wbr></code><i>sz</i><code>, struct page_frag&nbsp;<wbr>*&nbsp;<wbr></code><i>pfrag</i><code>, gfp_t&nbsp;<wbr></code><i>gfp</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>sz</i></p>
<dl>
<dd>
<dd>minimum size of the fragment we want to get</dl>
<p> <i>pfrag</i></p>
<dl>
<dd>pointer to page_frag</dl>
<p> <i>gfp</i></p>
<dl>
<dd>priority for memory allocation</dl>
<h2>Note</h2>
<p>While this allocator tries to use high order pages, there is no guarantee that allocations succeed. Therefore, <i>sz</i> MUST be less or equal than PAGE_SIZE.</p>
<h2>Copyright</h2>
