---
title: "stdpmrpolymorphic_allocatorallocate_object(3)"
name: "stdpmrpolymorphic_allocatorallocate_object"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrpolymorphic_allocatorallocate_object/"
description: "std::pmr::polymorphic_allocator<T>::allocate_object – std::pmr::polymorphic_allocator<T>::allocate_object"
---

<p>std::pmr::polymorphic_allocator&lt;T&gt;::allocate_object &#8211; std::pmr::polymorphic_allocator&lt;T&gt;::allocate_object</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class U&gt;
(since C++ 20)

    U *allocate_object(std::size_t n = 1);
Allocates storage for n objects of type U using the underlying memory resource.

If SIZE_MAX / sizeof(U) &lt; n, throws std::length_error, otherwise equivalent to return static_cast&lt;U*&gt;(allocate_bytes(n * sizeof(U), alignof(U)) );
</code></pre>
<h2>Parameters</h2>
<p>n &#8211; the number of objects to allocate storage for</p>
<h2>Return value</h2>
<p>A pointer to the allocated storage. </p>
<h2>Notes</h2>
<p>This function was introduced for use with the fully-specialized allocator std::polymorphic_allocator&lt;&gt;, but it may be useful in any specialization as a shortcut to avoid having to rebind from std::polymorphic_allocator&lt;T&gt; to std::polymorphic_allocator&lt;U&gt;.<br />
Since U is not deduced, it must be provided as a template argument when calling this function. </p>
<h2>Exceptions</h2>
<p>Throws std::length_error if n &gt; SIZE_MAX / sizeof(T); may also any exceptions thrown by the call to resource()-&gt;allocate.</p>
<h2>See also</h2>
<p>allocate_bytes Allocate raw aligned memory from the underlying resource<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
new_object Allocates and constructs an object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Allocate memory<br />
allocate <i>(public member function)</i><br />
allocate allocates uninitialized storage using the allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::allocator_traits&lt;Alloc&gt;)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocates memory<br />
allocate <i>(public member function of std::pmr::memory_resource)</i> </p>
