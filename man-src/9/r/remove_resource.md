---
title: "remove_resource(9)"
name: "remove_resource"
section: "9"
letter: "r"
url: "/docs/linux/man/9-remove_resource/"
description: "remove_resource – Remove a resource in the resource tree"
---

<p>remove_resource &#8211; Remove a resource in the resource tree</p>
<h2>Synopsis</h2>
<pre><code>int remove_resource(struct resource *old);</code></pre>
<h2>Arguments</h2>
<p><i>old</i></p>
<dl>
<dd>
<dd>resource to remove</dl>
<h2>Description</h2>
<p>Returns 0 on success, -EINVAL if the resource is not valid. </p>
<p> This function removes a resource previously inserted by <code>insert_resource</code> or <code>insert_resource_conflict</code>, and moves the children (if any) up to where they were before. <code>insert_resource</code> and <code>insert_resource_conflict</code> insert a new resource, and move any conflicting resources down to the children of the new resource. </p>
<p> <code>insert_resource</code>, <code>insert_resource_conflict</code> and <code>remove_resource</code> are intended for producers of resources, such as FW modules and bus drivers.</p>
<h2>Copyright</h2>
