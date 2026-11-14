---
title: "alloc_contig_range(9)"
name: "alloc_contig_range"
section: "9"
letter: "a"
url: "/docs/linux/man/9-alloc_contig_range/"
description: "alloc_contig_range – – tries to allocate given range of pages"
---

<p>alloc_contig_range &#8211; &#8211; tries to allocate given range of pages</p>
<h2>Synopsis</h2>
<pre><code>int alloc_contig_range(unsigned long start, unsigned long end, unsigned migratetype);</code></pre>
<h2>Arguments</h2>
<p><i>start</i></p>
<dl>
<dd>
<dd>start PFN to allocate</dl>
<p> <i>end</i></p>
<dl>
<dd>one-past-the-last PFN to allocate</dl>
<p> <i>migratetype</i></p>
<dl>
<dd>migratetype of the underlaying pageblocks (either #MIGRATE_MOVABLE or #MIGRATE_CMA). All pageblocks in range must have the same migratetype and it must be either of the two.</dl>
<h2>Description</h2>
<p>The PFN range does not have to be pageblock or MAX_ORDER_NR_PAGES aligned, however it&#8217;s the caller&#8217;s responsibility to guarantee that we are the only thread that changes migrate type of pageblocks the pages fall in. </p>
<p> The PFN range must belong to a single zone. </p>
<p> Returns zero on success or negative error code. On success all pages which PFN is in [start, end) are allocated for the caller and need to be freed with <code>free_contig_range</code>.</p>
<h2>Copyright</h2>
