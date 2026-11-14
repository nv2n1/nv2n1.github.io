---
title: "stdallocator_traitsmax_size(3)"
name: "stdallocator_traitsmax_size"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocator_traitsmax_size/"
---

std::allocator_traits&lt;Alloc&gt;::max_size - std::allocator_traits&lt;Alloc&gt;::max_size

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
static size_type max_size( const Alloc&amp; a ) noexcept; <i>(since C++11)</i> 
If possible, obtains the maximum theoretically possible allocation size from the allocator a, by calling 
a.max_size() 
If the above is not possible (e.g. a does not have the member function max_size()), then returns 
std::numeric_limits&lt;size_type&gt;::max() 
<i>(until C++17)</i> 
std::numeric_limits&lt;size_type&gt;::max() / sizeof(value_type) 
<i>(since C++17)</i> 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Theoretical maximum allocation size 

<h2>See also</h2>

max_size returns the largest supported allocation size 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function of std::allocator&lt;T&gt;)</i> 
(deprecated in C++17) 
(removed in C++20) 
