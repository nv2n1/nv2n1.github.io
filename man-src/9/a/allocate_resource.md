---
title: "allocate_resource(9)"
name: "allocate_resource"
section: "9"
letter: "a"
url: "/docs/linux/man/9-allocate_resource/"
---

allocate_resource - allocate empty slot in the resource tree given range &amp; alignment. The resource will be reallocated with a new size if it was already allocated

<h2>Synopsis</h2>

<pre><code>int allocate_resource(struct resource *root, struct resource *new, resource_size_t size, resource_size_t min, resource_size_t max, resource_size_t align, resource_size_t (*alignf)(void *, const struct resource *, resource_size_t, resource_size_t), void *alignf_data);</code></pre>

<h2>Arguments</h2>

<i>root</i>
<dl><dd><dd>root resource descriptor</dl>
 

 <i>new</i>
<dl><dd>resource descriptor desired by caller</dl>
 

 <i>size</i>
<dl><dd>requested resource region size</dl>
 

 <i>min</i>
<dl><dd>minimum boundary to allocate</dl>
 

 <i>max</i>
<dl><dd>maximum boundary to allocate</dl>
 

 <i>align</i>
<dl><dd>alignment requested, in bytes</dl>
 

 <i>alignf</i>
<dl><dd>alignment function, optional, called if not NULL</dl>
 

 <i>alignf_data</i>
<dl><dd>arbitrary data to pass to the <i>alignf</i> function</dl>

<h2>Copyright</h2>


