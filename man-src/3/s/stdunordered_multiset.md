---
title: "stdunordered_multiset(3)"
name: "stdunordered_multiset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunordered_multiset/"
---

std::unordered_multiset&lt;Key,Hash,KeyEqual,Allocator&gt;::~unordered_multiset - std::unordered_multiset&lt;Key,Hash,KeyEqual,Allocator&gt;::~unordered_multiset

<h2>Synopsis</h2>

~unordered_multiset(); <i>(since C++11)</i> 
Destructs the container. The destructors of the elements are called and the used storage is deallocated. Note, that if the elements are pointers, the pointed-to objects are not destroyed. 

<h2>Complexity</h2>

Linear in the size of the container.
