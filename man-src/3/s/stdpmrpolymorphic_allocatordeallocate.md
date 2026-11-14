---
title: "stdpmrpolymorphic_allocatordeallocate(3)"
name: "stdpmrpolymorphic_allocatordeallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrpolymorphic_allocatordeallocate/"
description: "std::pmr::polymorphic_allocator<T>::deallocate – std::pmr::polymorphic_allocator<T>::deallocate"
---

<p>std::pmr::polymorphic_allocator&lt;T&gt;::deallocate &#8211; std::pmr::polymorphic_allocator&lt;T&gt;::deallocate</p>
<h2>Synopsis</h2>
<pre><code>void deallocate(T *p, std::size_t n);
(since C++ 17)
    Deallocates the storage pointed to by p,
    which must have been allocated from a std::pmr::memory_resource x that compares equal to *resource() using x.allocate(n * sizeof(T), alignof(T)).

    Equivalent to this-&gt;resource()
        -&gt;deallocate(p, n * sizeof(T), alignof(T));
</code></pre>
<h2>Parameters</h2>
<p>p &#8211; pointer to memory to deallocate<br />
n &#8211; the number of objects originally allocated</p>
<h2>Exceptions</h2>
<p>Throws nothing.</p>
<h2>See also</h2>
<p>deallocate_bytes Free raw memory obtained from allocate_bytes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
deallocate_object Frees raw memory obtained by allocate_object<br />
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
