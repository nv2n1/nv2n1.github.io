---
title: "stdexperimentalpromisepromiselibraryfundamentalsts(3)"
name: "stdexperimentalpromisepromiselibraryfundamentalsts"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpromisepromiselibraryfundamentalsts/"
---

std::experimental::promise&lt;R&gt;::promise(libraryfundamentalsTS) - std::experimental::promise&lt;R&gt;::promise(libraryfundamentalsTS)

<h2>Synopsis</h2>

<pre><code>promise();
(1)(library fundamentals TS)

    template &lt;class Alloc&gt;
    (2)(library fundamentals TS)

        promise(std::allocator_arg_t, const Alloc &amp;alloc);

promise(promise &amp;&amp;other) noexcept;
(3)(library fundamentals TS)

    promise(const promise &amp;other) = delete;
(4)(library fundamentals TS)</code></pre> 
Constructs a std::experimental::promise object. 
1) Default constructor. Constructs the promise with an empty shared state. 
2) Constructs the promise with an empty shared state. The shared state is allocated using alloc, which is treated as a type-erased allocator (see below). 
3) Move constructor. Constructs the promise with the shared state of other using move semantics. After construction, other has no shared state. 
4) std::experimental::promise is not copyable. 
Type-erased allocator 
The constructors of promise taking an allocator argument alloc treats that argument as a type-erased allocator. The memory resource pointer used by promise to allocate memory is determined using the allocator argument (if specified) as follows: 
Type of alloc value of the memory resource pointer 
Non-existent (no allocator specified at time of construction) The value of std::experimental::pmr::get_default_resource() at time of construction. 
std::nullptr_t The value of std::experimental::pmr::get_default_resource() at time of construction 
A pointer type convertible to static_cast&lt;std::experimental::pmr::memory_resource*&gt;(alloc) 
std::experimental::pmr::memory_resource* 
A specialization of alloc.resource() 
std::experimental::pmr::polymorphic_allocator 
Any other type meeting the Allocator requirements A pointer to a value of type std::experimental::pmr::resource_adaptor&lt;A&gt;(alloc), where A is the type of alloc. The pointer remains valid only for the lifetime of the promise object. 
None of the above The program is ill-formed. 

<h2>Parameters</h2>

alloc - allocator to use to allocate the shared state 
other - another std::experimental::promise to acquire the state from

<h2>Exceptions</h2>

1-2) <i>(none)</i>
