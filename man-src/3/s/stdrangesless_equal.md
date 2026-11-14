---
title: "stdrangesless_equal(3)"
name: "stdrangesless_equal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesless_equal/"
---

std::ranges::less_equal - std::ranges::less_equal

<h2>Synopsis</h2>

Defined in header &lt;functional&gt; 
struct less_equal; <i>(since C++20)</i> 
Function object for performing comparisons. Deduces the parameter types of the function call operator from the arguments (but not the return type). 

<h2>Member types</h2>

Member type Definition 
is_transparent /* unspecified */

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the first argument is less than or equal to the second 
operator() <i>(public member function)</i> 

 

 
std::ranges::less_equal::operator() 

 

 
template&lt; class T, class U &gt; 
requires StrictTotallyOrderedWith&lt;T, U&gt; || 
/* std::declval&lt;T&gt;() &lt; std::declval&lt;U&gt;() resolves to 
a built-in operator comparing pointers */ 
constexpr bool operator()(T&amp;&amp; t, U&amp;&amp; u) const; 

 
Compares t and u. Equivalent to return !ranges::less{}(std::forward&lt;U&gt;(u), std::forward&lt;T&gt;(t));.

<h2>Notes</h2>

Unlike std::less_equal, std::ranges::less_equal requires all six comparison operators &lt;, &lt;=, &gt;, &gt;=, == and != to be valid (via the StrictTotallyOrderedWith constraint) and is entirely defined in terms of std::ranges::less. However, the implementation is free to use operator&lt;= directly, because those concepts require the results of the comparison operators to be consistent. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x &lt;= y 
less_equal <i>(class template)</i> 
