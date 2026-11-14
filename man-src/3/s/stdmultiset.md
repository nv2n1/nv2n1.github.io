---
title: "stdmultiset(3)"
name: "stdmultiset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmultiset/"
---

std::multiset&lt;Key,Compare,Allocator&gt;::~multiset - std::multiset&lt;Key,Compare,Allocator&gt;::~multiset

<h2>Synopsis</h2>

<pre><code>~multiset();</code></pre> 
Destructs the container. The destructors of the elements are called and the used storage is deallocated. Note, that if the elements are pointers, the pointed-to objects are not destroyed. 

<h2>Complexity</h2>

Linear in the size of the container.
