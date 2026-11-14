---
title: "stdrangesequal_to(3)"
name: "stdrangesequal_to"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesequal_to/"
---

std::ranges::equal_to - std::ranges::equal_to

<h2>Synopsis</h2>

Defined in header &lt;functional&gt; 
struct equal_to; <i>(since C++20)</i> 
Function object for performing comparisons. Deduces the parameter types of the function call operator from the arguments (but not the return type). 

<h2>Member types</h2>

Member type Definition 
is_transparent /* unspecified */

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the arguments are equal 
operator() <i>(public member function)</i> 

 

 
std::ranges::equal_to::operator() 

 

 
template&lt; class T, class U &gt; 
requires EqualityComparableWith&lt;T, U&gt; || 
/* std::declval&lt;T&gt;() == std::declval&lt;U&gt;() resolves to 
a built-in operator comparing pointers */ 
constexpr bool operator()(T&amp;&amp; t, U&amp;&amp; u) const; 

 
Compares t and u, equivalent to return std::forward&lt;T&gt;(t) == std::forward&lt;U&gt;(u);, except when that expression resolves to a call to a builtin operator == comparing pointers. 
When a call would invoke a built-in operator comparing pointers of type P, the result is instead determined as follows: 

 
* Returns false if one of the (possibly converted) value of the first argument and the (possibly converted) value of the second argument precedes the other in the implementation-defined strict total ordering over all pointer values of type P. This strict total ordering is consistent with the partial order imposed by the builtin operators &lt;, &gt;, &lt;=, and &gt;=. 
* Otherwise (neither precedes the other), returns true. 

 
The behavior is undefined unless the the conversion sequences from both T and U to P are equality-preserving (see below). 

 
Equality preservation 

 
An expression is equality preserving if it results in equal outputs given equal inputs. 

 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 

 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects.

<h2>Notes</h2>

Unlike std::equal_to, std::ranges::equal_to requires both == and != to be valid (via the EqualityComparableWith constraint). 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x == y 
equal_to <i>(class template)</i> 
