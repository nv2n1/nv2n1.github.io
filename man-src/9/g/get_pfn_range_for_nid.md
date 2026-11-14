---
title: "get_pfn_range_for_nid(9)"
name: "get_pfn_range_for_nid"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_pfn_range_for_nid/"
description: "get_pfn_range_for_nid – Return the start and end page frames for a node"
---

<p>get_pfn_range_for_nid &#8211; Return the start and end page frames for a node</p>
<h2>Synopsis</h2>
<pre><code>void get_pfn_range_for_nid(unsigned int nid, unsigned long *start_pfn, unsigned long *end_pfn);</code></pre>
<h2>Arguments</h2>
<p><i>nid</i></p>
<dl>
<dd>
<dd>The nid to return the range for. If MAX_NUMNODES, the min and max PFN are returned.</dl>
<p> <i>start_pfn</i></p>
<dl>
<dd>Passed by reference. On return, it will have the node start_pfn.</dl>
<p> <i>end_pfn</i></p>
<dl>
<dd>Passed by reference. On return, it will have the node end_pfn.</dl>
<h2>Description</h2>
<p>It returns the start and end page frame of a node based on information provided by <code>memblock_set_node</code>. If called for a node with no available memory, a warning is printed and the start and end PFNs will be 0.</p>
<h2>Copyright</h2>
