---
title: "stdallocatorallocate(3)"
name: "stdallocatorallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocatorallocate/"
description: "std::allocator<T>::allocate – std::allocator<T>::allocate"
---

<p>std::allocator&lt;T&gt;::allocate &#8211; std::allocator&lt;T&gt;::allocate</p>
<h2>Synopsis</h2>
<pre><code>pointer allocate(size_type n, const void *hint = 0);
(1)(until C++ 17)(since C++ 17)

    T *allocate(std::size_t n, const void *hint);
(1)(deprecated)(removed in C++ 20)

    T *allocate(std::size_t n);
(since C++ 17)(2)(until C++ 20)

    [[nodiscard]] T *allocate(std::size_t n);
(since C++ 20)</code></pre>
<p>Allocates n * sizeof(T) bytes of uninitialized storage by calling ::operator_new(std::size_t)<br />
or ::operator_new(std::size_t, std::align_val_t)<br />
<i>(since C++17)</i>, but it is unspecified when and how this function is called. The pointer hint may be used to provide locality of reference: the allocator, if supported by the implementation, will attempt to allocate the new memory block as close as possible to hint. </p>
<h2>Parameters</h2>
<p>n &#8211; the number of objects to allocate storage for<br />
hint &#8211; pointer to a nearby memory location</p>
<h2>Return value</h2>
<p>Pointer to the first byte of a memory block suitably aligned and sufficient to hold an array of n objects of type T. </p>
<h2>Exceptions</h2>
<p>Throws std::bad_alloc if allocation fails.</p>
<h2>Notes</h2>
<p>The &quot;unspecified when and how&quot; wording makes it possible to combine_or_optimize_away_heap_allocations made by the standard library containers, even though such optimizations are disallowed for direct calls to ::operator new. For example, this is implemented by libc++ ([1] and [2]) </p>
<h2>See also</h2>
<p>allocate allocates uninitialized storage using the allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::allocator_traits&lt;Alloc&gt;)</i><br />
<code>[static]</code> </p>
