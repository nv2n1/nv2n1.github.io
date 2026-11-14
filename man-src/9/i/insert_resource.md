---
title: "insert_resource(9)"
name: "insert_resource"
section: "9"
letter: "i"
url: "/docs/linux/man/9-insert_resource/"
---

insert_resource - Inserts a resource in the resource tree

<h2>Synopsis</h2>

<pre><code>int insert_resource(struct resource *parent, struct resource *new);</code></pre>

<h2>Arguments</h2>

<i>parent</i>
<dl><dd><dd>parent of the new resource</dl>
 

 <i>new</i>
<dl><dd>new resource to insert</dl>

<h2>Description</h2>

Returns 0 on success, -EBUSY if the resource can't be inserted. 

 This function is intended for producers of resources, such as FW modules and bus drivers.

<h2>Copyright</h2>


