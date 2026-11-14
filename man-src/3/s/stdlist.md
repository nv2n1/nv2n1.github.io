---
title: "stdlist(3)"
name: "stdlist"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlist/"
---

std::list&lt;T,Allocator&gt;::~list - std::list&lt;T,Allocator&gt;::~list

<h2>Synopsis</h2>

<pre><code>~list();</code></pre> 
Destructs the container. The destructors of the elements are called and the used storage is deallocated. Note, that if the elements are pointers, the pointed-to objects are not destroyed. 

<h2>Complexity</h2>

Linear in the size of the container.
