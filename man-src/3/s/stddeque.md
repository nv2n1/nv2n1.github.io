---
title: "stddeque(3)"
name: "stddeque"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddeque/"
---

std::deque&lt;T,Allocator&gt;::~deque - std::deque&lt;T,Allocator&gt;::~deque

<h2>Synopsis</h2>

<pre><code>~deque();</code></pre> 
Destructs the container. The destructors of the elements are called and the used storage is deallocated. Note, that if the elements are pointers, the pointed-to objects are not destroyed. 

<h2>Complexity</h2>

Linear in the size of the container.
