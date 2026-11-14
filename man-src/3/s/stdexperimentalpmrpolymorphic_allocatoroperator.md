---
title: "stdexperimentalpmrpolymorphic_allocatoroperator(3)"
name: "stdexperimentalpmrpolymorphic_allocatoroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrpolymorphic_allocatoroperator/"
---

std::experimental::pmr::polymorphic_allocator&lt;T&gt;::operator= - std::experimental::pmr::polymorphic_allocator&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>polymorphic_allocator &amp;operator=(const polymorphic_allocator &amp;rhs) = default;
(library fundamentals TS)</code></pre> 
Copy assigns this polymorphic_allocator. Sets the memory resource pointer of *this to that of rhs. 

<h2>Parameters</h2>

rhs - another polymorphic_allocator to copy from

<h2>Return value</h2>

*this 
