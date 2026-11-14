---
title: "reallocate_resource(9)"
name: "reallocate_resource"
section: "9"
letter: "r"
url: "/docs/linux/man/9-reallocate_resource/"
---

reallocate_resource - allocate a slot in the resource tree given range &amp; alignment. The resource will be relocated if the new size cannot be reallocated in the current location.

<h2>Synopsis</h2>

<pre><code>int reallocate_resource(struct resource *root, struct resource *old, resource_size_t newsize, struct resource_constraint *constraint);</code></pre>

<h2>Arguments</h2>

<i>root</i>
<dl><dd><dd>root resource descriptor</dl>
 

 <i>old</i>
<dl><dd>resource descriptor desired by caller</dl>
 

 <i>newsize</i>
<dl><dd>new size of the resource descriptor</dl>
 

 <i>constraint</i>
<dl><dd>the size and alignment constraints to be met.</dl>

<h2>Copyright</h2>


