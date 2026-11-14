---
title: "lookup_resource(9)"
name: "lookup_resource"
section: "9"
letter: "l"
url: "/docs/linux/man/9-lookup_resource/"
---

lookup_resource - find an existing resource by a resource start address

<h2>Synopsis</h2>

<pre><code>struct resource *lookup_resource(struct resource *root, resource_size_t start);</code></pre>

<h2>Arguments</h2>

<i>root</i>
<dl><dd><dd>root resource descriptor</dl>
 

 <i>start</i>
<dl><dd>resource start address</dl>

<h2>Description</h2>

Returns a pointer to the resource if found, NULL otherwise

<h2>Copyright</h2>


