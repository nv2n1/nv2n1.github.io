---
title: "stdallocator_arg(3)"
name: "stdallocator_arg"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocator_arg/"
---

std::allocator_arg - std::allocator_arg

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;memory&gt;

constexpr std::allocator_arg_t allocator_arg = std::allocator_arg_t();         (since C++11)
(until C++17)

inline constexpr std::allocator_arg_t allocator_arg = std::allocator_arg_t();  (since C++17)</code></pre> 
std::allocator_arg is a constant of type std::allocator_arg_t used to disambiguate, at call site, the overloads of the constructors and member functions of allocator-aware objects, such as std::tuple, 
std::function, std::packaged_task, 
<i>(until C++17)</i>and std::promise. 

<h2>See also</h2>

allocator_arg_t tag type used to select allocator-aware constructor overloads 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
uses_allocator checks if the specified type supports uses-allocator construction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
