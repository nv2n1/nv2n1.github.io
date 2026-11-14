---
title: "sparse_memory_present_with_active_regions(9)"
name: "sparse_memory_present_with_active_regions"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sparse_memory_present_with_active_regions/"
description: "sparse_memory_present_with_active_regions – Call memory_present for each active range"
---

<p>sparse_memory_present_with_active_regions &#8211; Call memory_present for each active range</p>
<h2>Synopsis</h2>
<pre><code>void sparse_memory_present_with_active_regions(int nid);</code></pre>
<h2>Arguments</h2>
<p><i>nid</i></p>
<dl>
<dd>
<dd>The node to call memory_present for. If MAX_NUMNODES, all nodes will be used.</dl>
<h2>Description</h2>
<p>If an architecture guarantees that all ranges registered contain no holes and may be freed, this function may be used instead of calling <code>memory_present</code> manually.</p>
<h2>Copyright</h2>
