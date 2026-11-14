---
title: "stdpointer_traitsto_address(3)"
name: "stdpointer_traitsto_address"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpointer_traitsto_address/"
description: "std::pointer_traits<Ptr>::to_address – std::pointer_traits<Ptr>::to_address"
---

<p>std::pointer_traits&lt;Ptr&gt;::to_address &#8211; std::pointer_traits&lt;Ptr&gt;::to_address</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
static element_type* to_address(pointer p) noexcept; <code>(1)</code> <i>(since C++20)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(optional member of user-defined specialization)<br />
Constructs a raw pointer that references the same object as its pointer-like (&quot;fancy pointer&quot;) argument.<br />
This function, if defined, is the inverse of pointer_to, and exists as the customization point to be called by std::to_address. </p>
<h2>Parameters</h2>
<p>p &#8211; fancy pointer/pointer-like object</p>
<h2>Return value</h2>
<p>A raw pointer of the type element_type* that references the same memory location as the argument p </p>
<h2>See also</h2>
<p>pointer_to obtains a dereferenceable pointer to its argument<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
to_address obtains a raw pointer from a pointer-like type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
