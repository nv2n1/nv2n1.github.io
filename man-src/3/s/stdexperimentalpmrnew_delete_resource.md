---
title: "stdexperimentalpmrnew_delete_resource(3)"
name: "stdexperimentalpmrnew_delete_resource"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrnew_delete_resource/"
---

std::experimental::pmr::new_delete_resource - std::experimental::pmr::new_delete_resource

<h2>Synopsis</h2>

Defined in header &lt;experimental/memory_resource&gt; 
memory_resource* new_delete_resource() noexcept; (library fundamentals TS) 
Returns a pointer to a memory_resource that uses the global operator_new and operator_delete to allocate memory. 

<h2>Return value</h2>

Returns a pointer p to a static storage duration object of a type derived from std::experimental::pmr::memory_resource, with the following properties: 
* its allocate() function uses ::operator new to allocate memory; 
* its deallocate() function uses ::operator delete to deallocate memory; 
* for any memory_resource r, p-&gt;is_equal(r) returns &amp;r == p. 
The same value is returned every time this function is called. 
