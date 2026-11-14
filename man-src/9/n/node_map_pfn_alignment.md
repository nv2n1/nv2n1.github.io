---
title: "node_map_pfn_alignment(9)"
name: "node_map_pfn_alignment"
section: "9"
letter: "n"
url: "/docs/linux/man/9-node_map_pfn_alignment/"
---

node_map_pfn_alignment - determine the maximum internode alignment

<h2>Synopsis</h2>

<pre><code>unsigned long node_map_pfn_alignment(void);</code></pre>

<h2>Arguments</h2>

<i>void</i>
<dl><dd><dd>no arguments</dl>

<h2>Description</h2>

This function should be called after node map is populated and sorted. It calculates the maximum power of two alignment which can distinguish all the nodes. 

 For example, if all nodes are 1GiB and aligned to 1GiB, the return value would indicate 1GiB alignment with (1 &lt;&lt; (30 - PAGE_SHIFT)). If the nodes are shifted by 256MiB, 256MiB. Note that if only the last node is shifted, 1GiB is enough and this function will indicate so. 

 This is used to test whether pfn -&gt; nid mapping of the chosen memory model has fine enough granularity to avoid incorrect mapping for the populated node map. 

 Returns the determined alignment in pfn's. 0 if there is no alignment requirement (single node).

<h2>Copyright</h2>


