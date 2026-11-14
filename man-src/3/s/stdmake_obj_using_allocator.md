---
title: "stdmake_obj_using_allocator(3)"
name: "stdmake_obj_using_allocator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_obj_using_allocator/"
---

std::make_obj_using_allocator - std::make_obj_using_allocator

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
template&lt; class T, class Alloc, class... Args &gt; <i>(since C++20)</i> 
T make_obj_using_allocator( const Alloc&amp; alloc, Args&amp;&amp;... args ) 
Creates an object of the given type T by means of uses-allocator_construction 
Equivalent to <pre><code>return std::make_from_tuple&lt;T&gt;(
    std::uses_allocator_construction_args&lt;T&gt;(alloc, std::forward&lt;Args&gt;(args)...)

);
</code></pre>

<h2>Parameters</h2>

alloc - the allocator to use. 
args - the arguments to pass to T's constructor

<h2>Return value</h2>

The newly-created object of type T 

<h2>Exceptions</h2>

May throw any exception thrown by the constructor of T, typically including std::bad_alloc

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

uses_allocator_construction_args prepares the argument list matching the flavor of uses-allocator construction required by the given type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
uninitialized_construct_using_allocator creates an object of the given type at specified memory location by means of uses-allocator construction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
