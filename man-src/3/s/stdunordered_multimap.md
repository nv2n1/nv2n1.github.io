---
title: "stdunordered_multimap(3)"
name: "stdunordered_multimap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunordered_multimap/"
---

std::unordered_multimap&lt;Key,T,Hash,KeyEqual,Allocator&gt;::~unordered_multimap - std::unordered_multimap&lt;Key,T,Hash,KeyEqual,Allocator&gt;::~unordered_multimap

<h2>Synopsis</h2>

~unordered_multimap(); <i>(since C++11)</i> 
Destructs the container. The destructors of the elements are called and the used storage is deallocated. Note, that if the elements are pointers, the pointed-to objects are not destroyed. 

<h2>Complexity</h2>

Linear in the size of the container.
