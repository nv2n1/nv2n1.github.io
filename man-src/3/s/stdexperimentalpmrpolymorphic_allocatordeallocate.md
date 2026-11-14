---
title: "stdexperimentalpmrpolymorphic_allocatordeallocate(3)"
name: "stdexperimentalpmrpolymorphic_allocatordeallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrpolymorphic_allocatordeallocate/"
description: "std::experimental::pmr::polymorphic_allocator<T>::deallocate – std::experimental::pmr::polymorphic_allocator<T>::deallocate"
---

<p>std::experimental::pmr::polymorphic_allocator&lt;T&gt;::deallocate &#8211; std::experimental::pmr::polymorphic_allocator&lt;T&gt;::deallocate</p>
<h2>Synopsis</h2>
<pre><code>void deallocate(T *p, std::size_t n);
(library fundamentals TS)
    Deallocates the storage pointed to by p,
    which must have been allocated from a memory_resource x that compares equal to *resource() using x.allocate(n * sizeof(T), alignof(T)).

    Equivalent to this-&gt;resource()
        -&gt;deallocate(p, n * sizeof(T), alignof(T));
</code></pre>
<h2>Parameters</h2>
<p>p &#8211; pointer to memory to deallocate<br />
n &#8211; the number of objects originally allocated</p>
<h2>Exceptions</h2>
<p>Throws nothing.</p>
<h2>See also</h2>
<p>deallocate deallocates storage using the allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::allocator_traits&lt;Alloc&gt;)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocates memory<br />
deallocate <i>(public member function of std::experimental::pmr::memory_resource)</i> </p>
