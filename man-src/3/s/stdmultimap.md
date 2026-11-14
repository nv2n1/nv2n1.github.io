---
title: "stdmultimap(3)"
name: "stdmultimap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmultimap/"
---

std::multimap&lt;Key,T,Compare,Allocator&gt;::~multimap - std::multimap&lt;Key,T,Compare,Allocator&gt;::~multimap

<h2>Synopsis</h2>

<pre><code>~multimap();</code></pre> 
Destructs the container. The destructors of the elements are called and the used storage is deallocated. Note, that if the elements are pointers, the pointed-to objects are not destroyed. 

<h2>Complexity</h2>

Linear in the size of the container.
