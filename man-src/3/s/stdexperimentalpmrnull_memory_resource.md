---
title: "stdexperimentalpmrnull_memory_resource(3)"
name: "stdexperimentalpmrnull_memory_resource"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrnull_memory_resource/"
---

std::experimental::pmr::null_memory_resource - std::experimental::pmr::null_memory_resource

<h2>Synopsis</h2>

Defined in header &lt;experimental/memory_resource&gt; 
memory_resource* null_memory_resource() noexcept; (library fundamentals TS) 
Returns a pointer to a memory_resource that doesn't perform any allocation. 

<h2>Return value</h2>

Returns a pointer p to a static storage duration object of a type derived from std::experimental::pmr::memory_resource, with the following properties: 
* its allocate() function always throws std::bad_alloc; 
* its deallocate() function has no effect; 
* for any memory_resource r, p-&gt;is_equal(r) returns &amp;r == p. 
The same value is returned every time this function is called. 
