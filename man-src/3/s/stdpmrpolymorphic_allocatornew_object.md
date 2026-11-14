---
title: "stdpmrpolymorphic_allocatornew_object(3)"
name: "stdpmrpolymorphic_allocatornew_object"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrpolymorphic_allocatornew_object/"
description: "std::pmr::polymorphic_allocator<T>::new_object – std::pmr::polymorphic_allocator<T>::new_object"
---

<p>std::pmr::polymorphic_allocator&lt;T&gt;::new_object &#8211; std::pmr::polymorphic_allocator&lt;T&gt;::new_object</p>
<h2>Synopsis</h2>
<pre><code>template&lt; class U, class CtorArgs... &gt;     (since C++20)

U* new_object( CtorArgs&amp;&amp;... ctor_args );</code></pre>
<p>Allocates and constructs an object of type U.<br />
Equivalent to </p>
<pre><code>U *p = allocate_object&lt;U&gt;();

try {
    construct(p, std::forward&lt;CtorArgs&gt;(ctor_args)...);

} catch (...) {
    deallocate_object(p);
    throw;
}

return p;
</code></pre>
<h2>Parameters</h2>
<p>ctor_args &#8211; the arguments to forward to the the constructor of U</p>
<h2>Return value</h2>
<p>A pointer to the allocated and constructed object. </p>
<h2>Notes</h2>
<p>This function was introduced for use with the fully-specialized allocator std::polymorphic_allocator&lt;&gt;, but it may be useful in any specialization as a shortcut to avoid having to rebind from std::polymorphic_allocator&lt;T&gt; to std::polymorphic_allocator&lt;U&gt;, and having to call allocate, construct, and deallocate individually.<br />
Since U is not deduced, it must be provided as a template argument when calling this function. </p>
<h2>Exceptions</h2>
<p>May throw any exceptions thrown by the call to allocate_object or the constructor of U.</p>
<h2>See also</h2>
<p>allocate_bytes Allocate raw aligned memory from the underlying resource<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
allocate_object Allocates raw memory suitable for an object or an array<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(C++20)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Allocate memory<br />
allocate <i>(public member function)</i><br />
allocate allocates uninitialized storage using the allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::allocator_traits&lt;Alloc&gt;)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocates memory<br />
allocate <i>(public member function of std::pmr::memory_resource)</i> </p>
