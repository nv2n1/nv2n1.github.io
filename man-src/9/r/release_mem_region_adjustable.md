---
title: "release_mem_region_adjustable(9)"
name: "release_mem_region_adjustable"
section: "9"
letter: "r"
url: "/docs/linux/man/9-release_mem_region_adjustable/"
---

release_mem_region_adjustable - release a previously reserved memory region

<h2>Synopsis</h2>

<pre><code>int release_mem_region_adjustable(struct resource *parent, resource_size_t start, resource_size_t size);</code></pre>

<h2>Arguments</h2>

<i>parent</i>
<dl><dd><dd>parent resource descriptor</dl>
 

 <i>start</i>
<dl><dd>resource start address</dl>
 

 <i>size</i>
<dl><dd>resource region size</dl>

<h2>Description</h2>

This interface is intended for memory hot-delete. The requested region is released from a currently busy memory resource. The requested region must either match exactly or fit into a single busy resource entry. In the latter case, the remaining resource is adjusted accordingly. Existing children of the busy memory resource must be immutable in the request.

<h2>Note</h2>

- Additional release conditions, such as overlapping region, can be supported after they are confirmed as valid cases. - When a busy memory resource gets split into two entries, the code assumes that all children remain in the lower address entry for simplicity. Enhance this logic when necessary.

<h2>Copyright</h2>


