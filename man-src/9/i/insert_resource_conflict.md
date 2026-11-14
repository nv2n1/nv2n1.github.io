---
title: "insert_resource_conflict(9)"
name: "insert_resource_conflict"
section: "9"
letter: "i"
url: "/docs/linux/man/9-insert_resource_conflict/"
---

insert_resource_conflict - Inserts resource in the resource tree

<h2>Synopsis</h2>

<pre><code>struct resource *insert_resource_conflict(struct resource *parent, struct resource *new);</code></pre>

<h2>Arguments</h2>

<i>parent</i>
<dl><dd><dd>parent of the new resource</dl>
 

 <i>new</i>
<dl><dd>new resource to insert</dl>

<h2>Description</h2>

Returns 0 on success, conflict resource if the resource can't be inserted. 

 This function is equivalent to request_resource_conflict when no conflict happens. If a conflict happens, and the conflicting resources entirely fit within the range of the new resource, then the new resource is inserted and the conflicting resources become children of the new resource. 

 This function is intended for producers of resources, such as FW modules and bus drivers.

<h2>Copyright</h2>


