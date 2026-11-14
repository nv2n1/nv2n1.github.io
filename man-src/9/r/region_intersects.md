---
title: "region_intersects(9)"
name: "region_intersects"
section: "9"
letter: "r"
url: "/docs/linux/man/9-region_intersects/"
description: "region_intersects – determine intersection of region with known resources"
---

<p>region_intersects &#8211; determine intersection of region with known resources</p>
<h2>Synopsis</h2>
<pre><code>int region_intersects(resource_size_t start, size_t size, unsigned long flags, unsigned long desc);</code></pre>
<h2>Arguments</h2>
<p><i>start</i></p>
<dl>
<dd>
<dd>region start address</dl>
<p> <i>size</i></p>
<dl>
<dd>size of region</dl>
<p> <i>flags</i></p>
<dl>
<dd>flags of resource (in iomem_resource)</dl>
<p> <i>desc</i></p>
<dl>
<dd>descriptor of resource (in iomem_resource) or IORES_DESC_NONE</dl>
<h2>Description</h2>
<p>Check if the specified region partially overlaps or fully eclipses a resource identified by <i>flags</i> and <i>desc</i> (optional with IORES_DESC_NONE). Return REGION_DISJOINT if the region does not overlap <i>flags</i>/<i>desc</i>, return REGION_MIXED if the region overlaps <i>flags</i>/<i>desc</i> and another resource, and return REGION_INTERSECTS if the region overlaps <i>flags</i>/<i>desc</i> and no other defined resource. Note that REGION_INTERSECTS is also returned in the case when the specified region overlaps RAM and undefined memory holes. </p>
<p> <code>region_intersect</code> is used by memory remapping functions to ensure the user is not remapping RAM and is a vast speed up over walking through the resource table page by page.</p>
<h2>Copyright</h2>
