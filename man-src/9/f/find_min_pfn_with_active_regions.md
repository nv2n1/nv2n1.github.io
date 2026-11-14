---
title: "find_min_pfn_with_active_regions(9)"
name: "find_min_pfn_with_active_regions"
section: "9"
letter: "f"
url: "/docs/linux/man/9-find_min_pfn_with_active_regions/"
description: "find_min_pfn_with_active_regions – Find the minimum PFN registered"
---

<p>find_min_pfn_with_active_regions &#8211; Find the minimum PFN registered</p>
<h2>Synopsis</h2>
<pre><code>unsigned long find_min_pfn_with_active_regions(void);</code></pre>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Description</h2>
<p>It returns the minimum PFN based on information provided via <code>memblock_set_node</code>.</p>
<h2>Copyright</h2>
