---
title: "stdpointer_traitspointer_to(3)"
name: "stdpointer_traitspointer_to"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpointer_traitspointer_to/"
description: "std::pointer_traits<Ptr>::pointer_to – std::pointer_traits<Ptr>::pointer_to"
---

<p>std::pointer_traits&lt;Ptr&gt;::pointer_to &#8211; std::pointer_traits&lt;Ptr&gt;::pointer_to</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
static pointer <code>(1)</code> <i>(since C++11)</i><br />
pointer_to( element_type&amp; r ); (member of pointer_traits&lt;Ptr&gt; specialization)<br />
static pointer <i>(since C++11)</i><br />
pointer_to( element_type&amp; r ) noexcept; <i>(until C++20)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>(2)</code> (member of pointer_traits&lt;T*&gt; specialization)<br />
static constexpr pointer <i>(since C++20)</i><br />
pointer_to( element_type&amp; r ) noexcept; (member of pointer_traits&lt;T*&gt; specialization)<br />
Constructs a dereferenceable pointer or pointer-like object (&quot;fancy pointer&quot;) to its argument.<br />
1) The version of this function in the non-specialized std::pointer_traits template simply calls Ptr::pointer_to(r), and if Ptr does not provide a static member function pointer_to, instantiation of this function is a compile-time error.<br />
2) The version of this function in the specialization of std::pointer_traits for pointer types returns std::addressof(r) </p>
<h2>Parameters</h2>
<p>r &#8211; reference to an object of type element_type&amp;, except if element_type is void, in which case the type of r is unspecified</p>
<h2>Return value</h2>
<p>A dereferenceable pointer to r, of the type pointer_traits&lt;&gt;::pointer. </p>
<h2>Exceptions</h2>
<p>1) Unspecified (typically same as Ptr::pointer_to)</p>
<h2>Notes</h2>
<p>The Boost.Intrusive_library_version of this function returns pointer(std::addressof(r)) if Ptr::pointer_to does not exist. </p>
<h2>See also</h2>
<p>addressof obtains actual address of an object, even if the &amp; operator is overloaded<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
address obtains the address of an object, even if operator&amp; is overloaded<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function of std::allocator&lt;T&gt;)</i><br />
(deprecated in C++17)<br />
(removed in C++20)<br />
to_address obtains a raw pointer from a fancy pointer (inverse of pointer_to)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> (C++20)<br />
to_address obtains a raw pointer from a pointer-like type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
