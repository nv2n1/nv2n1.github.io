---
title: "stdallocator_traitsdestroy(3)"
name: "stdallocator_traitsdestroy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocator_traitsdestroy/"
---

std::allocator_traits&lt;Alloc&gt;::destroy - std::allocator_traits&lt;Alloc&gt;::destroy

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;memory&gt;

    template &lt;class T&gt;
    (since C++ 11)

        static void destroy(Alloc &amp;a, T *p);</code></pre> 
Calls the destructor of the object pointed to by p. If possible, does so by calling a.destroy(p). If not possible (e.g. a does not have the member function destroy()), then calls the destructor of *p directly, as p-&gt;~T(). 

<h2>Parameters</h2>

a - allocator to use for destruction 
p - pointer to the object being destroyed

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

Because this function provides the automatic fall back to direct call to the destructor, the member function destroy() is an optional Allocator requirement since C++11. 

<h2>See also</h2>

destroy destructs an object in allocated storage 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function of std::allocator&lt;T&gt;)</i> 
(deprecated in C++17) 
(removed in C++20) 
