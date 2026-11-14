---
title: "stdallocator_traitsallocate(3)"
name: "stdallocator_traitsallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocator_traitsallocate/"
---

std::allocator_traits&lt;Alloc&gt;::allocate - std::allocator_traits&lt;Alloc&gt;::allocate

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;memory&gt;

static pointer allocate( Alloc&amp; a, size_type n );                       (since C++11)
(until C++20)

[[nodiscard]] static pointer allocate( Alloc&amp; a, size_type n );         (since C++20)

static pointer allocate( Alloc&amp; a, size_type n,                 (1)                    (since C++11)

const_void_pointer hint );                                          (2)                (until C++20)

[[nodiscard]] static pointer allocate( Alloc&amp; a, size_type n,                          (since C++20)

const_void_pointer hint );</code></pre> 
Uses the allocator a to allocate n*sizeof(Alloc::value_type) bytes of uninitialized storage. 
1) Calls <a HREF="/docs/linux/man/n-a-allocate/">a.allocate</a>(n) 
2) Additionally passes memory locality hint hint. Calls a.allocate(n, hint) if possible. If not possible (e.g. a has no two-argument member function allocate()), calls <a HREF="/docs/linux/man/n-a-allocate/">a.allocate</a>(n) 

<h2>Parameters</h2>

a - allocator to use 
n - the number of objects to allocate storage for 
hint - pointer to a nearby memory location

<h2>Return value</h2>

The pointer returned by the call to <a HREF="/docs/linux/man/n-a-allocate/">a.allocate</a>(n) 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocates uninitialized storage 
allocate <i>(public member function of std::allocator&lt;T&gt;)</i> 
