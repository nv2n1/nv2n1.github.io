---
title: "stdpmrpolymorphic_allocatorallocate(3)"
name: "stdpmrpolymorphic_allocatorallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrpolymorphic_allocatorallocate/"
description: "std::pmr::polymorphic_allocator<T>::allocate – std::pmr::polymorphic_allocator<T>::allocate"
---

<p>std::pmr::polymorphic_allocator&lt;T&gt;::allocate &#8211; std::pmr::polymorphic_allocator&lt;T&gt;::allocate</p>
<h2>Synopsis</h2>
<p>T* allocate( std::size_t n ); <i>(since C++17)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++20)</i><br />
[[nodiscard]] T* allocate( std::size_t n ); <i>(since C++20)</i> </p>
<pre><code>Allocates storage for n objects of type T using the underlying memory resource. Equivalent to return static_cast&lt;T*&gt;(resource()-&gt;allocate(n * sizeof(T), alignof(T)));
.
</code></pre>
<h2>Parameters</h2>
<p>n &#8211; the number of objects to allocate storage for</p>
<h2>Return value</h2>
<p>A pointer to the allocated storage. </p>
<h2>Exceptions</h2>
<p>Throws std::length_error if n &gt; SIZE_MAX / sizeof(T); may also any exceptions thrown by the call to resource()-&gt;allocate.</p>
<h2>See also</h2>
<p>allocate_bytes Allocate raw aligned memory from the underlying resource<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
allocate_object Allocates raw memory suitable for an object or an array<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
new_object Allocates and constructs an object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
allocate allocates uninitialized storage using the allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::allocator_traits&lt;Alloc&gt;)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocates memory<br />
allocate <i>(public member function of std::pmr::memory_resource)</i> </p>
