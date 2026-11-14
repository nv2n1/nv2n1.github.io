---
title: "adjust_resource(9)"
name: "adjust_resource"
section: "9"
letter: "a"
url: "/docs/linux/man/9-adjust_resource/"
---

adjust_resource - modify a resource's start and size

<h2>Synopsis</h2>

<pre><code>int adjust_resource(struct resource *res, resource_size_t start, resource_size_t size);</code></pre>

<h2>Arguments</h2>

<i>res</i>
<dl><dd><dd>resource to modify</dl>
 

 <i>start</i>
<dl><dd>new start value</dl>
 

 <i>size</i>
<dl><dd>new size</dl>

<h2>Description</h2>

Given an existing resource, change its start and size to match the arguments. Returns 0 on success, -EBUSY if it can't fit. Existing children of the resource are assumed to be immutable.

<h2>Copyright</h2>


