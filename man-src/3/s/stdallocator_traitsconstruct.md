---
title: "stdallocator_traitsconstruct(3)"
name: "stdallocator_traitsconstruct"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocator_traitsconstruct/"
---

std::allocator_traits&lt;Alloc&gt;::construct - std::allocator_traits&lt;Alloc&gt;::construct

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;memory&gt;

    template &lt;class T, class... Args&gt;
    (since C++ 11)

        static void construct(Alloc &amp;a, T *p, Args &amp;&amp;...args);</code></pre> 
If possible, constructs an object of type T in allocated uninitialized storage pointed to by p, by calling 
a.construct(p, std::forward&lt;Args&gt;(args)...) 
If the above is not possible (e.g. a does not have the member function construct(),), then calls placement-new as 
::new (static_cast&lt;void*&gt;(p)) T(std::forward&lt;Args&gt;(args)...) 

<h2>Parameters</h2>

a - allocator to use for construction 
args... - the constructor arguments to pass to a.construct() or to placement-new

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

This function is used by the standard library containers when inserting, copying, or moving elements. 
Because this function provides the automatic fall back to placement new, the member function construct() is an optional Allocator requirement since C++11. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocation functions 
operator_new <i>(function)</i> 
operator_new[] 
construct constructs an object in allocated storage 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function of std::allocator&lt;T&gt;)</i> 
(deprecated in C++17) 
(removed in C++20) 
