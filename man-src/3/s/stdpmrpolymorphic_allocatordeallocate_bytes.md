---
title: "stdpmrpolymorphic_allocatordeallocate_bytes(3)"
name: "stdpmrpolymorphic_allocatordeallocate_bytes"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrpolymorphic_allocatordeallocate_bytes/"
description: "std::pmr::polymorphic_allocator<T>::deallocate_bytes – std::pmr::polymorphic_allocator<T>::deallocate_bytes"
---

<p>std::pmr::polymorphic_allocator&lt;T&gt;::deallocate_bytes &#8211; std::pmr::polymorphic_allocator&lt;T&gt;::deallocate_bytes</p>
<h2>Synopsis</h2>
<pre><code>void deallocate_bytes(void *p,

                      std::size_t nbytes, (since C++ 20)

                                              std::size_t alignment = alignof(std::max_align_t));
Deallocates the storage pointed to by p, which must have been allocated from a std::pmr::memory_resource x that compares equal to *resource(). using x.allocate(nbytes, alignment), typically through a call to allocate_bytes(nbytes, alignment.

Equivalent to resorce()-&gt;deallocate(p, nbytes, alignment);
</code></pre>
<h2>Parameters</h2>
<p>p &#8211; pointer to memory to deallocate<br />
nbytes &#8211; the number of bytes originally allocated<br />
alignment &#8211; the alignment originally allocated</p>
<h2>Exceptions</h2>
<p>Throws nothing.</p>
<h2>Notes</h2>
<p>This function was introduced for use with the fully-specialized allocator std::polymorphic_allocator&lt;&gt;, but it may be useful in any specialization. </p>
<h2>See also</h2>
<p>deallocate_object Frees raw memory obtained by allocate_object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
delete_object Destroys and deallocates an object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
deallocate deallocates storage using the allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::allocator_traits&lt;Alloc&gt;)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocates memory<br />
deallocate <i>(public member function of std::pmr::memory_resource)</i> </p>
