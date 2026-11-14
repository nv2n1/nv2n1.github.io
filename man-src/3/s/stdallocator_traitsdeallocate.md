---
title: "stdallocator_traitsdeallocate(3)"
name: "stdallocator_traitsdeallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocator_traitsdeallocate/"
description: "std::allocator_traits<Alloc>::deallocate – std::allocator_traits<Alloc>::deallocate"
---

<p>std::allocator_traits&lt;Alloc&gt;::deallocate &#8211; std::allocator_traits&lt;Alloc&gt;::deallocate</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
static void deallocate( Alloc&amp; a, pointer p, size_type n ); <i>(since C++11)</i><br />
Uses the allocator a to deallocate the storage referenced by p, by calling a.deallocate(p, n) </p>
<h2>Parameters</h2>
<p>a &#8211; allocator to use<br />
p &#8211; pointer to the previously allocated storage<br />
n &#8211; the number of objects the storage was allocated for</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>See also</h2>
<p>allocate allocates uninitialized storage using the allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocates storage<br />
deallocate <i>(public member function of std::allocator&lt;T&gt;)</i> </p>
