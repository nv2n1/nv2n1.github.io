---
title: "stdexperimentalpmrpolymorphic_allocatorallocate(3)"
name: "stdexperimentalpmrpolymorphic_allocatorallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrpolymorphic_allocatorallocate/"
description: "std::experimental::pmr::polymorphic_allocator<T>::allocate – std::experimental::pmr::polymorphic_allocator<T>::allocate"
---

<p>std::experimental::pmr::polymorphic_allocator&lt;T&gt;::allocate &#8211; std::experimental::pmr::polymorphic_allocator&lt;T&gt;::allocate</p>
<h2>Synopsis</h2>
<p>T* allocate( std::size_t n ); (library fundamentals TS) </p>
<pre><code>Allocates storage for n objects of type T using the underlying memory resource. Equivalent to return static_cast&lt;T*&gt;(this-&gt;resource()-&gt;allocate(n * sizeof(T), alignof(T)));
</code></pre>
<h2>Parameters</h2>
<p>n &#8211; the number of objects to allocate storage for</p>
<h2>Return value</h2>
<p>A pointer to the allocated storage. </p>
<h2>See also</h2>
<p>allocate allocates uninitialized storage using the allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::allocator_traits&lt;Alloc&gt;)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocates memory<br />
deallocate <i>(public member function of std::experimental::pmr::memory_resource)</i> </p>
