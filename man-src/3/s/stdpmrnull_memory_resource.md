---
title: "stdpmrnull_memory_resource(3)"
name: "stdpmrnull_memory_resource"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrnull_memory_resource/"
---

std::pmr::null_memory_resource - std::pmr::null_memory_resource

<h2>Synopsis</h2>

Defined in header &lt;memory_resource&gt; 
std::pmr::memory_resource* null_memory_resource() noexcept; <i>(since C++17)</i> 
Returns a pointer to a memory_resource that doesn't perform any allocation. 

<h2>Return value</h2>

Returns a pointer p to a static storage duration object of a type derived from std::pmr::memory_resource, with the following properties: 
* its allocate() function always throws std::bad_alloc; 
* its deallocate() function has no effect; 
* for any memory_resource r, p-&gt;is_equal(r) returns &amp;r == p. 
The same value is returned every time this function is called. 
