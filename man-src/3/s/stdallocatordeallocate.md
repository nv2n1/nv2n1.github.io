---
title: "stdallocatordeallocate(3)"
name: "stdallocatordeallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocatordeallocate/"
description: "std::allocator<T>::deallocate – std::allocator<T>::deallocate"
---

<p>std::allocator&lt;T&gt;::deallocate &#8211; std::allocator&lt;T&gt;::deallocate</p>
<h2>Synopsis</h2>
<pre><code>void deallocate(T *p, std::size_t n);</code></pre>
<p>Deallocates the storage referenced by the pointer p, which must be a pointer obtained by an earlier call to allocate().<br />
The argument n must be equal to the first argument of the call to allocate() that originally produced p; otherwise, the behavior is undefined.<br />
Calls ::operator_delete(void*)<br />
or ::operator_delete(void*, std::align_val_t)<br />
<i>(since C++17)</i>, but it is unspecified when and how it is called. </p>
<h2>Parameters</h2>
<p>p &#8211; pointer obtained from allocate()<br />
n &#8211; number of objects earlier passed to allocate()</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocates uninitialized storage<br />
allocate <i>(public member function)</i><br />
deallocate deallocates storage using the allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::allocator_traits&lt;Alloc&gt;)</i><br />
<code>[static]</code> </p>
