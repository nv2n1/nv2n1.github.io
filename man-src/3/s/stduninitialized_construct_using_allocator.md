---
title: "stduninitialized_construct_using_allocator(3)"
name: "stduninitialized_construct_using_allocator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduninitialized_construct_using_allocator/"
---

std::uninitialized_construct_using_allocator - std::uninitialized_construct_using_allocator

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
template&lt; class T, class Alloc, class... Args &gt; <i>(since C++20)</i> 
T* uninitialized_construct_using_allocator( T* p, const Alloc&amp; alloc, Args&amp;&amp;... args ) 
Creates an object of the given type T by means of uses-allocator_construction at the uninitialized memory location indicated by p 
Equivalent to <pre><code>return ::new (static_cast&lt;void *&gt;(p)) T(
    std::make_obj_using_allocator&lt;T&gt;(alloc, std::forward&lt;Args&gt;(args)...)

);
</code></pre>

<h2>Parameters</h2>

p - the memory location where the object will be placed. 
alloc - the allocator to use. 
args - the arguments to pass to T's constructor

<h2>Return value</h2>

Pointer to the newly-created object of type T 

<h2>Exceptions</h2>

May throw any exception thrown by the constructor of T, typically including std::bad_alloc

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

uses_allocator checks if the specified type supports uses-allocator construction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
make_obj_using_allocator creates an object of the given type by means of uses-allocator construction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
