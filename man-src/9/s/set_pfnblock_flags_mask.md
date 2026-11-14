---
title: "set_pfnblock_flags_mask(9)"
name: "set_pfnblock_flags_mask"
section: "9"
letter: "s"
url: "/docs/linux/man/9-set_pfnblock_flags_mask/"
---

set_pfnblock_flags_mask - Set the requested group of flags for a pageblock_nr_pages block of pages

<h2>Synopsis</h2>

<pre><code>void set_pfnblock_flags_mask(struct page *page, unsigned long flags, unsigned long pfn, unsigned long end_bitidx, unsigned long mask);</code></pre>

<h2>Arguments</h2>

<i>page</i>
<dl><dd><dd>The page within the block of interest</dl>
 

 <i>flags</i>
<dl><dd>The flags to set</dl>
 

 <i>pfn</i>
<dl><dd>The target page frame number</dl>
 

 <i>end_bitidx</i>
<dl><dd>The last bit of interest</dl>
 

 <i>mask</i>
<dl><dd>mask of bits that the caller is interested in</dl>

<h2>Copyright</h2>


