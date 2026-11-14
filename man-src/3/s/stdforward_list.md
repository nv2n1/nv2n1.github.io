---
title: "stdforward_list(3)"
name: "stdforward_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdforward_list/"
---

std::forward_list&lt;T,Allocator&gt;::~forward_list - std::forward_list&lt;T,Allocator&gt;::~forward_list

<h2>Synopsis</h2>

~forward_list(); <i>(since C++11)</i> 
Destructs the container. The destructors of the elements are called and the used storage is deallocated. Note, that if the elements are pointers, the pointed-to objects are not destroyed. 

<h2>Complexity</h2>

Linear in the size of the container.
