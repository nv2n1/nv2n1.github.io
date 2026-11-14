---
title: "stdpmrpolymorphic_allocatorallocate_bytes(3)"
name: "stdpmrpolymorphic_allocatorallocate_bytes"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrpolymorphic_allocatorallocate_bytes/"
description: "std::pmr::polymorphic_allocator<T>::allocate_bytes – std::pmr::polymorphic_allocator<T>::allocate_bytes"
---

<p>std::pmr::polymorphic_allocator&lt;T&gt;::allocate_bytes &#8211; std::pmr::polymorphic_allocator&lt;T&gt;::allocate_bytes</p>
<h2>Synopsis</h2>
<pre><code>void *allocate_bytes(std::size_t nbytes, (since C++ 20)

                                             std::size_t alignment = alignof(std::max_align_t));
Allocates nbytes bytes of storage at specified alignment alignment using the underlying memory resource.Equivalent to return resource()-&gt;allocate(nbytes, alignment);
</code></pre>
<h2>Parameters</h2>
<p>nbytes &#8211; the number of bytes to allocate<br />
alignment &#8211; the alignment to use</p>
<h2>Return value</h2>
<p>A pointer to the allocated storage. </p>
<h2>Notes</h2>
<p>This function was introduced for use with the fully-specialized allocator std::polymorphic_allocator&lt;&gt;, but it may be useful in any specialization.<br />
The return type is void* (rather than, e.g., std::byte*) to support conversion to an arbitrary pointer type U* by static_cast&lt;U*&gt;. </p>
<h2>Exceptions</h2>
<p>May throw any exceptions thrown by the call to resource()-&gt;allocate.</p>
<h2>See also</h2>
<p>allocate_object Allocates raw memory suitable for an object or an array<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
new_object Allocates and constructs an object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Allocate memory<br />
allocate <i>(public member function)</i><br />
allocate allocates uninitialized storage using the allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::allocator_traits&lt;Alloc&gt;)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocates memory<br />
allocate <i>(public member function of std::pmr::memory_resource)</i> </p>
