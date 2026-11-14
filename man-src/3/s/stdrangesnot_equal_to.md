---
title: "stdrangesnot_equal_to(3)"
name: "stdrangesnot_equal_to"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesnot_equal_to/"
---

std::ranges::not_equal_to - std::ranges::not_equal_to

<h2>Synopsis</h2>

Defined in header &lt;functional&gt; 
struct not_equal_to; <i>(since C++20)</i> 
Function object for performing comparisons. Deduces the parameter types of the function call operator from the arguments (but not the return type). 

<h2>Member types</h2>

Member type Definition 
is_transparent /* unspecified */

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the arguments are not equal 
operator() <i>(public member function)</i> 

 

 
std::ranges::not_equal_to::operator() 

 

 
template&lt; class T, class U &gt; 
requires EqualityComparableWith&lt;T, U&gt; || 
/* std::declval&lt;T&gt;() == std::declval&lt;U&gt;() resolves to 
a built-in operator comparing pointers */ 
constexpr bool operator()(T&amp;&amp; t, U&amp;&amp; u) const; 

 
Compares t and u. Equivalent to return !ranges::equal_to{}(std::forward&lt;T&gt;(t), std::forward&lt;U&gt;(u));.

<h2>Notes</h2>

Unlike std::not_equal_to, std::ranges::not_equal_to requires both == and != to be valid (via the EqualityComparableWith constraint), and is entirely defined in terms of std::ranges::equal_to. However, the implementation is free to use operator!= directly, because those concepts require the results of == and != to be consistent. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x != y 
not_equal_to <i>(class template)</i> 
