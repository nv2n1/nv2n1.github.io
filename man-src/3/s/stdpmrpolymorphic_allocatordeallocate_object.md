---
title: "stdpmrpolymorphic_allocatordeallocate_object(3)"
name: "stdpmrpolymorphic_allocatordeallocate_object"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrpolymorphic_allocatordeallocate_object/"
description: "std::pmr::polymorphic_allocator<T>::deallocate_object – std::pmr::polymorphic_allocator<T>::deallocate_object"
---

<p>std::pmr::polymorphic_allocator&lt;T&gt;::deallocate_object &#8211; std::pmr::polymorphic_allocator&lt;T&gt;::deallocate_object</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class U&gt;
(since C++ 20)

    void deallocate_object(U *p, std::size_t n = 1);
Deallocates the storage pointed to by p, which must have been allocated from a std::pmr::memory_resource x that compares equal to *resource().using x.allocate(n * sizeof(U), alignof(U)), typically through a call to allocate_object&lt;U&gt;(n).

                                                                                                                                                                                           Equivalent to deallocate_bytes(p, n * sizeof(U), alignof(U));
</code></pre>
<h2>Parameters</h2>
<p>p &#8211; pointer to memory to deallocate<br />
n &#8211; number of objects of type U the memory was for</p>
<h2>Exceptions</h2>
<p>Throws nothing.</p>
<h2>Notes</h2>
<p>This function was introduced for use with the fully-specialized allocator std::polymorphic_allocator&lt;&gt;, but it may be useful in any specialization. </p>
<h2>See also</h2>
<p>deallocate_bytes Free raw memory obtained from allocate_bytes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
delete_object Destroys and deallocates an object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
deallocate deallocates storage using the allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::allocator_traits&lt;Alloc&gt;)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocates memory<br />
deallocate <i>(public member function of std::pmr::memory_resource)</i> </p>
