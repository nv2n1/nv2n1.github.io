---
title: "stdallocator_arg_t(3)"
name: "stdallocator_arg_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocator_arg_t/"
---

std::allocator_arg_t - std::allocator_arg_t

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;memory&gt;

    struct allocator_arg_t {
};
(since C++ 11)(until C++ 17)

    struct allocator_arg_t {
    explicit allocator_arg_t() = default;
};
(since C++ 17)</code></pre> 
std::allocator_arg_t is an empty class type used to disambiguate the overloads of constructors and member functions of allocator-aware objects, including std::tuple, 
std::function, std::packaged_task, 
<i>(until C++17)</i>and std::promise. 

<h2>See also</h2>

allocator_arg an object of type std::allocator_arg_t used to select allocator-aware constructors 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(constant) 
<i>(C++11)</i> 
uses_allocator checks if the specified type supports uses-allocator construction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
