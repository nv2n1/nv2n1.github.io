---
title: "insert_resource_expand_to_fit(9)"
name: "insert_resource_expand_to_fit"
section: "9"
letter: "i"
url: "/docs/linux/man/9-insert_resource_expand_to_fit/"
---

insert_resource_expand_to_fit - Insert a resource into the resource tree

<h2>Synopsis</h2>

<pre><code>void insert_resource_expand_to_fit(struct resource *root, struct resource *new);</code></pre>

<h2>Arguments</h2>

<i>root</i>
<dl><dd><dd>root resource descriptor</dl>
 

 <i>new</i>
<dl><dd>new resource to insert</dl>

<h2>Description</h2>

Insert a resource into the resource tree, possibly expanding it in order to make it encompass any conflicting resources.

<h2>Copyright</h2>


