---
title: "stdmap(3)"
name: "stdmap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmap/"
---

std::map&lt;Key,T,Compare,Allocator&gt;::~map - std::map&lt;Key,T,Compare,Allocator&gt;::~map

<h2>Synopsis</h2>

<pre><code>~map();</code></pre> 
Destructs the container. The destructors of the elements are called and the used storage is deallocated. Note, that if the elements are pointers, the pointed-to objects are not destroyed. 

<h2>Complexity</h2>

Linear in the size of the container.
