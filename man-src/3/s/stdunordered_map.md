---
title: "stdunordered_map(3)"
name: "stdunordered_map"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunordered_map/"
---

std::unordered_map&lt;Key,T,Hash,KeyEqual,Allocator&gt;::~unordered_map - std::unordered_map&lt;Key,T,Hash,KeyEqual,Allocator&gt;::~unordered_map

<h2>Synopsis</h2>

~unordered_map(); <i>(since C++11)</i> 
Destructs the container. The destructors of the elements are called and the used storage is deallocated. Note, that if the elements are pointers, the pointed-to objects are not destroyed. 

<h2>Complexity</h2>

Linear in the size of the container.
