---
title: "free_area_init_nodes(9)"
name: "free_area_init_nodes"
section: "9"
letter: "f"
url: "/docs/linux/man/9-free_area_init_nodes/"
description: "free_area_init_nodes – Initialise all pg_data_t and zone data"
---

<p>free_area_init_nodes &#8211; Initialise all pg_data_t and zone data</p>
<h2>Synopsis</h2>
<pre><code>void free_area_init_nodes(unsigned long *max_zone_pfn);</code></pre>
<h2>Arguments</h2>
<p><i>max_zone_pfn</i></p>
<dl>
<dd>
<dd>an array of max PFNs for each zone</dl>
<h2>Description</h2>
<p>This will call <code>free_area_init_node</code> for each active node in the system. Using the page ranges provided by <code>memblock_set_node</code>, the size of each zone in each node and their holes is calculated. If the maximum PFN between two adjacent zones match, it is assumed that the zone is empty. For example, if arch_max_dma_pfn == arch_max_dma32_pfn, it is assumed that arch_max_dma32_pfn has no pages. It is also assumed that a zone starts where the previous one ended. For example, ZONE_DMA32 starts at arch_max_dma_pfn.</p>
<h2>Copyright</h2>
