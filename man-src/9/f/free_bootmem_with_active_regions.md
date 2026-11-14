---
title: "free_bootmem_with_active_regions(9)"
name: "free_bootmem_with_active_regions"
section: "9"
letter: "f"
url: "/docs/linux/man/9-free_bootmem_with_active_regions/"
description: "free_bootmem_with_active_regions – Call memblock_free_early_nid for each active range"
---

<p>free_bootmem_with_active_regions &#8211; Call memblock_free_early_nid for each active range</p>
<h2>Synopsis</h2>
<pre><code>void free_bootmem_with_active_regions(int nid, unsigned long max_low_pfn);</code></pre>
<h2>Arguments</h2>
<p><i>nid</i></p>
<dl>
<dd>
<dd>The node to free memory on. If MAX_NUMNODES, all nodes are freed.</dl>
<p> <i>max_low_pfn</i></p>
<dl>
<dd>The highest PFN that will be passed to memblock_free_early_nid</dl>
<h2>Description</h2>
<p>If an architecture guarantees that all ranges registered contain no holes and may be freed, this this function may be used instead of calling <code>memblock_free_early_nid</code> manually.</p>
<h2>Copyright</h2>
